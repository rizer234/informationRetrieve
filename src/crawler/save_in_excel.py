import pandas as pd
from model import News
from openpyxl import load_workbook


def save_file_to_excel(subject: str, title: str, text: str, link: str, path: str = 'ir.xlsx'):
    arr = [subject, title, text, link]
    df = pd.DataFrame([arr], columns=['subject', 'title', 'text', 'link'])
    df.to_excel(path, sheet_name='sheet1', index=False)

def add_data_to_excel(news: News, path: str = 'ir.xlsx'):
    workbook = load_workbook(path)
    worksheet = workbook['sheet1']
    worksheet.append({"A": news.subject, "B": news.title, "C": news.text[0:1000], "D": news.link})
    workbook.save(path)
    # workbook.close()

# save_file_to_excel("test", "test title", "this is a test file", "test://testl.com")