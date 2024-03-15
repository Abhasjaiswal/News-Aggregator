from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

def extract_source_name(url):
    match = re.search(r'\/\/(?:www\.)?([A-Za-z0-9\-]+)\.', url)
    if match:
        return match.group(1).replace("-", " ").title()
    return "Unknown"

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

chrome_options = Options()
chrome_options.add_argument("--headless")

url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
time.sleep(5)
scroll_down(driver, 2)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    redirected_link = "https://news.google.com" + link['href']
    driver.get(redirected_link)
    redirected_page_source = driver.page_source
    redirected_soup = BeautifulSoup(redirected_page_source, 'html.parser')
    source_name = extract_source_name(driver.current_url)
    print("Headline:", headline.text)
    print("Link:", redirected_link)
    print("Source Name:", source_name)
    print()

driver.quit()
