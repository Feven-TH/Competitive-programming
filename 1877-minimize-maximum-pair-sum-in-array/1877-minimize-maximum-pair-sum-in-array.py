class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0
        l = len(nums) - 1
        for i in range(len(nums)//2):
            maxx = max(maxx, nums[i] + nums[l])
            l -= 1
        return maxx