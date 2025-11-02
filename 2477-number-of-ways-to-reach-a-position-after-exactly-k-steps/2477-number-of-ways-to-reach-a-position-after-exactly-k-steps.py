class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        d = endPos - startPos 
        if (k + d) % 2 != 0 or abs(d) > k:
            return 0
        r = (k + d)//2 
        num = factorial(k) % MOD
        deno = factorial(r)*factorial(k-r) 
        return num * pow(deno, MOD-2, MOD) % MOD
