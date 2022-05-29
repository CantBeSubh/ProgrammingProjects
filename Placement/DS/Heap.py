arr = [2,66,30,5,5,9,10]
n=len(arr)

def max_heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        max_heapify(arr,n,largest)
        
def min_heapify(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[largest]>arr[left]:
        largest=left
    if right<n and arr[largest]>arr[right]:
        largest=right
    
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        min_heapify(arr,n,largest)
    
        



for i in range(n//2-1,-1,-1):
    max_heapify(arr,n,i)

print(arr)