t=int(input())
for i in range(t):
    n=int(input())
    s=input().split()
    i=0
    j=0
    res=0
    while(i<n and s[i]=="1"):
        i+=1
    while(i<n and j<n):
        if(s[j]=="0"):
            j+=1
        else:
            res=max(res,j-i)
            i=j
            while(i<n and s[i]=="1"):
                i+=1
            j=i
    res=max(res,j-i)
    print(res)