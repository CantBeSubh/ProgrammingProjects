def solve(a):
    arr=a.split(' ')
    print(arr)
    l=''
    for i in arr[::-1]:
        if i!='':
            l=l+' '+i
    return l.strip()
print(solve('Reverse   Me'))