class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        # res = 1
        def count(n):
            if n % 2 == 0:
                return (pow(5 , n//2, mod) * pow(4 , n//2, mod)) % mod
                # return (5**(n//2)) * (4**(n//2))
            else:
                return (5 * count(n - 1)) % mod
        return count(n) % mod
        






        # def count(x ,even):
        #     nonlocal res
        #     if x == n :
        #         return res % mod
        #     if even:
        #         res *= 5
        #         # print(res)
        #         return count(x + 1, not even)
        #     else:
        #         res *= 4
        #         # print(res)
        #         return count(x + 1, not even)
            
        # return count(0,True)

