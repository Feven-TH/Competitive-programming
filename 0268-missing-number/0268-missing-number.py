class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            bucket[num].append(num)
        
        for i in range(len(bucket)):
            if len(bucket[i]) == 0:
                return i 
        