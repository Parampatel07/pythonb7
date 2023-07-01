#example of private variable in class 
class account:
     __balance = 0
     def __init__(self,name,id,balance):
          self.name = name
          self.id = id 
          self.__balance = balance
     
     def getInfo(self):
          print(f"Your name is {self.name} and your id number is {self.id} your balance is {self.__balance}")

     def change_balance(self,balance):
          self.__balance = balance

     
a1 = account("Param",99,10000000)
a1.getInfo()
a1.name = "Param Patel"
a1.getInfo()
# a1.__balance = 10000  
a1.change_balance(100)
a1.getInfo()
print(a1._account__balance)