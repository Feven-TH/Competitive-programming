class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i == len(s1):
                return sum(ord(c) for c in s2[j:])
            if j == len(s2):
                return sum(ord(c) for c in s1[i:])
            if s1[i] == s2[j]:
                return dp(i+1, j+1)
            
            del_1 = ord(s1[i]) + dp(i+1,j)
            del_2 = ord(s2[j]) + dp(i,j+1)

            return min(del_1,del_2)
        return dp(0,0)
