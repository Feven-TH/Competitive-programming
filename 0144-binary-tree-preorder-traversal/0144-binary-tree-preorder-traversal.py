# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def help(node):
            if node == None:
                return
            res.append(node.val)
            help(node.left)
            help(node.right)
        help(root)
        return res