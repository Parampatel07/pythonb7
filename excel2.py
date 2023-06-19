# Create a excel sheet with following pattern
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, 176 ... 3000
from openpyxl import Workbook
import time
wb = Workbook()
worksheet = wb.active
number = 1 
temp = 4
count = 1
cell_name = 'A'
cell_number =''
while number<3000:
     time.sleep(2)
     print(number)
     cell_number = cell_name + str(count)
     # print(cell_number) 
     worksheet[cell_number] = number
     number= number + temp
     temp +=3
     count = int(count)
     count+=1
# print(number)
# worksheet['A2'] = number
# number = number + temp
# temp +=3
# print(number)
# worksheet['A3']=number
# number = number + temp
# temp+=3
# print(number)
# worksheet['A4'] = number
wb.save("pattern.xlsx")