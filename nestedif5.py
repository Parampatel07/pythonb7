# 16) Write a Python program to calculate income tax, gross income, net income from monthly income given by user 

# yearly income     tax rate
# <3,00,000         5%  

# >=3,00,000
# <5,00,000         10%  

# >=5,00,000
# <8,00,000         20%

# >=8,00,000        30%  

monthly_income = int(input("Enter your monthly income "))
yearly_income = monthly_income * 12
print("your yearly income is ",yearly_income)
tax_rate = 0
if yearly_income < 300000:
     tax_rate = 5 
elif yearly_income >= 300000 and yearly_income < 500000:
     tax_rate = 10
elif yearly_income >=500000 and yearly_income < 800000:
     tax_rate = 20
elif yearly_income>800000:
     tax_rate = 30
income_tax = yearly_income * tax_rate / 100
print("your income tax is ",income_tax)
net_income = yearly_income - income_tax
print("your net income is ",net_income)