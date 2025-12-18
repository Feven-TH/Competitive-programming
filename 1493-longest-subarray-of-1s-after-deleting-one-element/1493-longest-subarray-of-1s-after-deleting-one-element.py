class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zeros, res = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
           
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, i - l)
        return res
