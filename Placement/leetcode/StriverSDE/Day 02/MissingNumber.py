def soln(nums):
    n = len(nums)
    n = n * (n + 1) // 2
    return n - sum(nums)
