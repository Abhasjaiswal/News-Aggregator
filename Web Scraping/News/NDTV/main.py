from bs4 import BeautifulSoup
import requests


India_News_Data = set()

for x in range(1, 15):
    r = requests.get(f'https://www.ndtv.com/india/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()
        

Election_News = set()

for x in range(1, 5):
    r = requests.get(f'https://www.ndtv.com/elections/elections-news/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h3')
    
    for h3_tag in News_Data:
        headline = h3_tag.text.strip()
        link = h3_tag.a['href']
        print(headline)
        print(link)
        print()
        
Latest_News = set()

for x in range(1, 9):
    r = requests.get(f'https://www.ndtv.com/latest/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()



#cities
Cities = set()

for x in range(1, 15):
    r = requests.get(f'https://www.ndtv.com/cities/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()
        
Education = set()


for x in range(1, 15):
    r = requests.get(f'https://www.ndtv.com/education/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()
        
Trending = set()
r = requests.get("https://www.ndtv.com/trends") #single page for trending news on website
soup = BeautifulSoup(r.text, 'lxml')
    
News_Data = soup.find_all('h3')
    
for h3_tag in News_Data:
        headline = h3_tag.text.strip()
        link = h3_tag.a['href']
        print(headline)
        print(link)
        print()
        
Offbeat = set()


for x in range(1, 15):
    r = requests.get(f'https://www.ndtv.com/offbeat/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()
        
South = set()


for x in range(1, 15):
    r = requests.get(f'https://www.ndtv.com/south/page-{x}')
    soup = BeautifulSoup(r.text, 'lxml')
    
    News_Data = soup.find_all('h2')
    
    for h2_tag in News_Data:
        headline = h2_tag.text.strip()
        link = h2_tag.a['href']
        print(headline)
        print(link)
        print()
        
