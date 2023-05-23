#Example of function with input and without return value 

def printSymbol(symbol,size):
     print(symbol*size)

symbol = input("Enter symbol you want to print ")
size = int(input("Enter size of line "))
printSymbol(symbol,size)