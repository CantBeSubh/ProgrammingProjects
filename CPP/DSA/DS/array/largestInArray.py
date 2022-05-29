from numpy import random


a=[]
M=0
pos=0
size=int(input('Enter size: '))
for i in range(size):
    a.append(int(random.rand()*10))
for i in range(size):
    if M<a[i]:
        M=a[i]
        pos=i
    
print(*a)
print(M,pos,sep=' ')