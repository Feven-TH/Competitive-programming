# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def maxx(node , depth):
            if not node:
                return res
            if len(res) == depth:
                res.append(node.val)
            else:
                if res[depth] < node.val:
                    res[depth] = node.val
            maxx(node.left , depth + 1)
            maxx(node.right , depth + 1)
            
            return res
        return maxx(root, 0)