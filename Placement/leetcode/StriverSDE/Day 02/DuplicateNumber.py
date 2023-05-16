def soln(nums):
    n = len(nums)
    arr = [0] * n
    for i in range(n):
        if arr[nums[i]] == 1:
            return nums[i]
        else:
            arr[nums[i]] = 1


def soln2(nums):
    n = len(nums)
    for i in range(n):
        if nums[abs(nums[i]) - 1] < 0:
            return abs(nums[i])
        else:
            nums[abs(nums[i]) - 1] *= -1
