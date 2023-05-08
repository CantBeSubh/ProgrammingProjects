t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    arr=[int(x) for x in input().split()]
    if len(set(arr))==1:print(0)
    else:
        arr.sort()
        maxi=arr[-1]
        mini1=arr[0]
        mini2=arr[1]
        del1=maxi-mini1
        del2=maxi-mini2
        if n>m:
            res=(del1*(n-1)*m)+(del2*(m-1))
        else:
            res=(del1*(m-1)*n)+(del2*(n-1))
        print(res)