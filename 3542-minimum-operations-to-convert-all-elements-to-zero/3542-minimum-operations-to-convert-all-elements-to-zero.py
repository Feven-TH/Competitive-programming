class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        count = 0
        
        for x in nums:
            if x == 0:
                stack = []
                continue
            while stack and stack[-1] > x:
                stack.pop()
        
            if not stack or stack[-1] < x:
                count += 1
                stack.append(x)
        return count