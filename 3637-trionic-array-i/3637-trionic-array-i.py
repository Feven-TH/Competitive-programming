class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        count,n = 1, len(nums)
        if nums[0] >= nums[1]:
            return False
        
        for i in range(2,n):
            if nums[i] == nums[i-1]:
                return False
            if (nums[i-1] - nums[i]) * (nums[i-2] - nums[i-1]) < 0:
                count += 1
        return count == 3
