class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i,summ):
            if summ == amount:
                return 1
            if i == len(coins) or summ > amount:
                return 0
            if (i,summ) not in memo:
                memo[(i,summ)] = dp(i+1, summ) + dp(i, summ + coins[i])
            return memo[(i,summ)]
        return dp(0,0)