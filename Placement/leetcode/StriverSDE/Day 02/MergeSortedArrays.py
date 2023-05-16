def soln(nums1, m, nums2, n):
    left = m - 1
    right = 0
    nums1 = nums1[:m]
    while left >= 0 and right < n:
        if nums1[left] > nums2[right]:
            nums1[left], nums2[right] = nums2[right], nums1[left]
            left -= 1
            right += 1
        else:
            break
    nums1.sort()
    nums2.sort()
    nums1.extend(nums2)
    return nums1


print(soln([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(soln([1], 1, [], 0))
print(soln([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3))
