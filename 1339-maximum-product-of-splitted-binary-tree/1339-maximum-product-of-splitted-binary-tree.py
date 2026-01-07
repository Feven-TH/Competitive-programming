# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree = []
        MOD = 10**9 + 7
        def summ(node):
            if not node:
                return 0
            left = summ(node.left)
            right = summ(node.right)
            curr = left + right + node.val
            subtree.append(curr)
            return curr
        summ(root)
        # print(subtree)
        maxx = float('-inf')
        total = subtree[-1]
        for i in range(len(subtree)-1):
            curr = subtree[i]
            maxx = max(maxx, curr*(total -curr))
        return maxx % MOD

        