def soln(nums):
    s = 0
    res = -float("inf")
    for i in nums:
        s += i
        if res < s:
            res = s
        if s < 0:
            s = 0
    return res


print(soln([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
