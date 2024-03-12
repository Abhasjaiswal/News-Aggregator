import streamlit as st
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

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

st.title("News Aggregator")

categories = {
    "India": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
    "World": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
    "Business": "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNREYzTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen",
}

selected_category = st.selectbox("Select a category", list(categories.keys()))

category_url = categories[selected_category]

headlines, links = scrape_google_news(category_url)

if headlines:
    st.subheader(f"Headlines for {selected_category} Category:")
    for headline, link in zip(headlines, links):
        st.write("Headline:", headline.text)
        st.write("Link:", "https://news.google.com" + link['href'])
        st.write("---")
else:
    st.warning("No headlines found for the selected category.")
