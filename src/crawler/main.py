import concurrent.futures as con
from save_in_excel import add_data_to_excel
from scrappers import hamshahri_scrapper, irna_scrapper, isna_scrapper, mehr_scrapper
import links


def get_and_save(topic: str, links: list, scrapper):
    for link in links:
        news = scrapper(topic, link)
        add_data_to_excel(news)


def run(agency: str):
    if agency == "mehr":
        
        sport_links =  mehr_scrapper.get_mehr_news_links(links.mehr_links["sport"])
        get_and_save("sport", sport_links, mehr_scrapper.get_mehr_news)

        political_links = mehr_scrapper.get_mehr_news_links(links.mehr_links["political"])
        get_and_save("political", political_links, mehr_scrapper.get_mehr_news)
        
        economy_links = mehr_scrapper.get_mehr_news_links(links.mehr_links["economy"])
        get_and_save("economy", economy_links, mehr_scrapper.get_mehr_news)

        art_links = mehr_scrapper.get_mehr_news_links(links.mehr_links["art"])
        get_and_save("art", art_links, mehr_scrapper.get_mehr_news)

    elif agency == "irna":

        sport_links =  irna_scrapper.get_irna_news_links(links.irna_links["sport"])
        get_and_save("sport", sport_links, irna_scrapper.get_irna_news)

        political_links = irna_scrapper.get_irna_news_links(links.irna_links["political"])
        get_and_save("political", political_links, irna_scrapper.get_irna_news)

        economy_links = irna_scrapper.get_irna_news_links(links.irna_links["economy"])
        get_and_save("economy", economy_links, irna_scrapper.get_irna_news)

        art_links = irna_scrapper.get_irna_news_links(links.irna_links["art"])
        get_and_save("art", art_links, irna_scrapper.get_irna_news)

    elif agency == "isna":

        sport_links =  isna_scrapper.get_isna_news_links(links.isna_links["sport"])
        get_and_save("sport", sport_links, isna_scrapper.get_isna_news)    

        political_links = isna_scrapper.get_isna_news_links(links.isna_links["political"])
        get_and_save("political", political_links, isna_scrapper.get_isna_news)    
        
        economy_links = isna_scrapper.get_isna_news_links(links.isna_links["economy"])
        get_and_save("economy", economy_links, isna_scrapper.get_isna_news)    
        
        art_links = isna_scrapper.get_isna_news_links(links.isna_links["art"])
        get_and_save("art", art_links, isna_scrapper.get_isna_news)
    
    elif agency == "hamshahri":

        sport_links =  hamshahri_scrapper.get_hamshahri_news_links(links.hamshahri_links["sport"])
        get_and_save("sport", sport_links, hamshahri_scrapper.get_hamshahri_news)
        
        political_links = hamshahri_scrapper.get_hamshahri_news_links(links.hamshahri_links["political"])
        get_and_save("political", political_links, hamshahri_scrapper.get_hamshahri_news)
        
        economy_links = hamshahri_scrapper.get_hamshahri_news_links(links.hamshahri_links["economy"])
        get_and_save("economy", economy_links, hamshahri_scrapper.get_hamshahri_news)
        
        art_links = hamshahri_scrapper.get_hamshahri_news_links(links.hamshahri_links["art"])
        get_and_save("art", art_links, hamshahri_scrapper.get_hamshahri_news)
    
    
run("irna")
