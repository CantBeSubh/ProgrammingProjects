t=int(input())
for i in range(t):
    s=int(input())
    a=[]
    a=[int(x) for x in input().split(' ')]
    
    a=a[::-1]
    print(a)

t=int(input())
for i in range(t):
    s=int(input())
    a=[int(x) if x else -1 for x in input().split(' ')]
    if a[-1]==-1:
        a.pop()
    a=a[::-1]
    print(*a,sep=' ')