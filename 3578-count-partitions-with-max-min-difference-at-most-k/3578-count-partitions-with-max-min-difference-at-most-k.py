class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        dp = [0]*(n+1)
        prefix = [0]*(n+1)
        dp[0],prefix[0] = 1,1
        maxx,minn = deque(), deque()
        j = 0

        for i in range(n):
            while maxx and nums[maxx[-1]] <= nums[i]:
                maxx.pop()
            maxx.append(i)
            while minn and nums[minn[-1]] >= nums[i]:
                minn.pop()
            minn.append(i)

            while nums[maxx[0]] - nums[minn[0]] > k:
                if maxx[0] == j:
                    maxx.popleft()
                if minn[0] == j:
                    minn.popleft()
                j += 1
            if j == 0:
                dp[i+1] = prefix[i] % mod
            else:
                dp[i+1] = (prefix[i] - prefix[j-1] + mod) % mod
            prefix[i+1] = (prefix[i] + dp[i+1]) % mod
        
        return dp[-1]