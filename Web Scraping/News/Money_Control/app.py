# import requests
# from bs4 import BeautifulSoup
# import streamlit as st
# from joblib import Parallel, delayed

# base_urls = {
#     'business': "https://www.moneycontrol.com/news/business/page-{}/",
#     'markets': "https://www.moneycontrol.com/news/business/markets/page-{}/",
#     'stocks': "https://www.moneycontrol.com/news/business/stocks/page-{}/",
#     'economy': "https://www.moneycontrol.com/news/business/economy/page-{}/",
#     'companies': "https://www.moneycontrol.com/news/business/companies/page-{}/",
#     'trends': "https://www.moneycontrol.com/news/trends/page-{}/",
#     'ipo': "https://www.moneycontrol.com/news/business/ipo/page-{}/",
# }

# def scrape_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     headlines = soup.find_all('h2')
#     page_data = []
#     for h2_tag in headlines:
#         a_tag = h2_tag.find('a', href=True)
#         if a_tag:
#             headline = a_tag.get_text()
#             link_href = a_tag['href']
#             next_p_tag = h2_tag.find_next_sibling('p')
#             short_news = next_p_tag.get_text() if next_p_tag else None
#             page_data.append({'headline': headline, 'link': link_href, 'short_news': short_news})
#     return page_data

# def scrape_category_parallel(category, start_page=1, end_page=31):
#     base_url = base_urls.get(category)
#     if not base_url:
#         st.error("Invalid category.")
#         return []

#     urls = [base_url.format(page_number) for page_number in range(start_page, end_page + 1)]
#     scraped_data = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url) for url in urls)
#     return [item for sublist in scraped_data for item in sublist]

# def display_news(category_data):
#     for item in category_data:
#         st.markdown(f"<h2 style='color: white; font-weight: bold;'>{item['headline']}</h2>", unsafe_allow_html=True)
#         st.markdown(f"<p style='color: white;'>{item['short_news']}</p>", unsafe_allow_html=True)
#         st.write(f"<a style='background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;' href='{item['link']}' target='_blank'>Read more</a>", unsafe_allow_html=True)
#         st.write("---")

# def main():
#     st.markdown(
#         """
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Nasalization&display=swap');
#         .title {
#             color: white;
#             font-size: 36px;
#             font-family: 'Nasalization', sans-serif;
#             font-weight: bold;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .subheader {
#             color: white;
#             font-size: 18px;
#             font-family: 'Nasalization', sans-serif;
#             text-align: center;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown('<p class="title">News Aggregator</p>', unsafe_allow_html=True)
#     st.markdown('<p class="subheader">A project by Abhas Jaiswal</p>', unsafe_allow_html=True)

#     category = st.selectbox("Select Category", list(base_urls.keys()))

#     news_data = scrape_category_parallel(category)
#     if news_data:
#         display_news(news_data)
#     else:
#         st.error(f"No data available for {category.capitalize()} category.")

# if __name__ == "__main__":
#     main()

import requests
from bs4 import BeautifulSoup
import streamlit as st
from joblib import Parallel, delayed
import base64
def set_bg_hack(main_bg):
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('pxfuel.png')
base_urls = {
    'business': "https://www.moneycontrol.com/news/business/page-{}/",
    'markets': "https://www.moneycontrol.com/news/business/markets/page-{}/",
    'stocks': "https://www.moneycontrol.com/news/business/stocks/page-{}/",
    'economy': "https://www.moneycontrol.com/news/business/economy/page-{}/",
    'companies': "https://www.moneycontrol.com/news/business/companies/page-{}/",
    'trends': "https://www.moneycontrol.com/news/trends/page-{}/",
    'ipo': "https://www.moneycontrol.com/news/business/ipo/page-{}/",
}

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h2')
    page_data = []
    for h2_tag in headlines:
        a_tag = h2_tag.find('a', href=True)
        if a_tag:
            headline = a_tag.get_text()
            link_href = a_tag['href']
            next_p_tag = h2_tag.find_next_sibling('p')
            short_news = next_p_tag.get_text() if next_p_tag else None
            page_data.append({'headline': headline, 'link': link_href, 'short_news': short_news})
    return page_data

def scrape_category_parallel(category, start_page=1, end_page=31):
    base_url = base_urls.get(category)
    if not base_url:
        st.error("Invalid category.")
        return []

    urls = [base_url.format(page_number) for page_number in range(start_page, end_page + 1)]
    scraped_data = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url) for url in urls)
    return [item for sublist in scraped_data for item in sublist]

def display_news(category_data):
    for item in category_data:
        st.markdown(f"<h2 style='color: white; font-weight: bold;'>{item['headline']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{item['short_news']}</p>", unsafe_allow_html=True)
        st.write(f"<a style='background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;' href='{item['link']}' target='_blank'>Read more</a>", unsafe_allow_html=True)
        st.write("---")

def search_news(news_data, query):
    if query:
        return [item for item in news_data if query.lower() in item['headline'].lower() or (item['short_news'] and query.lower() in item['short_news'].lower())]
    else:
        return news_data

def main():
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


    st.markdown('<p class="title" style="font-weight: bold; font-size: 46px; font-family: \'Nasalization\', sans-serif;">News Aggregator</p>', unsafe_allow_html=True)

    st.markdown('<p class="subheader" style="font-weight: bold; font-size: 24px;">A project by Abhas Jaiswal</p>', unsafe_allow_html=True)

    category = st.selectbox("Select Category", list(base_urls.keys()))

    news_data = scrape_category_parallel(category)
    
    query = st.text_input("Search news by keyword:")
    filtered_news = search_news(news_data, query)

    if filtered_news:
        display_news(filtered_news)
    else:
        st.error("No matching news found.")

if __name__ == "__main__":
    main()
