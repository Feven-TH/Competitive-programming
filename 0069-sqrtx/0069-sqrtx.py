class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high and high:
            mid = (low + high) //2
            if mid**2 <= x:
                low = mid + 1
            else:
                high = mid - 1
        return high