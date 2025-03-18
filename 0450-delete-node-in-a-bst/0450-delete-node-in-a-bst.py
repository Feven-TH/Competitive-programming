# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(root, key):
            if not root:
                return root
            if key < root.val:
                root.left = delete(root.left, key)
            elif(key > root.val):
                root.right = delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = minValueNode(root.right)
                root.val = temp.val
    
                root.right = delete(root.right, temp.val)
            return root

        def minValueNode(node):
            current = node
            while current.left:
                current = current.left
            return current

        return delete(root,key)

            
