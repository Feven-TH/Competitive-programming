class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        sets = set(stones)
        if 1 not in sets:
            return False 
        def dp(curr,k):
            if curr == stones[-1]:
                return True
            if (curr,k) not in memo:
                flag = False
                for i in range(k-1, k+2):
                    if i > 0 and curr+i in sets and dp(curr + i, i):
                        memo[(curr, k)] = True
                        return True
            memo[(curr, k)] = False
            return memo[(curr,k)]
        return dp(1,1)