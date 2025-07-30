class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxx = max(nums)
        count = max_count = 0
        
        for num in nums:
            if num == maxx:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0  
                
        return max_count
