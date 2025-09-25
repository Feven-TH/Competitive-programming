class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i], nums[i-1])
            if i not in memo:
                memo[i] = max(dp(i-2) + nums[i], dp(i-1))
            return memo[i]
        return dp(len(nums)-1)

     