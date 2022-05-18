#https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
#obsidian://open?vault=HolyCow&file=Placement%2FArray%2FLevel%202%2F13%20Count%20pairs%20with%20given%20sum

def getPairsCount(self, arr, n, k):
    # code here
    count=0
    for i in range(n):
        if arr[i]<k:
            j=k-arr[i]
            for z in range(i+1,n):
                if arr[z]==j:
                    count+=1
    
    return count

# Better
class Solution:
    def getPairsCount(self, arr, n, sum):
        # code here

        m = dict()
 
        # Store counts of all elements in map m
        for i in range(n):
            if arr[i] in m.keys():
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
 
        twice_count = 0
 
        # Iterate through each element and increment
        # the count (Notice that every pair is
        # counted twice)
        for i in range(0, n):
            if (sum-arr[i]) in m.keys():
                twice_count += m[sum - arr[i]]
 
            # if (arr[i], arr[i]) pair satisfies the
            # condition, then we need to ensure that
            # the count is  decreased by one such
            # that the (arr[i], arr[i]) pair is not
            # considered
            if (sum - arr[i] == arr[i]):
                twice_count -= 1
 
        # return the half of twice_count
        return int(twice_count / 2)