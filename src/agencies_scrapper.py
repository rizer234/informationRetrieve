from bs4 import BeautifulSoup

def ham_irna_mehr_get_news_links(response: str):
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
        

def isna_get_news_links(html_text: str):
    soup = BeautifulSoup(html_text, "html.parser")
    news_tags = soup.find_all("li", class_="text")
    news_tags += soup.find_all("li", class_="coverage")
    links = []
    for tag in news_tags:
        a_tags = tag.find_all("a")
    for a_tag in a_tags:
        if a_tag.get("href", False):
                links.append(a_tag["href"])
                break
    return links

