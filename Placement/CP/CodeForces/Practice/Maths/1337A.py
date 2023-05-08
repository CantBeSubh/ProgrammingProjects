t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())

    x=max(a,b)
    y=max(b,c)
    z=min(c,d)
    print(x,y,z,sep=" ")