class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        
        if target not in nums:
            return [-1,-1]
        return [left,right]
        
        # res = [0 ,0]
        # nums.sort()
        # if len(nums) == 0:
        #     return [-1,-1]

        # left = bisect_left(nums, target)
        # right = bisect_right(nums, target)
        # res[0] = left
        # res[1] = right - 1

        # if 0 <= left < len(nums):
        #     if nums[left] != target:
        #         res[0] = -1
        
        # if 0 <= right < len(nums):
        #     if nums[right - 1] != target:
        #         res[1] = -1

        # return res