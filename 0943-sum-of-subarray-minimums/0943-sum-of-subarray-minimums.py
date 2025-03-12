class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        stack = []

        # stacks = [1 , 2, 3 ]

        for i , val in enumerate(arr):
            while stack and arr[stack[-1]] > val:
                popped = stack.pop()
                left = (popped - stack[-1]) if stack else popped + 1
                right = i - popped
                
                res += (arr[popped] * left * right) % mod
            stack.append(i)

        for i in range(len(stack)):
            left = stack[i] - stack [i - 1] if i > 0 else stack[i] + 1
            right = len(arr) - stack[i]
            res += (arr[stack[i]] * left * right) % mod
            
        return res 

                

