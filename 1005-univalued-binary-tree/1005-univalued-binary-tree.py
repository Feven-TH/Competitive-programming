# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visited = set()
        queue = deque([root])
        val = root.val
    
        while queue:

            for curr in range(len(queue)):
                if root.val not in visited:
                    visited.add(root.val)
                    queue.append(root)
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if curr.val != val:
                    return False
        return True 

            