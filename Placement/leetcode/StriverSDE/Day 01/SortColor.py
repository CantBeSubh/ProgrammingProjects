def soln(nums):
    # n = len(nums)
    # o = 0
    # t = n - 1
    # while o < n and nums[o] == 0:
    #     o += 1

    # while t > 0 and nums[t] == 2:
    #     t -= 1
    # i = o
    # while i < n and nums[i] == 1:
    #     i += 1

    # while i <= t:
    #     if nums[i] == 2:
    #         nums[i], nums[t] = nums[t], nums[i]
    #         while nums[t] == 2:
    #             t -= 1
    #     if nums[i] == 0:
    #         nums[i], nums[o] = nums[o], nums[i]
    #         while nums[o] == 0:
    #             o += 1
    #     i += 1
    n = len(nums)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(soln([2, 0, 1]))
