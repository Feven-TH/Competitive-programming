class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0 
            if rem < 0:
                return float('inf')
            if rem not in memo:
                res = float('inf')
                for c in coins:
                    res = min(res, 1 + dp(rem-c))
                memo[rem] = res
            return memo[rem]
        ans = dp(amount)
        return ans if ans != float('inf') else -1