import requests
from crawler import get_mehr_news, get_news_links
from save_in_excel import add_data_to_excel
import links


def get_and_save_news(topic: str, urls: list):
    for url in urls:
        text = get_mehr_news(url)
        add_data_to_excel(topic, text)



def run(agency: str):
    if agency == "mehr":
        sport_links =  get_news_links(links.mehr_links["sport"])
        political_links = get_news_links(links.mehr_links["political"])
        economy_links = get_news_links(links.mehr_links["economy"])
        art_links = get_news_links(links.mehr_links["art"])
    elif agency == "irna":
        sport_links =  get_news_links(links.irna_links["sport"])
        political_links = get_news_links(links.irna_links["political"])
        economy_links = get_news_links(links.irna_links["economy"])
        art_links = get_news_links(links.irna_links["art"])
    elif agency == "isna":
        sport_links =  get_news_links(links.isna_links["sport"])
        political_links = get_news_links(links.isna_links["political"])
        economy_links = get_news_links(links.isna_links["economy"])
        art_links = get_news_links(links.isna_links["art"])
    elif agency == "hamshahri":
        sport_links =  get_news_links(links.mehr_links["sport"])
        political_links = get_news_links(links.mehr_links["political"])
        economy_links = get_news_links(links.mehr_links["economy"])
        art_links = get_news_links(links.mehr_links["art"])
    
    get_and_save_news("sport", sport_links)
    get_and_save_news("political", political_links)
    get_and_save_news("economy", economy_links)
    get_and_save_news("art", art_links)
    
run("mehr")
