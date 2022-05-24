def func(a):
    res=[]
    n=len(a)
    a.sort(key=lambda x:x[0])
    i=0
    while(i<n):
        if (i<n-1) and (a[i][1]>=a[i+1][0]):
            x=a[i+1][1] if a[i+1][1]>a[i][1] else a[i][1]
            temp=[a[i][0],x]
            res.append(temp)
            i+=1
        else:
            res.append(a[i])
        i+=1
    
    return res

print(func([[1,3],[2,6],[8,10],[15,18]]))