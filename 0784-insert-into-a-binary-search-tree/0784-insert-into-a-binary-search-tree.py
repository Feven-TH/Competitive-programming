# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def help(node, val):
            if node is None:
                new = TreeNode(val)
                node = new
            if node.left is None and node.val > val:
                new = TreeNode(val)
                node.left = new
            if node.right is None and node.val < val:
                new = TreeNode(val)
                node.right = new
            if node.val > val:
                help(node.left , val)
            if node.val < val:
                help(node.right , val)
            return node
        return help(root , val)