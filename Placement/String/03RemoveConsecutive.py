def solve(a,b):
    n=len(a)
    prev=a[0]
    res=[]
    count=1
    for i in a[1:]:
        if i==prev:
            count+=1
        else:
            if count==b:
                count=1
            else:
                res.append(prev*count)
                count=1
        prev=i
    if count<b:
        res.append(prev)
    return "".join(res)

print(solve('aaagccc',3))
