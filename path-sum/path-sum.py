# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node:
                return False 
            if not node.left and not node.right and cur_sum == targetSum:
                return True 
            
            return dfs(node.left, cur_sum + node.left.val if node.left else 0) or dfs(node.right, cur_sum + node.right.val if node.right else 0) 
        
        if not root:
            return False
        return dfs(root, root.val)