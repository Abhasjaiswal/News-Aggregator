import streamlit as st
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch_news_text(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            page_content = await response.text()
            soup = BeautifulSoup(page_content, 'html.parser')
            news_paragraphs = soup.find_all('p')[:2]
            news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
            return news_text
        else:
            return None

async def scrape_page(session, url_pattern, tag_name, page_num):
    async with session.get(f'{url_pattern}{page_num}') as response:
        if response.status == 200:
            page_content = await response.text()
            soup = BeautifulSoup(page_content, 'html.parser')
            news_items = soup.find_all(tag_name)
            results = []
            for item in news_items:
                headline = item.text.strip()
                link = item.a['href']
                news_text = await fetch_news_text(session, link)
                if news_text is not None:
                    results.append((headline, link, news_text))
            return results
        else:
            return []

async def scrape_category(url_pattern, tag_name, pages):
    async with aiohttp.ClientSession() as session:
        tasks = [scrape_page(session, url_pattern, tag_name, page_num) for page_num in range(1, pages + 1)]
        results = await asyncio.gather(*tasks)
        news_data = set()
        for page_result in results:
            for item in page_result:
                news_data.add(item)
        return news_data

def display_news(category_data):
    for headline, link, news_text in category_data:
        st.markdown(f"<h2 style='color: white; font-weight: bold;'>{headline}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{news_text}</p>", unsafe_allow_html=True)
        st.write('<a style="background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;" href="'+link+'" target="_blank">Read more</a>', unsafe_allow_html=True)
        st.write("---")

async def main():
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

    if category == "India":
        news_data = await scrape_category('https://www.ndtv.com/india/page-', 'h2', 14)
    elif category == "Latest":
        news_data = await scrape_category('https://www.ndtv.com/latest/page-', 'h2', 8)
    elif category == "Cities":
        news_data = await scrape_category('https://www.ndtv.com/cities/page-', 'h2', 14)
    elif category == "Education":
        news_data = await scrape_category('https://www.ndtv.com/education/page-', 'h2', 14)
    elif category == "Trending":
        news_data = await scrape_category('https://www.ndtv.com/trends', 'h3', 1)
    elif category == "Offbeat":
        news_data = await scrape_category('https://www.ndtv.com/offbeat/page-', 'h2', 14)
    elif category == "South":
        news_data = await scrape_category('https://www.ndtv.com/south/page-', 'h2', 14)
    else:
        st.error("Invalid category selected.")

    display_news(news_data)

if __name__ == "__main__":
    asyncio.run(main())
