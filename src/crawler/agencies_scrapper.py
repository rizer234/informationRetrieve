import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def parse_page_for_news_links(response):
    domain = response.url[:response.url.find(response.request.path_url)]
    soup = BeautifulSoup(response.content, "html.parser")
    
    if "isna" in domain:
        news_tags = soup.find_all("li", class_="text")
        news_tags += soup.find_all("li", class_="coverage")
    else:
        news_tags = soup.find_all("li", class_="news")

    links = []
    for tag in news_tags:
        # all of href links that direct to single news in a class tags
        a_tags = tag.find_all("a")
        for a_tag in a_tags:
            if a_tag.get("href", False):
                links.append(domain + '/' + a_tag["href"])
                break
    return links
        

def parse_isna_pages_using_selenium_for_news_links(url: str):
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)
    page_html = driver.page_source
    driver.close()
    soup = BeautifulSoup(page_html, "html.parser")
    news_tags = soup.find_all("li", class_="news")
    links = []
    for tag in news_tags:
        # all of href links that direct to single news in a class tags
        a_tags = tag.find_all("a")
        for a_tag in a_tags:
            if a_tag.get("href", False):
                links.append("https://www.isna.ir/" + a_tag["href"])
                break
    return links


