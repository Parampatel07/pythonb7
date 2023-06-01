# What is the value of x after executing the following code snippet?
x = 10
def foo():
    global x
    x += 5

foo()
print(x)