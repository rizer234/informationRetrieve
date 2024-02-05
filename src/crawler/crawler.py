import requests
from bs4 import BeautifulSoup
from agencies_scrapper import parse_page_for_news_links

client = requests.Session()

class Crawler:
    def __init__(self) -> None:
        pass

def get_news_links(url: str):
    links = []
    for i in range(1, 15):
        pagination_cursor = url.find("&pi=")
        url_list = list(url)
        url_list[pagination_cursor + 4] = str(i)
        url = ''.join(url_list)
        try:
            response = client.get(url)
        except:
            continue
        links += parse_page_for_news_links(response)
    return links


def get_mehr_news(url: str):
    try:
        response = client.get(url)
    except:
        print ("get error")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    body_tag = soup.find("div", class_="item-body")
    text_tag = body_tag.find("div", class_="item-text")
    text = text_tag.get_text()
    return text


    

