# import requests
# from bs4 import BeautifulSoup

# topic_urls = [
#     ('Peace and Security', 'https://news.un.org/en/news/topic/peace-and-security?page={}'),
#     ('Climate Change', 'https://news.un.org/en/news/topic/climate-change?page={}'),
#     ('Women', 'https://news.un.org/en/news/topic/women?page={}'),
#     ('Culture and Education', 'https://news.un.org/en/news/topic/culture-and-education?page={}'),
#     ('Economic Development', 'https://news.un.org/en/news/topic/economic-development?page={}'),
#     ('Human Rights', 'https://news.un.org/en/news/topic/human-rights?page={}'),
#     ('Law and Crime Prevention', 'https://news.un.org/en/news/topic/law-and-crime-prevention?page={}'),
#     ('SDGs', 'https://news.un.org/en/news/topic/sdgs?page={}'),
#     ('Humanitarian Aid', 'https://news.un.org/en/news/topic/humanitarian-aid?page={}'),
#     ('UN Affairs', 'https://news.un.org/en/news/topic/un-affairs?page={}'),
#     ('Health', 'https://news.un.org/en/news/topic/health?page={}'),
#     ('Migrants and Refugees', 'https://news.un.org/en/news/topic/migrants-and-refugees?page={}')
# ]

# for topic_name, topic_url in topic_urls:
#     print(f"Articles for {topic_name}:")
#     for page_num in range(0,2): #PAGE NUMBERS TO BE MODIFIED HERE (On the Website there are around 430 pages as the news is from 2001)
#         url = topic_url.format(page_num)
#         page = requests.get(url)
#         soup = BeautifulSoup(page.text, 'html.parser')

#         articles = soup.find_all('article', class_='node--type-news-story')  

#         for article in articles:
            
#             headline_tag = article.find('h2', class_='node__title')
#             if headline_tag:
#                 article_link = headline_tag.find('a', href=True)
#                 if article_link:
#                     base_url='https://news.un.org'
#                     href = article_link['href']
#                     headline = article_link.span.text.strip()
#                     print(f"Headline: {headline}")
#                     print(f"Href: {base_url+href}")

#             time_tag = article.find('time', class_='datetime')
#             if time_tag:
#                 time = time_tag.text.strip()
#                 print(f"Time: {time}")

#             news_text_tag = article.find('div', class_='field--name-field-news-story-lead')
#             if news_text_tag:
#                 news_text = news_text_tag.text.strip()
#                 print(f"News Text: {news_text}")

#             print("-------------------")

import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

topic_urls = [
    ('Peace and Security', 'https://news.un.org/en/news/topic/peace-and-security?page={}'),
#     ('Climate Change', 'https://news.un.org/en/news/topic/climate-change?page={}'),
#     ('Women', 'https://news.un.org/en/news/topic/women?page={}'),
#     ('Culture and Education', 'https://news.un.org/en/news/topic/culture-and-education?page={}'),
#     ('Economic Development', 'https://news.un.org/en/news/topic/economic-development?page={}'),
#     ('Human Rights', 'https://news.un.org/en/news/topic/human-rights?page={}'),
#     ('Law and Crime Prevention', 'https://news.un.org/en/news/topic/law-and-crime-prevention?page={}'),
#     ('SDGs', 'https://news.un.org/en/news/topic/sdgs?page={}'),
#     ('Humanitarian Aid', 'https://news.un.org/en/news/topic/humanitarian-aid?page={}'),
#     ('UN Affairs', 'https://news.un.org/en/news/topic/un-affairs?page={}'),
#     ('Health', 'https://news.un.org/en/news/topic/health?page={}'),
#     ('Migrants and Refugees', 'https://news.un.org/en/news/topic/migrants-and-refugees?page={}')
# 
]

for topic_name, topic_url in topic_urls:
    print(f"Articles for {topic_name}:")
    for page_num in range(0, 2):
        url = topic_url.format(page_num)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        articles = soup.find_all('article', class_='node--type-news-story')  

        for article in articles:
            headline_tag = article.find('h2', class_='node__title')
            if headline_tag:
                article_link = headline_tag.find('a', href=True)
                if article_link:
                    base_url = 'https://news.un.org'
                    href = article_link['href']
                    article_url = base_url + href
                    headline = headline_tag.text.strip()
                    print(f"Headline: {headline}")
                    print(f"URL: {article_url}")

                    article_page = requests.get(article_url)
                    article_soup = BeautifulSoup(article_page.text, 'html.parser')

                    news_text_tags = article_soup.find_all('p')
                    news_text = "\n".join([tag.get_text(strip=True) for tag in news_text_tags])

                    response = model.generate_content('summarise this news article: ' + news_text)
                    summary = response.text.strip()
                    print("Summary:")
                    print(summary)

                    print("-------------------")
