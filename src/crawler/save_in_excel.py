import pandas as pd
from openpyxl import load_workbook


def save_file_to_excel(subject: str, content: str, path: str = 'ir.xlsx'):
    arr = [subject, content]
    df = pd.DataFrame([arr], columns=['subject', 'content'])
    df.to_excel(path, sheet_name='sheet1')

def add_data_to_excel(subject: str, content: str, path: str = 'ir.xlsx'):
    workbook = load_workbook(path)
    worksheet = workbook['sheet1']
    worksheet.append({"B": subject, "C": content})
    workbook.save(path)

