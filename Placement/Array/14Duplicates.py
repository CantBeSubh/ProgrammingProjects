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


# print(duplicates([1,2,3,2,1],5))

def duplicates2(arr,n):
    res=[]
    for i in range(n):
        if arr[abs(arr[i])]<=0:
            if arr[abs(arr[i])] not in res:
                res.append(abs(arr[i]))
        else:
            arr[arr[i]]=-arr[arr[i]]
        
    return res

print(duplicates2([1,2,3,2,1],5))