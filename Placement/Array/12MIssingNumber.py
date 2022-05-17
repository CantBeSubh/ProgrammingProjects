#https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1#
#obsidian://open?vault=HolyCow&file=12%20Missing%20Element
def MissingNumber(array,n):
    s=0
    for i in range(1,n+1):
        s+=i
    for i in array:
        s-=i
    
    return s