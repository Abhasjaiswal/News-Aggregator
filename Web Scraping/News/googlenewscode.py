from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'
page=requests.get(url)
soup=BeautifulSoup(page.text,'lxml')

test=soup.find_all('a',class_="gPFEn")
headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

# Printing headlines and links
for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()
    
    
#INDIA NEWS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()


#WORLD NEWS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()


#BUSINESS NEWS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()
    
#TECHNOLOGY NEWS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()

# Entertainment news

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()
    
#Sports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()

#Science

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()

#Health

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def scroll_down(driver, scroll_pause_time):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen'

driver = webdriver.Chrome()

driver.get(url)

time.sleep(5)

scroll_down(driver, 2)

page_source = driver.page_source

driver.quit()

soup = BeautifulSoup(page_source, 'html.parser')

headlines = soup.find_all('a', class_='gPFEn')
links = soup.find_all('a', class_='gPFEn')

for headline, link in zip(headlines, links):
    print("Headline:", headline.text)
    print("Link:", "https://news.google.com" + link['href'])
    print()
