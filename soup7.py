import requests
from bs4 import BeautifulSoup
data_formate = {'name':'',"position":'',"Pace":"","Shoot":"","Pass":"","Dribble":"","Defending":"","Physic":""}
final_data=[]
url = f'''https://www.futhead.com/23/players/'''
html_content = requests.get(url).text
soup = BeautifulSoup(html_content,'html.parser')
html_list = soup.find_all('li',{'class':'list-group-item list-group-table-row player-group-item dark-hover'})
count = 0 
while count<48:
     single_list = html_list[count]
     name = single_list.find('span',{'class':'player-name'}).text
     position = single_list.find('strong').text
     pac = single_list.find_all('span',{'class':'value'})
     data_formate = {"name":name,"position":position,"Pace":pac[0].text,"Shoot":pac[1].text,"Pass":pac[2].text,"Dribble":pac[3].text,"Defending":pac[4].text,"Physic":pac[5].text}
     final_data.append(data_formate)
     count+=1
print(final_data)