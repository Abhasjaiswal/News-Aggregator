import google.generativeai as genai
import streamlit as st
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import requests
import base64
from joblib import Parallel, delayed
from about_me import display_about_me
import os
from dotenv import load_dotenv
load_dotenv()
from google.generativeai.types import HarmCategory, HarmBlockThreshold

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def set_bg_hack(main_bg):
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

def streamlit_menu():
    selected = option_menu(
        menu_title="Main Menu",  
        options=["Home","Project Documentation","About Me","Contact"],  
        default_index=0,  
    )
    return selected

base_urls = {
    'Business': "https://www.moneycontrol.com/news/business/page-{}/",
    'Markets': "https://www.moneycontrol.com/news/business/markets/page-{}/",
    'Stocks': "https://www.moneycontrol.com/news/business/stocks/page-{}/",
    'Economy': "https://www.moneycontrol.com/news/business/economy/page-{}/",
    'Companies': "https://www.moneycontrol.com/news/business/companies/page-{}/",
    'Trends': "https://www.moneycontrol.com/news/trends/page-{}/",
    'IPO': "https://www.moneycontrol.com/news/business/ipo/page-{}/",
}

def scrape_page(url):
    try:
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
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
                    article_text = scrape_article(link_href)
                    page_data.append({'headline': headline, 'link': link_href, 'short_news': short_news, 'article_text': article_text})
            return page_data
        else:
            print(f"Failed to scrape page: {url}. Status code: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error scraping page: {url}. Exception: {str(e)}")
        return []

@st.cache_data
def scrape_category_parallel(category, start_page=1, end_page=10):
    base_url = base_urls.get(category)
    if not base_url:
        st.error("Invalid category.")
        return []

    urls = [base_url.format(page_number) for page_number in range(start_page, end_page + 1)]
    scraped_data = Parallel(n_jobs=32, verbose=100)(delayed(scrape_page)(url) for url in urls)
    return [item for sublist in scraped_data for item in sublist]


def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    article_text = ' '.join([p.get_text() for p in paragraphs])
    return article_text

# def display_news(category_data):
#     for idx, item in enumerate(category_data):
#         article_container = st.empty()  # Create an empty placeholder for the article content

#         with article_container:  # Fill the placeholder with the article content
#             st.markdown(f"<h2 style='color: white; font-weight: bold;'>{item['headline']}</h2>", unsafe_allow_html=True)
#             st.markdown(f"<p style='color: white;'>{item['short_news']}</p>", unsafe_allow_html=True)

#             # Generate a unique key for the button using the index
#             button_key = f"summary_button_{idx}"

#             # Add a button next to each article
#             if st.button("Generate Summary", key=button_key):
#                 with st.spinner("Generating Summary..."):  # Display a spinner while generating the summary
#                     response = model.generate_content('summarise this news article in short but dont miss on anything: ' + item['article_text'], safety_settings=safety_settings)
                
#                 # Update the article container with the generated summary
#                 st.markdown("<div style='color: white; padding: 10px; border-radius: 5px;'>"
#                             "<h3 style='color: white;'>Summary</h3>"
#                             f"<p>{response.text}</p>"
#                             "</div>", unsafe_allow_html=True)

#             st.write(f"<a style='background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;' href='{item['link']}' target='_blank'>Read more</a>", unsafe_allow_html=True)
#             st.write("---")


def search_news(news_data, query):
    if query:
        return [item for item in news_data if query.lower() in item['headline'].lower() or (item['short_news'] and query.lower() in item['short_news'].lower())]
    else:
        return news_data

def main():
    set_bg_hack('pxfuel.png')
    selected_option = streamlit_menu()
    
    if selected_option == "Home":
        selected_category = st.selectbox("Select Category", list(base_urls.keys()))
        with st.spinner("Scraping news data..."):
            news_data = scrape_category_parallel(selected_category)
    elif selected_option == "About Me":
        display_about_me()
    elif selected_option == "Contact":
       from contact_us import display_contact
       display_contact()
    elif selected_option == "Project Documentation":
        st.write("Project Documentation")
    else:
        st.error("Invalid option selected.")

    if selected_option == "Home":
        query = st.text_input("Search news by keyword:")
        filtered_news = search_news(news_data, query)

        if filtered_news:
            for idx, item in enumerate(filtered_news):
                st.markdown(f"<h2 style='color: white; font-weight: bold;'>{item['headline']}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: white;'>{item['short_news']}</p>", unsafe_allow_html=True)

                button_key = f"summary_button_{idx}"

                if st.button("Generate Summary", key=button_key):
                    with st.spinner("Generating Summary..."):
                        print("Generating summary for:", item['headline'])  

                        response = model.generate_content('summarise this news article in short but dont miss on anything: ' + item['article_text'], safety_settings=safety_settings)
                    st.markdown("<div style='color: white; padding: 10px; border-radius: 5px;'>"
                                "<h3 style='color: white;'>Summary</h3>"
                                f"<p>{response.text}</p>"
                                "</div>", unsafe_allow_html=True)

                st.write(f"<a style='background-color: #2C3E50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;' href='{item['link']}' target='_blank'>Read more</a>", unsafe_allow_html=True)
                st.write("---")
        else:
            st.error("No matching news found.")

if __name__ == "__main__":
    main()
