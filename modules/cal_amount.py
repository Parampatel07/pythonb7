amount = 2000 #global amount

def addAmount():
     global amount
     amount = amount + 10000
     print("inside the function ",amount)

addAmount()
print("outside the function ",amount)