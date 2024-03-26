from bs4 import BeautifulSoup
import requests
import pandas as pd
from joblib import Parallel, delayed
import time  # Import the time module

def extract_anime_info(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    divs = soup.find_all('div', class_='spaceit_pad')
    anime_info = {}

    for div in divs:
        span = div.find('span', class_='dark_text')
        if span:
            label = span.get_text(strip=True)
            value = div.get_text(strip=True, separator=' ')[len(label) + 1:].strip()
            # Fix Genres and Themes
            if label == 'Genres:':
                value = ', '.join([genre.strip() for genre in value.split(',')])
            elif label == 'Themes:':
                value = ', '.join([theme.strip() for theme in value.split(',')])
            anime_info[label[:-1]] = value  # Remove the trailing colon

    return anime_info

def scrape_anime_info(title, url):
    anime_info = extract_anime_info(url)
    anime_info['Title'] = title
    return anime_info

product_links = []

for x in range(4, 6):  # Modify the number of pages here 
    r = requests.get(f'https://myanimelist.net/anime/genre/1/Action?page={x}')
    soup = BeautifulSoup(r.text, 'html.parser')
    anime_links = soup.find_all('a', class_='link-title')

    for link in anime_links:
        title = link.text
        url = link['href']
        product_links.append((title, url))
        
    time.sleep(1)  # Sleep for 1 second between each page request


anime_data = Parallel(n_jobs=32, verbose=100)(delayed(scrape_anime_info)(title, url) for title, url in product_links)

df = pd.DataFrame(anime_data)

columns_order = ['Title', 'Synonyms', 'Japanese', 'English', 'Type', 'Episodes', 'Status', 'Aired', 
                 'Premiered', 'Broadcast', 'Producers', 'Licensors', 'Studios', 'Source', 'Genres', 
                 'Themes', 'Demographic', 'Duration', 'Rating', 'Score', 'Ranked', 'Popularity', 
                 'Members', 'Favorites']

df = df.reindex(columns=columns_order)
print(df)

df.to_csv('anime2.csv')
