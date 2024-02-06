import requests

client = requests.Session()

class News:
    def __init__(self, subject, title, text, link) -> None:
        self.subject = subject
        self.title = title
        self.text = text
        self.link = link
    