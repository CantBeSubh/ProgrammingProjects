m=dict()
def soln(a,b):
    if b==a:
        return 1
    if a%3!=0 or b>a:
        return 0
    if (a,b) in m.keys():
        return m[(a,b)]
    ans=max(soln(a//3,b),soln(2*a//3,b))
    m[(a,b)]=ans
    return ans
    

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if(soln(a,b)==1):print("YES")
    else: print("NO")