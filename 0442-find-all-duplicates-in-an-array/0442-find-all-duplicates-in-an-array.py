class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            bucket[num].append(num)
        
        res = []
        for i in range(len(bucket)):
            if len(bucket[i]) == 2:
                res.append(bucket[i][0])
        return res 
        