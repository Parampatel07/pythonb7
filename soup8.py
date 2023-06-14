# https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-gujarat.cms
# https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-agra.cms
# https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-ahmedabad.cms
# https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-bangalore.cms
import requests
from bs4 import BeautifulSoup
city = input("Enter name of city ")
url = f'''https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-{city}.cms'''
print(url)
html_content = requests.get(url).text
print(html_content)
soup = BeautifulSoup(html_content,'html.parser')
price = soup.find('span',{'class':"fuel-price"}).text
print(price)