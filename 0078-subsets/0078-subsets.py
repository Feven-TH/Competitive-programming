
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, arr):
            ans.append(arr[:])

            for i in range(first, n): 
                arr.append(nums[i])  
                backtrack(i + 1, arr)  
                arr.pop()  
        
        ans = []  
        n = len(nums)  
        
        backtrack(0, []) 
        return ans
