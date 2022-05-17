#https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
#obsidian://open?vault=HolyCow&file=Placement%2FArray%2FLevel%201%2F10%20Union%20of%20arrays

def doUnion(a,n,b,m):
    def findMe(a,i):
        try:
            a.index(i)
            return 1
        except:
            return 0
        
    if(n>m):
        count=n
        for i in b:
            count+=1 if findMe(a,i)==0 else 0
    
    return count

print(([1,2,3,4,5],5,[1,2,9],3))


def doUnion2(a,n,b,m):
    a=set(a)
    b=set(b)
    a=a.union(b)
    count=len(a)
    
    return count

print(doUnion2([1,2,3,4,5],5,[1,2,9],3))
