class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        shift = n>>1
        temp = shift ^ n
        return (temp & (temp+1)) == 0