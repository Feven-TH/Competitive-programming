# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def maxxx(node , maxx , minn):
            if node is None:
                self.res = max(self.res ,abs(minn - maxx))
                return 
            maxx = max(maxx , node.val)
            minn = min(minn , node.val)
       
            maxxx(node.left, maxx , minn)
            maxxx(node.right, maxx , minn)

            # return max(res)
        maxxx(root , root.val , root.val)
        return self.res
