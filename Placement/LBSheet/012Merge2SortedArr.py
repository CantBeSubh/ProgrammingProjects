def func(a,b):
    n=len(a)
    m=len(b)
    i,j=0,0
    while(j<m):
        if b[j]>a[n-1]:
            break
        while(i<n):
            if a[i]>b[j]:
                a[i],b[j]=b[j],a[i]
            i+=1
        i=0
        j+=1
    b.sort()
    return (a,b)

def func2(a,b):
    n=len(a)
    m=len(b)
    a=a[::-1]
    i=0
    while(i<min(n,m) and a[i]>b[i]):
        a[i],b[i]=b[i],a[i]
        i+=1
    a.sort()
    b.sort()
    return (a,b)

print(func([1, 3, 5, 7],[0, 2, 6, 8, 9]))
print(func2([1, 3, 5, 7],[0, 2, 6, 8, 9]))