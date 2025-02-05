# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        res = dummy
        while list1 or list2:
            if not list1:
                res.next = list2
                break
            elif not list2:
                res.next = list1
                break
            else:
                if list1.val > list2.val:
                    res.next = ListNode(list2.val)
                    res = res.next
                    list2 = list2.next
                else:
                    res.next = ListNode(list1.val)
                    res = res.next
                    list1 = list1.next
        return dummy.next  