# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur(node, left, right):
            if not node:
                return True
            if not left < node.val < right:
                return False
            ans = True
            if node.left:
                ans = ans and recur(node.left, left, node.val)
            if node.right:
                ans =  ans and recur(node.right, node.val, right)
            return ans
        return recur(root, float("-inf"), float("inf"))