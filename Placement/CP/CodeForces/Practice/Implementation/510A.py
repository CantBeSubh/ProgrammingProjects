n,m=map(int,input().split())

arr=[]
for i in range(n):
    if i%4==1:
        t=["."]*(m-1)
        t.append("#")
        print(*t,sep="")
    elif i%4==3:
        t=['#']
        t.extend(["."]*(m-1))
        print(*t,sep="")
    else:
        t= ['#']*m
        print(*t,sep="")
