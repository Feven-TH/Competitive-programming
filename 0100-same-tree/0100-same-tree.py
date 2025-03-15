# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(p , q):
            if p == None and q == None:
                return True
            if (p == None and q != None) or (q == None and p != None):
                return False  
            if p.val != q.val:
                return False
            return compare(p.left , q.left) and compare(p.right , q.right)
             
        return compare(p , q)