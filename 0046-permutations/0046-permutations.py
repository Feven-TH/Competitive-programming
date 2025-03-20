class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # n = len(nums)
        
        def backtrack(arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return 

            for i in nums:
                if i in arr:
                    continue
                arr.append(i)
                backtrack(arr)
                arr.pop()
        
        backtrack([])
        return ans