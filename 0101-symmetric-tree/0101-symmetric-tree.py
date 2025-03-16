class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if left is None and right is None:  
                return True
            if left is None or right is None: 
                return False
            if left.val != right.val:  
                return False

            return (
                helper(left.left, right.right) and  
                helper(left.right, right.left)  )
        if root is None:
            return True
        return helper(root.left, root.right)
