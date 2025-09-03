import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b = math.isqrt(c - a*a)
            if a*a + b*b == c:
                return True
        return False
            
        