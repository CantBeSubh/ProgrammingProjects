def func(a):
    res=[]
    n=len(a)
    a.sort(key=lambda x:x[0])
    for i in a:
        if(len(res)==0 or res[-1][1]<i[0]):
            res.append(i)
        else:
            res[-1][1]=max(res[-1][1],i[1])
    return res

print(func([[1,3],[2,6],[8,10],[15,18]]))