class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def lcm(a,b):
            return (a*b)//gcd(a,b)

        def check(lim,a,b,c):
            single = lim//a + lim//b + lim//c
            double = lim//lcm(a,b) + lim//lcm(a,c) + lim//lcm(b,c)
            triple = lim//lcm(a,lcm(b,c)) 
            return single - double + triple
            

        high,low = 2*(10**9) + 2, 1
        ans = high
        while low <= high:
            mid = low + (high - low)//2
            count = check(mid,a,b,c) 
            if count >= n:
                ans = mid
                high = mid -1
            else: 
                low = mid + 1
        return ans
                
