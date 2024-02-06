from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model import client, News


driver = webdriver.Firefox()


def get_irna_news_links(url: str):
    links = []
    for i in range(1, 5):
        pagination_cursor = url.find("pi=")
        url_list = list(url)
        url_list[pagination_cursor + 3] = str(i)
        url = ''.join(url_list)
        driver.get(url)
        try:
            main_body_tag = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'mainbody')))
            soup = BeautifulSoup(driver.page_source, "html.parser")
        except TimeoutError:
            print ("Loading took too much time!")
        
        news_tags = soup.find_all("li", class_="news")
        for tag in news_tags:
            # all of href links that direct to single news in a class tags
            a_tags = tag.find_all("a")
            for a_tag in a_tags:
                if a_tag.get("href", False):
                    links.append('https://www.irna.ir' + a_tag["href"])
                    break
    return links


def get_irna_news(subject: str, url: str) -> News:
    driver.get(url)
    try:
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, 'item')))
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except TimeoutError:
        print ("Loading took too much time!")
    body_tag = soup.find("div", class_="item-body")
    title = soup.find("h1", class_="title").text
    text_tag = body_tag.find("div", class_="item-text")
    text = text_tag.get_text()
    news = News(subject, title, text, url)
    return news


