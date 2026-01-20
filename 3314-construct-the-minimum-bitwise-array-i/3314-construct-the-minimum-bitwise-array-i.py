class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            x = num
            c = -1
            for j in range(1, x):
                if (j | (j + 1)) == x:
                    c = j
                    break
            res.append(c)
        return res