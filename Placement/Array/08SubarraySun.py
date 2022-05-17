#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
#obsidian://open?vault=HolyCow&file=Placement%2FArray%2FLevel%201%2F08%20Sum%20Of%20Subarray

def subSum(a,s):
    S=0
    i=0
    n=len(a)
    while(S<s and i<n):
        S+=a[i]
        i+=1
    j=0
    while(i<n):
        S=S-a[j]
        j+=1
        if(S==s):
            return [j+1,i]
        S+=a[i]
        i+=1
        if(S==s):
            return [j+1,i]
    
    return [-1]

print(subSum([135,101,170,125,79,159,163,65,106,146,82,28,162,92,196,143,28,37,192,5,103,154,93,183,22,117,119,96,48,127,172,139,70,113,68,100,36,95,104,12,123,134],468))


# An efficient program 
# to print subarray
# with sum as given sum 

# Returns true if the 
# there is a subarray 
# of arr[] with sum
# equal to 'sum' 
# otherwise returns 
# false. Also, prints 
# the result.
def subArraySum(arr, n, sum_):
    
    # Initialize curr_sum as
    # value of first element
    # and starting point as 0 
    curr_sum = arr[0]
    start = 0

    # Add elements one by 
    # one to curr_sum and 
    # if the curr_sum exceeds 
    # the sum, then remove 
    # starting element 
    i = 1
    while i <= n:
        
        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum_ and start < i-1:
        
            curr_sum = curr_sum - arr[start]
            start += 1
            
        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum_:
            print ("Sum found between indexes")
            print ("% d and % d"%(start, i-1))
            return 1

        # Add this element 
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here, 
    # then no subarray
    print ("No subarray found")
    return 0

# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
