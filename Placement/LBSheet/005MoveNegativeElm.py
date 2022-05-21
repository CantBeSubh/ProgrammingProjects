def func1(arr):
    a,b=0,len(arr)-1
    while(True):
        while(a<len(arr) and arr[a]<0):
            a+=1
        while(b<len(arr) and arr[b]>=0):
            b-=1
        if a>b:
            break
        arr[a],arr[b]=arr[b],arr[a]
    
    return arr


#Clean version
def func2(arr):
    n=len(arr)
    j = 0
    for i in range(0, n) :
        if (arr[i] < 0) :
            arr[i],arr[j]=arr[j],arr[i]
            j = j + 1
    return arr


#Dutch color thing
def reArrange(arr):
    n=len(arr)
    low,high = 0, n - 1
    while(low<high):
        if(arr[low] < 0):
            low += 1
        elif(arr[high] > 0):
            high -= 1
        else:
            arr[low],arr[high] = arr[high],arr[low]

    return arr


print(func1([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print(func2([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
print(reArrange([-12, 11, -13, -5, 6, -7, 5, -3, -6]))
