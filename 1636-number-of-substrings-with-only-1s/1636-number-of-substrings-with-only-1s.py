class Solution:
    def numSub(self, s: str) -> int:
        MOD = (10**9) +7
        res = 0
        curr = 0
        for i in range(len(s)):
            if s[i] == '1':
                curr += 1
            else:
                res += (curr + 1)*curr //2
                curr = 0
        res += (curr + 1)*curr //2
        return res % MOD
