#https://practice.geeksforgeeks.org/problems/count-subarrays-with-equal-number-of-1s-and-0s-1587115620/1

#O(N^2)
def func(arr):
    l=len(arr)
    res=[]
    
    for i in range(l):
        z,o=0,0
        if arr[i]==0:
            z+=1
        else:
            o+=1
        for j in range(i+1,l):
            if arr[j]==0:
                z+=1
            else:
                o+=1
            if z==o:
                res.append([i,j])
    
    return res

#O(N)

def func2(arr):
    m=dict()
    s,c=0,0
    m[s]=1
    for i in arr:
        if i==1:
            s+=1
        else:
            s-=1
        if s in m.keys():
            c+=m[s]
            m[s]+=1
        else:
            m[s]=1
    
    return c
        

print(func([1,0,0,1,0,1,1]))
print(func2([1,0,0,1,0,1,1]))

