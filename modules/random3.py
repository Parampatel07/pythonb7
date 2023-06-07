import random
color = ['red','blue','green','yellow']
cars = ['ford gt40','gtr r34','toyota','rolls royes','mustang']
print(color)

answer = random.choice(color)
print(answer)

print(cars)
answer = random.choices(cars,k=3)
print(answer)

random.shuffle(cars)
print(cars)

answer = random.sample(cars,k=5)
print(answer)