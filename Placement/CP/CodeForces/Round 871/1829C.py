t=int(input())
for i in range(t):
    n=int(input())
    m=dict()
    arr01=[]
    arr10=[]
    arr11=[]
    for i in range(n):
        temp=input().split()
        k,v=int(temp[0]),temp[1]
        if v=='11':
            arr11.append(k)
        elif v=='10':
            arr10.append(k)
        elif v=='01':
            arr01.append(k)
    arr01.sort()
    arr10.sort()
    arr11.sort()
    a,b,c=len(arr01),len(arr10),len(arr11)
    if c==0 and (a==0 or b==0):
        print(-1)
    elif c==0:
        print(arr01[0]+arr10[0])
    elif a==0 or b==0:
        print(arr11[0])
    else:
        x,y,z=arr01[0],arr10[0],arr11[0]
        if(x+y<z):
            print(x+y)
        else:
            print(z)
