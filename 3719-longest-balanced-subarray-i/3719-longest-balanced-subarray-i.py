class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxx = 0 
        for i in range(len(nums)):
            odds, evens = defaultdict(int), defaultdict(int)
            for j in range(i,len(nums)):
                if nums[j] % 2!= 0:
                    odds[nums[j]] += 1
                else:
                    evens[nums[j]] += 1
                if len(odds) == len(evens):
                    maxx = max(maxx, j -i +1) 
                    
        return maxx