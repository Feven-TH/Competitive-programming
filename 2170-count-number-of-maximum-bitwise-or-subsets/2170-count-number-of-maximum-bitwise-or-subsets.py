class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxx = -float('inf') 
        counts = 0 
        n = len(nums)
        for i in range(1<<n):
            temp = 0
            for j in range(n):
                if i & (1 <<j):
                    temp |= nums[j]
            if temp > maxx:
                maxx = temp
                counts = 1
            elif temp == maxx:
                counts += 1
        return counts    