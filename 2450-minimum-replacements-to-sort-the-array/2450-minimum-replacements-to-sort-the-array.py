class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        maxx = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > maxx:
                k = ceil(nums[i]/maxx)
                res += (k-1)
                maxx = nums[i]//k
            else:
                maxx = nums[i]
        return res
            

            
                