# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root,0)])
        res = []
        level = 0
        while q:
            curr = []
            for _ in range(len(q)):
                node, level = q.popleft()
                curr.append(node.val)
                if node.left: q.append((node.left, level + 1))
                if node.right: q.append((node.right, level + 1))
            if level % 2:
                res.append(curr[::-1])
            else:
                res.append(curr)
                
        return res        
        