a=[]
sum=0
size=int(input('Enter size: '))
for i in range(size):
    a.append(i+1)
    sum+=a[i]

print(*a,sep=' ')

print(sum)