import streamlit as st
from bs4 import BeautifulSoup
import requests
from joblib import Parallel, delayed

def get_news_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_paragraphs = soup.find_all('p')[:2]
    news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
    return news_text

def scrape_page(url_pattern, tag_name, page_num):
    r = requests.get(f'{url_pattern}{page_num}')
    soup = BeautifulSoup(r.text, 'html.parser')
    news_items = soup.find_all(tag_name)
    results = []
    for item in news_items:
        headline = item.text.strip()
        link = item.a['href']
        news_text = get_news_text(link)
        results.append((headline, link, news_text))
    return results

def scrape_category(url_pattern, tag_name, pages):
    results = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url_pattern, tag_name, page_num) for page_num in range(1, pages + 1))
    news_data = [item for page_result in results for item in page_result]
    return news_data

def display_news(category_data):
    for headline, link, news_text in category_data:
        st.markdown(f"<h2 style='color: white; font-weight: bold;'>{headline}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{news_text}</p>", unsafe_allow_html=True)
        st.write(f"[Read more]({link})", unsafe_allow_html=True)
        st.write("---")

def main():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Nasalization&display=swap');
        .title {
            color: white;
            font-size: 36px;
            font-family: 'Nasalization', sans-serif;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            color: white;
            font-size: 18px;
            font-family: 'Nasalization', sans-serif;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<p class="title">News Aggregator</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">A project by Abhas Jaiswal</p>', unsafe_allow_html=True)

    category = st.selectbox("Select Category", ["India", "Latest", "Cities", "Education", "Trending", "Offbeat", "South"])

    category_urls = {
        "India": 'https://www.ndtv.com/india/page-',
        "Latest": 'https://www.ndtv.com/latest/page-',
        "Cities": 'https://www.ndtv.com/cities/page-',
        "Education": 'https://www.ndtv.com/education/page-',
        "Trending": 'https://www.ndtv.com/trends',
        "Offbeat": 'https://www.ndtv.com/offbeat/page-',
        "South": 'https://www.ndtv.com/south/page-'
    }

    if category in category_urls:
        news_data = scrape_category(category_urls[category], 'h2', 14 if category != "Trending" else 1)
        display_news(news_data)
    else:
        st.error("Invalid category selected.")

if __name__ == "__main__":
    main()
