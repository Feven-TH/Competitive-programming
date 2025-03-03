class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = 0 
        for i in range(n):
            if reach < i:
                return False
            curr = i + nums[i]
            reach = max(reach, curr)
        return True
        # i = 0
        # diff = float('inf')
        # while i < n:
        #     val = nums[i]
        #     j = i + 1
        #     while j < val:
        #         diff = min(n - (j + nums[j])) 
        #     i = j
        #         if diff == 0:
        #             return True

