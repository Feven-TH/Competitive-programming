class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        maxx = [0] * len(s)
        ones = -1
        for i in s:
            if i == '1':
                maxx[ones] = 1
                ones += 1
        return ''.join(str(nums) for nums in maxx)

