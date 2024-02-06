from bs4 import BeautifulSoup
from agencies_scrapper import parse_page_for_news_links
from model import client, News


def get_hamshahri_news_links(url: str):
    links = []
    for i in range(1, 6):
        pagination_cursor = url.find("pi=")
        url_list = list(url)
        url_list[pagination_cursor + 3] = str(i)
        url = ''.join(url_list)
        try:
            response = client.get(url)
        except Exception as e:
            print ("error in get ", url)
            print (e, '\n\n')
            continue
        links += parse_page_for_news_links(response)
    return links


def get_hamshahri_news(subject: str, url: str):
    try:
        response = client.get(url)
    except:
        print ("get error")
        return
    
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1", class_="title").text
    body_tag = soup.find("div", class_="item-body")
    text_tag = body_tag.find("div", class_="item-text")
    text = text_tag.get_text()
    news = News(subject, title, text, url)
    return news        

