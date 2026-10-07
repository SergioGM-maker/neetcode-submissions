# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        head = head.next
        current.next = None
        one_before = current

        while head is not None:
            current = head

            head = head.next

            current.next = one_before

            one_before = current
            
        return current

        