class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(x):
            if x <= 2:
                return x
            if x in memo:
                return memo[x]
            memo[x] = dp(x-1) + dp(x-2)
            return memo[x]
        return dp(n)
