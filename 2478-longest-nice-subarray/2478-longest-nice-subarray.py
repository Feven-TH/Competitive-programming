class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, maxx ,temp= 0 ,0 ,0
        for i in range(len(nums)):
            while (temp & nums[i]).bit_count() != 0:
                temp ^= nums[left]
                left += 1
            temp |= nums[i]
            maxx = max(maxx, i -left +1)
        return maxx
