# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return (0,0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            summ = left_sum + right_sum + node.val
            counts = left_count + right_count + 1
            avg = summ//counts
            if avg == node.val:
                res += 1
            return (summ, counts)
        
        dfs(root)
        return res