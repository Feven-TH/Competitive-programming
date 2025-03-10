class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for b in s:
            if b == '(':
                stack.append(0)
            else:
                popped = stack.pop()    
                if popped == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * popped
        return stack[0]
