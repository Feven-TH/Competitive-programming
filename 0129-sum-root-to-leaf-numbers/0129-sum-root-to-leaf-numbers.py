# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def sums(root , temp):
            nonlocal res
            if root is None:
                return 
            temp = temp*10 + root.val
            if root.left is None and root.right is None:
                res += temp
            else:
                sums(root.left , temp)
                sums(root.right , temp )
            
            return res
        return sums(root , 0 )
            