#https://practice.geeksforgeeks.org/problems/peak-element/
#obsidian://open?vault=HolyCow&file=Placement%2FArray%2F01%20Peak%20Element

#O(N)
def peakElement(self,arr, n):
    if n==1:
        return 0
    for i in range(n):
        if i==0:
            if arr[i]>arr[i+1]:
                return i
        elif i==n-1:
            if arr[i]>arr[i-1]:
                return i
        else:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i


#O(LogN)

# A python3 program to find a peak 
#  element using divide and conquer

# A binary search based function 
# that returns index of a peak element
def findPeakUtil(arr, low, high, n):
    
     # Find index of middle element
     # (low + high)/2 
     mid = low + (high - low)/2 
     mid = int(mid)
    
    # Compare middle element with its 
    # neighbours (if neighbours exist)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid


    # If middle element is not peak and 
    # its left neighbour is greater 
    # than it, then left half must 
    # have a peak element
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1), n)

    # If middle element is not peak and
    # its right neighbour is greater
    # than it, then right half must 
    # have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive 
# function findPeakUtil()
def findPeak(arr, n):

    return findPeakUtil(arr, 0, n - 1, n)


# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
    
# This code is contributed by 
# Smitha Dinesh Semwal