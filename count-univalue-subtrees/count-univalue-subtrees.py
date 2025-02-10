# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(node):
            if not node:
                return True
            
            isLeftUniSubTree = dfs(node.left)
            isRightUniSubTree = dfs(node.right)
            
            count = 0
            if isLeftUniSubTree and isRightUniSubTree:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                self.count += 1
                return True
            return False 
        dfs(root)
        return self.count
                