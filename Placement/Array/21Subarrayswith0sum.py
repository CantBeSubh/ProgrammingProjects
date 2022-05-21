def func(arr):
    m=list()
    s=0
    c=False
    m.append(s)
    for i in arr:
        s+=i
        if s in m:
            return True
        else:
            m.append(s)
    
    return False

print(func([4,2,0,1,6]))
    

            