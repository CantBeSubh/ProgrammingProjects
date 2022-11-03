def sortedSquares(nums):
    arr = [x**2 for x in nums]
    arr.sort()
    return arr


def sortedSquares2(nums):
    n = len(nums)
    i, j = 0, n - 1
    arr = [0] * n
    for p in range(j, -1, -1):
        if abs(nums[i]) > abs(nums[j]):
            arr[p] = nums[i] ** 2
            i += 1
        else:
            arr[p] = nums[j] ** 2
            j -= 1
    return arr


print(sortedSquares2([-4, -1, 0, 3, 10]))
