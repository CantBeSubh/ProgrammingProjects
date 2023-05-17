def binarySearch(arr, t):
    l = 0
    h = len(arr)
    m = (l + h) // 2
    while l <= h:
        if t > arr[m]:
            l = m + 1
        elif t < arr[m]:
            h = m - 1
        else:
            return True
        m = (l + h) // 2
    return False


def soln(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    search = []
    for i in matrix:
        if i[0] <= target and i[n - 1] >= target:
            search = i
            break
    if len(search) == 0:
        return False
    return binarySearch(search, target)


# Consider 2D array to one huge 1D array
def best(matrix, target):
    lo = 0
    if not matrix:
        return False
    hi = (len(matrix) * len(matrix[0])) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
            return True
        if matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


print(soln([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
