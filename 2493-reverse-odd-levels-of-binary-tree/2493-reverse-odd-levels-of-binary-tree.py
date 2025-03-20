# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        track = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            if track %2 != 0:
                l , r = 0 , n - 1
                while l < r:
                    queue[l].val , queue[r].val = queue[r].val , queue[l].val
                    l += 1
                    r -= 1
            # print(queue)
            for i in range(n):
                node = queue.popleft()  
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            track += 1
        return root



