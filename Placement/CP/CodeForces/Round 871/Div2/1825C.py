t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[int(x) for x in input().split()]
    seat=[0]*m
    l=m-1
    r=0
    for j in range(n):
        x=arr[j]
        if x==-1:
            if l!=0:
                seat[l-1]=1
                l=l-1
        elif x==-1:
            if r!=m-1:
                seat[r]=1
                r+=1
        else:
            if seat[x]!=1:
                seat[x]=1
                if x<l:
                    l=x
                if x>r:
                    r=x
    print(seat.count(1))
