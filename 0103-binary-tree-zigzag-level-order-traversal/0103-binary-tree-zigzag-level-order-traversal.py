# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def zigzag(root , flag):
            if not root:
                return []

            res = []
            q = deque([root])
            while q:
                n = len(q)
                curr = []

                for i in range(n):
                    node = q.popleft()
                    curr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                if flag:
                    curr.reverse()
                    
                res.append(curr)
                flag = not flag
            return res

        return zigzag(root , False)

