class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)
        left = 0
        if len(nums) == 1 or k==1:
            return nums
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                left = i
            if i - left + 1 == k:
                res[i - k + 1] = nums[i]
                left += 1
        return res
