class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1), len(nums2)
        dp = [[-float('inf')]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                curr = nums1[i]*nums2[j]
                if i > 0 and j > 0:
                    dp[i][j] = max(curr, curr + dp[i-1][j-1])
                else:
                    dp[i][j] = curr
               
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]