# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversedDummy  = ListNode()
        dummyPtr = reversedDummy
        cur = head
        while cur:
            reversedDummy.next = ListNode(cur.val)
            cur = cur.next
            reversedDummy = reversedDummy.next
        
        prev = None 
        cur = dummyPtr.next
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        while head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
            
            