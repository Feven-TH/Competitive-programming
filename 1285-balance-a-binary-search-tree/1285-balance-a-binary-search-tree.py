# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) +[root.val] + inorder(root.right)
        def balance(ordered):
            if not ordered:
                return None
            mid = len(ordered)//2
            root = TreeNode(ordered[mid])
            root.left = balance(ordered[:mid])
            root.right = balance(ordered[mid+1:])
            return root
        
        ordered = inorder(root)
        return balance(ordered)
        