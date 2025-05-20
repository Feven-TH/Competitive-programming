class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while right != left:
            right >>= 1
            left >>= 1
            i += 1
        return left << i