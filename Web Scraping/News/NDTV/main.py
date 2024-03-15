from bs4 import BeautifulSoup
import requests
from joblib import Parallel, delayed

def get_news_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    news_paragraphs = soup.find_all('p')[:2]
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
    ('https://www.ndtv.com/india/page-', 'h2', 14),
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
        print(news_text)
        print()