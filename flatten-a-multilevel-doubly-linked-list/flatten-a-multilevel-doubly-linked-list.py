"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head 
        dummy = Node(None, None, head, None)
        
        stack = [head]
        prev = dummy
        while stack:
            node = stack.pop()
            node.prev = prev
            prev.next = node
            
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
            prev = node
        dummy.next.prev = None
        return dummy.next