from bs4 import BeautifulSoup
import requests

url = f'''https://vclock.com/time/'''
html_content = requests.get(url).text
print(html_content)
soup = BeautifulSoup(html_content,'html.parser')
formate_soup = soup.prettify()
print(soup.find('span',{'id':'lbl-time'}).text)
