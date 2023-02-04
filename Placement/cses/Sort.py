def Sort(arr,n):
    if n==len(arr):return Sort(arr,n-2)
    if n==-1: return arr
    for i in range(n,len(arr)-1):
        if arr[i]>arr[i+1]: arr[i],arr[i+1]=arr[i+1],arr[i]
        else: break
    return Sort(arr,n-1)

arr=[1,3,5,4,2]
print(Sort(arr,len(arr)))