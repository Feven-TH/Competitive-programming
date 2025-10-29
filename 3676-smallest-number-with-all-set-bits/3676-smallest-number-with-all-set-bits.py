class Solution:
    def smallestNumber(self, n: int) -> int:
        b = 1
        while (1 << b) - 1 < n:
            b += 1
        return (1 << b) -1