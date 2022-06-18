def calculateSpan(a):
    n=len(a)
    stack=[0]
    res=[1]
    for i in range(1,n):
        while(len(stack)>0 and a[stack[-1]]<a[i]):
            stack.pop()
        if len(stack)==0:
            res.append(i+1)
        else:
            res.append(i-stack[-1])
        stack.append(i) 
    return res

print(calculateSpan([100,80,60,70,60,75,85]))