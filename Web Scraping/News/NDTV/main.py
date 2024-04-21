from bs4 import BeautifulSoup
import requests
from joblib import Parallel, delayed
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from google.generativeai.types import HarmCategory, HarmBlockThreshold

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def get_news_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    news_paragraphs = soup.find_all('p')
    news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
    return news_text

def scrape_category(url_pattern, tag_name, pages):
    news_data = set()
    for page_num in range(1, pages + 1):
        r = requests.get(f'{url_pattern}{page_num}')
        soup = BeautifulSoup(r.text, 'lxml')
        news_items = soup.find_all(tag_name)
        for item in news_items:
            headline = item.text.strip()
            link = item.a['href']
            news_text = get_news_text(link)
            news_data.add((headline, link, news_text))
    return news_data

def process_category(category_params):
    return scrape_category(*category_params)

categories = [
    ('https://www.ndtv.com/india/page-', 'h2', 1),
    ('https://www.ndtv.com/latest/page-', 'h2', 8),
    ('https://www.ndtv.com/cities/page-', 'h2', 14),
    ('https://www.ndtv.com/education/page-', 'h2', 14),
    ('https://www.ndtv.com/trends', 'h3', 1),
    ('https://www.ndtv.com/offbeat/page-', 'h2', 14),
    ('https://www.ndtv.com/south/page-', 'h2', 14)
]

results = Parallel(n_jobs=32, verbose=100)(delayed(process_category)(category_params) for category_params in categories)
for category, data in zip(categories, results):
    print(f"{category[0]}:")
    for headline, link, news_text in data:
        print(headline)
        print(link)
        response = model.generate_content('summarise this news article in short but dont miss on anything:  '+ news_text, safety_settings=safety_settings)
        print(response.text)
        print()