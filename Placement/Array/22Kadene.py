def kadene(arr,n):
    s=0
    m=arr[0]
    for i in arr:
        s+=i
        m=max(m,s)
        if s<0:
            s=0
    return m

print(kadene([1, 2, 3, -2, 5],5))