# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def gst(node, add):
            if node is None:
                return 0
            
            original = node.val
            node.val += add
            right = gst(node.right, add)
            node.val += right
            left = gst(node.left, node.val)

            return original + left + right

            
            # node.val += gst(node.right)
            # gst(node.right , temp + node.right.val)

        gst(root, 0)
        return root