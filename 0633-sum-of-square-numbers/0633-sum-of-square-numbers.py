class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(c**0.5)+1
        while l <=r:
            curr = l**2 + r**2
            if curr == c:
                return True
            elif curr >c:
                r -= 1
            else:
                l += 1
        return False
                
            

