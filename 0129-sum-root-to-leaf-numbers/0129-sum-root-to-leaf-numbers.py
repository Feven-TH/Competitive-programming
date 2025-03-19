# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = [(root , 0)]
        
        while stack:
            node , curr = stack.pop()
            curr = curr*10 + node.val

            if node.left is None and node.right is None:
                res += curr
            else:
                if node.right:
                    stack.append((node.right , curr))
                if node.left:
                    stack.append((node.left , curr))
        return res
