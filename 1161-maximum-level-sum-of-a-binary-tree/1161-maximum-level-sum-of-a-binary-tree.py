# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        maxx = float('-inf')
        l, l_maxx = 1,1
        # print(q)
        while q:
            summ = 0
            for _ in range(len(q)):
                node = q.popleft()
                summ += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if summ > maxx:
                l_max = l
                maxx = summ
            l += 1
        return l_max
