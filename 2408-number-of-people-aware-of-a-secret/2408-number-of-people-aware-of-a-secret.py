class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        learned = [0]*(n + 1)
        learned[1] = 1  
        shareable = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                shareable = (shareable + learned[day - delay]) % MOD
            if day - forget >= 1:
                shareable = (shareable - learned[day - forget]) % MOD
            learned[day] = shareable%MOD
        
        res = 0
        for day in range(n - forget + 1, n + 1):
            res = (res+ learned[day]) % MOD

        return res
