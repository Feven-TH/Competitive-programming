class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        maps = Counter(power)
        vals = sorted(maps.keys())
        damage = [maps[v]*v for v in vals]

        dp = [0]*(len(vals))
        dp[0], j = damage[0], -1

        for i in range(1,len(vals)):
            while j < i+1 and vals[j + 1] <= vals[i] - 3:
                j += 1
            dp[i] = max(dp[i-1], damage[i] + (dp[j] if j != -1 else 0))

        return dp[-1]