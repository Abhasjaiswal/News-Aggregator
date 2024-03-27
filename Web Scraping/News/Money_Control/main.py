import requests
from bs4 import BeautifulSoup

base_urls = {
    'business': "https://www.moneycontrol.com/news/business/page-{}/",
    'markets': "https://www.moneycontrol.com/news/business/markets/page-{}/",
    'stocks': "https://www.moneycontrol.com/news/business/stocks/page-{}/",
    'economy': "https://www.moneycontrol.com/news/business/economy/page-{}/",
    'companies': "https://www.moneycontrol.com/news/business/companies/page-{}/",
    'trends': "https://www.moneycontrol.com/news/trends/page-{}/",
    'ipo': "https://www.moneycontrol.com/news/business/ipo/page-{}/",
}

def scrape_category(category, start_page=1, end_page=15):
    all_headlines_news = []
    base_url = base_urls.get(category)
    if not base_url:
        print("Invalid category.")
        return

    for page_number in range(start_page, end_page + 1):
        url = base_url.format(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        h2_tags = soup.find_all('h2')
        for h2_tag in h2_tags:
            a_tag = h2_tag.find('a', href=True)
            if a_tag:
                headline = a_tag.get_text()
                link_href = a_tag['href']
                next_p_tag = h2_tag.find_next_sibling('p')
                short_news = next_p_tag.get_text() if next_p_tag else None
                all_headlines_news.append({'headline': headline, 'link': link_href, 'short_news': short_news})

    print(f"Category: {category.capitalize()}")
    for item in all_headlines_news:
        print("Headline:", item['headline'])
        print("Link:", item['link'])
        print("Short News:", item['short_news'] if item['short_news'] else "N/A")
        print()

categories = ['business', 'markets', 'stocks', 'economy', 'companies', 'trends', 'ipo']
for category in categories:
    for start_page in range(1, 31, 15):
        end_page = min(start_page + 14, 30)
        scrape_category(category, start_page, end_page)
