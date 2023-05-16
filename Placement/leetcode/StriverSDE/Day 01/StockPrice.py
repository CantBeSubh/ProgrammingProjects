def soln(nums):
    mini = float("inf")
    res = 0
    for i in nums:
        if i < mini:
            mini = i
        res = max(res, i - mini)

    return res


print(soln([7, 1, 5, 3, 6, 4]))
