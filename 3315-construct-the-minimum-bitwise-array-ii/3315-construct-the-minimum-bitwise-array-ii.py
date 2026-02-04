class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            res = -1
            bit = 1
            while num & bit:
                res = num & ~bit
                bit <<= 1
            ans.append(res)
        return ans
            

