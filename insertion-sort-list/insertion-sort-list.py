# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        iterate through all the elements 
        do the swap 
        '''
        dummy = ListNode()
        cur = head
        while cur:
            prev = dummy
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next
            
            next_node = cur.next
            cur.next = prev.next
            prev.next = cur 
            cur = next_node
        return dummy.next
