# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
        
        lenB = 0
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next
        
        startA = headA
        startB = headB
        if lenA > lenB:
            diff = lenA - lenB
            while diff:
                startA = startA.next
                diff -= 1
        
        if lenB > lenA:
            diff = lenB - lenA
            while diff:
                startB = startB.next
                diff -= 1
        
        while startA and startB:
            if startA == startB:
                return startA
            startA = startA.next
            startB = startB.next
        return startA
        