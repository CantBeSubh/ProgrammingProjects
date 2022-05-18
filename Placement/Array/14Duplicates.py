def duplicates(arr, n): 
    # code here
    res=list()
    m=dict()
    print(type(m))
    for i in range(n):
        if arr[i] in m.keys():
            m[arr[i]]+=1
        else:
            m[arr[i]]=1
    
    for a,b in m.items():
        if b>1:
            res.append(a)
    
    return res


print(duplicates([1,2,3,2,1],5))