class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 1
        maxx,n = float('-inf'),len(nums)
        for i in range(len(nums)):
            while j < n and nums[j] <= k*nums[i]:
                j += 1 
            maxx = max(maxx, j -i)
        return n - maxx