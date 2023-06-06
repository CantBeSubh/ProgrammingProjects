from ast import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        k = 0
        while i < n:
            if i == 0 or nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k
