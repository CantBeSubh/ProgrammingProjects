def solve(A):
    vowel='aeiouAEIOU'
    p=[]
    l=len(A)
    for i in range(l):
        if A[i] in vowel:
            p.append(i)
    res=0
    res=l*len(p)
    for j in p:
        res-=j
    
    return res%10003

print(solve('ABEC'))