
# from bs4 import BeautifulSoup
# import requests


# India_News_Data = set()

# for x in range(1, 15):
#     r = requests.get(f'https://www.ndtv.com/india/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        

# Election_News = set()

# for x in range(1, 5):
#     r = requests.get(f'https://www.ndtv.com/elections/elections-news/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h3')
    
#     for h3_tag in News_Data:
#         headline = h3_tag.text.strip()
#         link = h3_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        
# Latest_News = set()

# for x in range(1, 9):
#     r = requests.get(f'https://www.ndtv.com/latest/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()



# #cities
# Cities = set()

# for x in range(1, 15):
#     r = requests.get(f'https://www.ndtv.com/cities/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        
# Education = set()


# for x in range(1, 15):
#     r = requests.get(f'https://www.ndtv.com/education/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        
# Trending = set()
# r = requests.get("https://www.ndtv.com/trends") #single page for trending news on website
# soup = BeautifulSoup(r.text, 'lxml')
    
# News_Data = soup.find_all('h3')
    
# for h3_tag in News_Data:
#         headline = h3_tag.text.strip()
#         link = h3_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        
# Offbeat = set()


# for x in range(1, 15):
#     r = requests.get(f'https://www.ndtv.com/offbeat/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        
# South = set()


# for x in range(1, 15):
#     r = requests.get(f'https://www.ndtv.com/south/page-{x}')
#     soup = BeautifulSoup(r.text, 'lxml')
    
#     News_Data = soup.find_all('h2')
    
#     for h2_tag in News_Data:
#         headline = h2_tag.text.strip()
#         link = h2_tag.a['href']
#         print(headline)
#         print(link)
#         print()
        


from bs4 import BeautifulSoup
import requests

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

India_News_Data = scrape_category('https://www.ndtv.com/india/page-', 'h2', 14)
Latest_News = scrape_category('https://www.ndtv.com/latest/page-', 'h2', 8)
Cities = scrape_category('https://www.ndtv.com/cities/page-', 'h2', 14)
Education = scrape_category('https://www.ndtv.com/education/page-', 'h2', 14)
Trending = scrape_category('https://www.ndtv.com/trends', 'h3', 1)
Offbeat = scrape_category('https://www.ndtv.com/offbeat/page-', 'h2', 14)
South = scrape_category('https://www.ndtv.com/south/page-', 'h2', 14)

for headline, link, news_text in India_News_Data:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()
    
for headline, link, news_text in Latest_News:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()

for headline, link, news_text in Cities:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()
    
for headline, link, news_text in Education:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()
    
for headline, link, news_text in Trending:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()
    
for headline, link, news_text in Offbeat:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()
    
for headline, link, news_text in South:
    print("India News")
    print(headline)
    print(link)
    print(news_text)
    print()