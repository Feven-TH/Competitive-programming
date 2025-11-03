class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(n):
            if n <0:
                return 0
            return (n+1)*(n+2)//2
        c_all = comb(n)
        one_invalid = 3*(comb(n-(limit+1)))
        two_invalid = 3*(comb(n-2*(limit+1)))
        three_invalid = comb(n-3*(limit+1))

        invalid = one_invalid - two_invalid + three_invalid
        return c_all - invalid
        
