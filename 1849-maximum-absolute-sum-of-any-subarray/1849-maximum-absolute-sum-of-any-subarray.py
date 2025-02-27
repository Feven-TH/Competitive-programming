class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxx = nums[0]
        res = nums[0]
        minn= nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            maxx = max(maxx + nums[i] , nums[i])
            res = max(maxx, res)  
            minn = min(minn + nums[i] , nums[i])   
            ans = min(ans ,minn)

        return(max(abs(ans) , res))

