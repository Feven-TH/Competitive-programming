class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {0 : -1}
        prefix = 0
        maxx = 0
        for i , num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1
            
            if prefix not in maps:
                maps[prefix] = i
            else:
                maxx = max(maxx , i - maps[prefix])
        return maxx
