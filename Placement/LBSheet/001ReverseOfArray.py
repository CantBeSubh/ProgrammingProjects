def func(arr):
    s=0
    e=len(arr)-1
    while(s<e):
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1
    return arr

print(func([1,2,3,4,5]))