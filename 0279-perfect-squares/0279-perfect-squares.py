class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1,int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for sq in nums:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], dp[i - sq] +1)
        return dp[n]


            