# News Aggregator Project

## Problem Statement
In today's fast-paced world, staying updated with the latest news from various sources can be a time-consuming task. With the abundance of information available on the internet, users often find it challenging to efficiently gather news articles from their preferred sources while filtering out irrelevant content. This inefficiency can lead to information overload and difficulty in accessing timely and relevant news updates. 

To address this issue, the development of a Python-based news aggregator with web scraping techniques is proposed. The goal of this project is to create a user-friendly application that automates the process of fetching news articles from a diverse range of sources, allowing users to customize their news consumption experience. 

## Introduction

This project is a Python-based news aggregator that fetches news articles from various sources on the internet using web scraping techniques. It utilizes libraries like Selenium, Beautiful Soup, and Requests to scrape data from different websites and present it in a structured format.

## Features

- **Website Scraping**: The project scrapes news articles from predefined websites using techniques like  HTTP requests and browser automation.
- **Source Selection**: Users can select their preferred news sources from a list of supported websites.
- **Article Summarization**: The application provides a summarized version of each news article to give users a quick overview.
- **Category Filtering**: Users can filter news articles based on predefined categories such as politics, technology, sports, etc.
- **Customization**: The project allows for customization of settings such as the number of articles to fetch, the frequency of updates, and the appearance of the user interface.

## Dependencies

- **Selenium**: For browser automation and dynamic content scraping.
- **Beautiful Soup**: For parsing HTML and extracting data from web pages.
- **Requests**: For making HTTP requests and fetching web content.
- **Google GenAI API**: For generating summaries of news articles.
- **Other standard libraries**: Used for various functionalities, Used Streamlit for GUI Development.

## Installation

1. Clone the project repository from GitHub or download the source code files.
2. Install the required dependencies using pip:
4. Ensure you have a compatible web driver installed (e.g., ChromeDriver for Selenium).

## Additional News Sources Integration

We have integrated additional news sources into the project to provide users with a wider selection of news content. 

## News Summarization with Google GenAI API

The project utilizes the Google GenAI API for generating summaries of news articles. This API provides advanced natural language processing capabilities to summarize textual content accurately and efficiently.

To generate a summary of a news article, the application sends the article's text to the Google GenAI API, which processes the text and returns a concise summary. The project incorporates safety settings to ensure that the generated summaries adhere to predefined thresholds for harmful content categories such as hate speech, harassment, and sexually explicit content.

By leveraging the Google GenAI API, the project enhances the news consumption experience by providing users with summarized versions of news articles, enabling quick comprehension and efficient browsing of multiple news stories.

## Conclusion

The News Aggregator Project offers a convenient solution for users to access and consume news articles from diverse online sources. By leveraging web scraping techniques, integrating additional news sources, and incorporating the Google GenAI API for news summarization, the project aims to enhance the news consumption experience for users. With further improvements and enhancements, the project has the potential to become a valuable tool for staying informed in today's fast-paced world.
