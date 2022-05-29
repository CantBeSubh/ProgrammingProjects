from numpy import random
a=[]
size=int(input('Enter size: '))
for i in range(size):
    a.append(int(random.rand()*100))

print(*a)
print(*a[::-1])