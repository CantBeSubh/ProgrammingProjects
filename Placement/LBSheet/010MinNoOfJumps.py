def func(arr):
    n=len(arr)
    jumps=0
    steps=arr[0]
    maxrange=0
    pos=0
    jumpTo=0
    while(pos+steps<n):
        if steps==0:
            steps=maxrange
            pos=jumpTo
            jumpTo=0
            jumps+=1
        if pos+steps<n:
            if(arr[pos+steps]>maxrange):
                maxrange=arr[pos+steps]
                jumpTo=pos+steps
            steps-=1
    
    return jumps

print(func([1, 4, 3, 2, 6, 7]))