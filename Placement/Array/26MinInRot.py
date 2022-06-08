def func(arr,n):
    if n==1:
        return arr[0]
    if n==2:
        if arr[0]<arr[1]:
            return arr[0]
        return arr[1]
    mid=n//2
    p=arr[mid]
    if arr[mid+1]<p:
        l=arr[0:mid]
        x=func(l,len(l))
        return min(p,x)
    else:
        r=arr[mid+1:]
        x=func(r,len(r))
        return min(p,x)
    

def fi(arr, low, high):
  
    while (low < high):
        mid = low + (high - low) // 2;
        
        if (arr[mid] == arr[high]):
            high -= 1;
        elif (arr[mid] > arr[high]):
            low = mid + 1;
        else:
            high = mid;
    return arr[high];
    
print(func([10, 20, 30, 40, 50, 5, 7],7))