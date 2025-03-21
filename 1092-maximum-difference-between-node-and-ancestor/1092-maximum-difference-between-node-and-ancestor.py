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
        def diff(node , maxx , minn):
            if node is None:
                self.res = max(self.res ,abs(minn - maxx))
                return 
            maxx = max(maxx , node.val)
            minn = min(minn , node.val)
       
            diff(node.left, maxx , minn)
            diff(node.right, maxx , minn)

            # return max(res)
        diff(root , root.val , root.val)
        return self.res
