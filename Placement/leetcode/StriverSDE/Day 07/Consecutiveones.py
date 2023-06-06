from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        res = -1
        cnt = 0
        while i < len(nums):
            if nums[i] == 0:
                res = max(res, cnt)
                cnt = 0
            else:
                cnt += 1
            i += 1
        res = max(res, cnt)
        return res
