def soln(nums):
    ind = -1
    n = len(nums)
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break
    if ind == -1:
        return nums[::-1]

    for i in range(n - 1, ind - 1, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    nums[ind + 1 :] = nums[ind + 1 :][::-1]
    return nums


print(soln([1, 2, 3]))
