class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1]*len(nums)
        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] == 1:
                for r in range(i+1, len(nums)):
                    if nums[r] > nums[i]:
                        memo[i] = max(dp(r)+1, memo[i])
            return memo[i]
        
        maxx = 0
        for i in range(len(nums)):
            maxx = max(maxx, dp(i))
        return maxx