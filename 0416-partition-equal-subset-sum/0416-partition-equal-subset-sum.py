class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        if sum(nums)%2 !=0 :
            return False
        def dp(i,summ):
            if i == len(nums):
                return summ == 0
            if (i, summ) not in memo:
                memo[(i,summ)] = dp(i+1, summ) or dp(i+1, summ-nums[i])
            return memo[(i,summ)]
        return dp(0,sum(nums)//2)