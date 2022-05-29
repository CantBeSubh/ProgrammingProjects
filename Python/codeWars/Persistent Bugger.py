def persistence(n):
    a=str(n)
    count=int(0)
    while(len(a)>1):
        p=int(1)
        for i in a:
            p*=int(i)
        count+=1
        a=str(p)
    return count