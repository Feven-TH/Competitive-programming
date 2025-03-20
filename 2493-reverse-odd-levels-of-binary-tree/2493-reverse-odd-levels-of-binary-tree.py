# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(left , right , flag):
            if left is None or right is None:
                return
            if flag:
                right.val , left.val = left.val , right.val
                
            reverse(left.left , right.right , not flag)
            reverse(left.right , right.left ,  not flag)
            
        reverse(root.left , root.right , True)
        return root
