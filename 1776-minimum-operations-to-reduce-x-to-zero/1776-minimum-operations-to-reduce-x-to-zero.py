class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:  
            return -1
        left, maxx, summ = 0,-1 ,0
        for i in range(len(nums)):
            summ += nums[i]
            while summ > target:
                summ -= nums[left]
                left += 1
            if summ == target:
                maxx = max(maxx, i - left +1)
        
        return len(nums) - maxx if maxx != -1 else -1


        
