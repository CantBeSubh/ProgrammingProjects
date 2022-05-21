import sys
def func(arr):
    m=sys.maxsize
    M=0
    for i in arr:
        M=i if M<i else M
        m=i if m>i else m
    
    return (m,M)

print(func([1,2,3,4,5]))