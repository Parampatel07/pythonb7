# https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-gujarat.cms

import requests
from bs4  import BeautifulSoup

data_formate = {'name':'',"price":""}

final_data=[]
url = f"https://economictimes.indiatimes.com/wealth/fuelprices/fuel-petrol,citystate-gujarat.cms"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content,'html.parser')
html_content = soup.find_all('tr')
html_price = soup.find_all('td')
#   print(html_price)
# print(hml_content)
count = 0
price_count=1
print(html_price[3].text)
print(html_price[1].text)
while count < 51:
    single_list = html_price[count] 
    count+=3
    single_list2 = html_price[price_count]   
    price_count+=3
    
    name = single_list.text
    price = single_list2.text
    # print(name) 
    # count+=1 
    # print(price)
    data_formate = {"name":name,"Price":price}
    final_data.append(data_formate)
print(final_data)