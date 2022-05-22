def minDiff(a,k):
    n=len(a)
    # m,M=min(a),max(a)
    # return M-m-2*k
    m=list()
    t=[]
    for i in a:
        m.append([i-k,i+k])
    for i,j in m:
        if i*j>0:
            t.append(min(i,j))
        else:
            t.append(max(i,j))
    M,d=max(t),min(t)
    return m,t

def better(a,k):
    a.sort()




print(minDiff([2,6,3,4,7,2,10,3,2,1],5))

def getMinDiff(arr, n, k):
    arr.sort()
    ans = arr[n - 1] - arr[0]  # Maximum possible height difference
 
    tempmin = arr[0]
    tempmax = arr[n - 1]
 
    for i in range(1, n):
        tempmin = min(arr[0] + k, arr[i] - k) 
         
        # Minimum element when we
        # add k to whole array
        # Maximum element when we
        tempmax = max(arr[i - 1] + k, arr[n - 1] - k)
         
        # subtract k from whole array
        ans = min(ans, tempmax - tempmin)
 
    return ans
 
# Driver Code Starts
k = 3
n = 4
arr = [1, 2, 15, 10]
ans = getMinDiff(arr, n, k)
print(ans)