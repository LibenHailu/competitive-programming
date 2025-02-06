# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def validate(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (node2 and not node1) or (node1.val != node2.val):
                return False 
            return validate(node1.right, node2.left) and validate(node1.left, node2.right)
        return validate(root.left, root.right)