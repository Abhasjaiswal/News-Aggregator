import streamlit as st
from bs4 import BeautifulSoup
import requests
from joblib import Parallel, delayed
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Function to scrape news text from NDTV
def get_news_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_paragraphs = soup.find_all('p')[:2]
    news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
    return news_text

# Function to scrape NDTV news
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

# Function to scrape NDTV category
def scrape_category(url_pattern, tag_name, pages):
    results = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url_pattern, tag_name, page_num) for page_num in range(1, pages + 1))
    news_data = set()
    for page_result in results:
        for item in page_result:
            news_data.add(item)
    return news_data

# Function to scrape headlines and links from Google News
def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_google_news(category_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless") 

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(category_url)
    time.sleep(5)
    scroll_down(driver, 2)
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')
    headlines = soup.find_all('a', class_='gPFEn')
    links = soup.find_all('a', class_='gPFEn')
    return headlines, links

# Streamlit app
st.title("News Aggregator")

source = st.selectbox("Select News Source", ["NDTV", "Google News"])

if source == "NDTV":
    category = st.selectbox("Select Category", ["India", "Latest", "Cities", "Education", "Trending", "Offbeat", "South"])
    
    if category == "Trending":
        news_data = scrape_category('https://www.ndtv.com/trends', 'h3', 1)
    else:
        url_pattern = f'https://www.ndtv.com/{category.lower()}/page-'
        pages = 14 if category != "Trending" else 1
        news_data = scrape_category(url_pattern, 'h2', pages)
elif source == "Google News":
    categories = {
        "India": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        "World": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
        "Business": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREYzTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
    }
    selected_category = st.selectbox("Select a category", list(categories.keys()))
    category_url = categories[selected_category]
    headlines, links = scrape_google_news(category_url)
    if headlines:
        news_data = [(headline.text, "https://news.google.com" + link['href'], "") for headline, link in zip(headlines, links)]
    else:
        news_data = []

if news_data:
    st.subheader("Latest News")
    for headline, link, news_text in news_data:
        st.markdown(f"<h2 style='color: white; font-weight: bold;'>{headline}</h2>", unsafe_allow_html=True)
        if news_text:
            st.markdown(f"<p style='color: white;'>{news_text}</p>", unsafe_allow_html=True)
        st.write('<a style="background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;" href="'+link+'" target="_blank">Read more</a>', unsafe_allow_html=True)
        st.write("---")
else:
    st.warning("No news found for the selected category/source.")
