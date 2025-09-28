class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i,tot):
            if i == len(nums):
                return 1 if tot == target else 0
            if (i,tot) not in memo:
                memo[(i,tot)] = dp(i+1, tot + nums[i]) + dp(i+1, tot -nums[i])
            return memo[(i,tot)]
        return dp(0,0)
        

