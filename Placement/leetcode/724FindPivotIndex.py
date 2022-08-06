def solve(nums):
    if len(nums)==1:
        return 0

    lsum,rsum=0,0
    for i in range(len(nums)):
        for j in range(i): lsum+=nums[j]
        for j in range(i+1,len(nums)): rsum+=nums[j]
        if lsum==rsum: return i
        else: lsum,rsum=0,0
    
    return -1

def solve2(nums):
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            return i
        leftsum += x
    return -1

print(solve([2,1,-1]))
print(solve2([2,1,-1]))