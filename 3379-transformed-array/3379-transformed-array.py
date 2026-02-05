class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        for ind,val in enumerate(nums): 
            res[ind] = nums[(ind + val) % len(nums)]
        return res               