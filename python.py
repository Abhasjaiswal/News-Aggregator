from bs4 import BeautifulSoup
import requests
import pandas as pd 

base_url = 'https://books.toscrape.com/catalogue/'

product_links = set()

for x in range(1,10):
    r = requests.get(f'https://books.toscrape.com/catalogue/page-{x}.html')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Extract product_list for this page
    product_list=soup.find_all('article',class_='product_pod')
    
    # Extract links and add to product_links
    for item in product_list:
        for link in item.find_all('a', href=True):
            product_links.add(base_url + link['href'])

product_links = list(product_links)
print(product_links)

test_link='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

for link in product_links:
    r=requests.get(link)
    soup=BeautifulSoup(r.text,'lxml')
    name=soup.find('h1').text.strip()
    availability=soup.find('p',class_='instock availability').text.strip()
    price=soup.find('p').text.strip('Â')
    rating = soup.find('p', class_='star-rating')['class'][1] 

    Book={'name':name,'availablity':availability,'pirce':price,'rating':rating}

print(Book)
