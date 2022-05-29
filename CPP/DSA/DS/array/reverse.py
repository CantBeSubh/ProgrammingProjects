from numpy import random
a=[]
size=int(input('Enter size: '))
for i in range(size):
    a.append(int(random.rand()*100))

b=a[::-1]
print(*a)
b=map(lambda x:x,b)
print(*b)