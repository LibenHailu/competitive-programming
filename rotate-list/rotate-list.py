# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        k %= l
        
        while k:
            curr = head
            prev = None
            while curr and curr.next:
                prev = curr
                curr = curr.next
            new_head = prev.next
            prev.next = None
            new_head.next = head
            head = new_head
            k -= 1
        return head
                