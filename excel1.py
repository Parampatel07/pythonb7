from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
wb = Workbook()
ws = wb.active
data = "97"
url = f'''https://vclock.com/time/'''
html_content = requests.get(url).text
print(html_content)
soup = BeautifulSoup(html_content,'html.parser')
formate_soup = soup.prettify()
print(soup.find('span',{'id':'lbl-time'}).text)
ws['A1'] = soup.find('span',{'id':'lbl-time'}).text
wb.save("sample.xlsx")