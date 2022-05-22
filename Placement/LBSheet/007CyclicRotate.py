def rotate(a):
    l=a[-1]
    for i in range(len(a)-2,-1,-1):
        a[i+1]=a[i]
    a[0]=l
    return a

print(rotate([1,2,3,4,5]))