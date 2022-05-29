def sort_array(arr):
    b=sorted(arr)
    a=[]
    a=[x for x in b if x%2!=0]
    for i in range(0,len(arr)):
        if arr[i]%2!=0:
            arr[i]=a[0]
            a.pop(0)
    return arr

print(sort_array([5, 8, 6, 3, 4]))

print([x for x in [5, 8, 6, 3, 4] if x%2==0])