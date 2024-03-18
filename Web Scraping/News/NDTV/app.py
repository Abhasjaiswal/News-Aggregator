# import streamlit as st
# from bs4 import BeautifulSoup
# import requests

# def get_news_text(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'lxml')
#     news_paragraphs = soup.find_all('p')[:2]
#     news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
#     return news_text

# def scrape_and_summarize(category_url):
#     news_data = []
#     for page_num in range(1, 6):  
#         page_url = f"{category_url}/page-{page_num}"
#         r = requests.get(page_url)
#         soup = BeautifulSoup(r.text, 'lxml')
        
#         for h2_tag in soup.find_all('h2'):
#             headline = h2_tag.text.strip()
#             link = h2_tag.a['href']
#             news_text = get_news_text(link)
#             news_data.append({"headline": headline, "news_text": news_text, "link": link})
#     return news_data

# st.title("News Aggregator")

# categories = [
#     "India",
#     "Elections",
#     "Latest",
#     "Cities",
#     "Education",
#     "Trends",
#     "Offbeat",
#     "South"
# ]

# selected_category = st.selectbox("Select a category:", categories)

# category_urls = {
#     "India": "https://www.ndtv.com/india/",
#     "Elections": "https://www.ndtv.com/elections/elections-news/",
#     "Latest": "https://www.ndtv.com/latest/",
#     "Cities": "https://www.ndtv.com/cities/",
#     "Education": "https://www.ndtv.com/education/",
#     "Trends": "https://www.ndtv.com/trends",
#     "Offbeat": "https://www.ndtv.com/offbeat/",
#     "South": "https://www.ndtv.com/south/"
# }

# if selected_category:
#     st.write(f"Scraping news for {selected_category} category...")
#     news_data = scrape_and_summarize(category_urls[selected_category])
#     for news_item in news_data:
#         st.subheader(news_item["headline"])
#         st.write("News Text:")
#         st.write(news_item["news_text"])
#         st.write("Link:", news_item["link"])
#         st.write("---")

import streamlit as st
from bs4 import BeautifulSoup
import requests
from joblib import Parallel, delayed
def get_news_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    news_paragraphs = soup.find_all('p')[:2]
    news_text = '\n'.join([p.text.strip() for p in reversed(news_paragraphs)])
    return news_text

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

def scrape_category(url_pattern, tag_name, pages):
    results = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url_pattern, tag_name, page_num) for page_num in range(1, pages + 1))
    news_data = set()
    for page_result in results:
        for item in page_result:
            news_data.add(item)
    return news_data

# def display_news(category_data):
#     for headline, link, news_text in category_data:
#         st.write("**Headline:**", headline)
#         st.write("**News Text:**", news_text)
#         # st.markdown(f"[Read more]({link})")
#         st.write('<a style="background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;" href="'+link+'" target="_blank">Read more</a>', unsafe_allow_html=True)
#         st.write("---")

def display_news(category_data):
    for headline, link, news_text in category_data:
        st.markdown(f"<h2 style='color: white; font-weight: bold;'>{headline}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{news_text}</p>", unsafe_allow_html=True)
        st.write('<a style="background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;" href="'+link+'" target="_blank">Read more</a>', unsafe_allow_html=True)
        st.write("---")

def main():
     import streamlit as st

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
    news_data = scrape_category('https://www.ndtv.com/india/page-', 'h2', 14)
elif category == "Latest":
    news_data = scrape_category('https://www.ndtv.com/latest/page-', 'h2', 8)
elif category == "Cities":
    news_data = scrape_category('https://www.ndtv.com/cities/page-', 'h2', 14)
elif category == "Education":
    news_data = scrape_category('https://www.ndtv.com/education/page-', 'h2', 14)
elif category == "Trending":
    news_data = scrape_category('https://www.ndtv.com/trends', 'h3', 1)
elif category == "Offbeat":
    news_data = scrape_category('https://www.ndtv.com/offbeat/page-', 'h2', 14)
elif category == "South":
    news_data = scrape_category('https://www.ndtv.com/south/page-', 'h2', 14)
else:
    st.error("Invalid category selected.")

display_news(news_data)

if __name__ == "__main__":
    main()

