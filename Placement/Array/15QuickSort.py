#DnC QuickSort

def QuickSort(arr):
    n=len(arr)
    if n==1:
        return arr
    elif n==2:
        if arr[1]<arr[0]:
            arr[1],arr[0]=arr[0],arr[1]
        return arr
    else:
        p=arr[0]
        i=1
        j=n-1
        while(True):
            while(arr[i]<p):
                i+=1
            while(arr[j]>p):
                j-=1
            if(j<i):
                arr[j],arr[0]=arr[0],arr[j]
                l=QuickSort(arr[0:j])
                r=QuickSort(arr[j+1:])
                l.append(p)
                res=l
                res.extend(r)
                return res
            arr[j],arr[i]=arr[i],arr[j]


print(QuickSort([4,1,3,9,7]))            