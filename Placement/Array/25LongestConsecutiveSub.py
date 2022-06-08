def func(arr):
    n=len(arr)
    ma=max(arr)
    res=[0 for i in range(ma+1)]
    print(res)
    for i in arr:
        res[i]=1
    
    c=0
    i=0
    m=0
    print(res)
    while(i<len(res)):
        if res[i]==0:
            m=max(c,m)
            c=0
        else:
            c+=1
        i+=1

    return max(m,c)


print(func([8,9,1,2,3,1]))