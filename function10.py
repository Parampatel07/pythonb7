# Write a programe to findout price from weight  from given fix value input weight.
# 1000gm = Rs500

def calculatePrice(rate,weight):
     price = rate * weight / 1000
     print("price is ",price)

rate = float(input("Enter rate of product "))
weight = float(input("Enter wegiht of product in grams "))
calculatePrice(rate, weight)