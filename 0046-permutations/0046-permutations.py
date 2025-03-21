class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        n = len(nums)
        
        def backtrack():
            if len(arr) == n:
                ans.append(arr[:])
                return 

            for i in nums:
                if i in arr:
                    continue
                arr.append(i)  
                backtrack()
                arr.pop()
            
        backtrack()
        return ans