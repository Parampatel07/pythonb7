# https://www.ndtv.com/fuel-prices
# [{'city':'Adilabad','petrol_price':'111.83 ₹/L','diseal':"99.84 ₹/L"}]
import requests
from bs4 import BeautifulSoup
count=0
data_formate = {'name':'','petrol_price':'','diseal_price':''}
final_data=[]
url = f'''https://www.ndtv.com/fuel-prices'''
html_content = requests.get(url).text
soup = BeautifulSoup(html_content,'html.parser')
table = soup.find_all('table',{'class':'font-16 color-blue'})
my_table = table[1]
td_list=my_table.find_all('td')
count=0
name_count=0
petrol_count=1
diseal_count=2
data_formate['name']=td_list[name_count].text 
data_formate['petrol_price']=td_list[petrol_count].text 
data_formate['diseal_price']=td_list[diseal_count].text
while count<((len(td_list)/3)-1):
     name_count+=3
     data_formate['name']=td_list[name_count].text 
     petrol_count+=3
     data_formate['petrol_price']=td_list[petrol_count].text 
     diseal_count+=3
     data_formate['diseal_price']=td_list[diseal_count].text
     print(data_formate)
     count+=1
print(final_data)