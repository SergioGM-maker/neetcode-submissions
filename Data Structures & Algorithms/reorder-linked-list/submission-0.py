# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        # Getting lenght
        size = 1
        listing = head

        while not not listing:
            size += 1
            listing = listing.next

        half = 0
        if size%2 == 1:
            half = size//2 +1
        else:
            half = size//2 
        midd = head
        
        # Splitting the list
        while half > 1 and not not midd:
            half -= 1
            midd = midd.next
        

        
        last = midd
        if midd:
            midd= midd.next

        if last:
            last.next = None

        #Turning the second half of the list around
        head_reverse = midd

        if midd and head_reverse:
            midd = midd.next
            head_reverse.next = None


        next = midd
        while not not midd:
            next = midd.next
            midd.next = head_reverse
            head_reverse = midd
            midd = next
        
        #Uniting the lists
        while not not head and not not head_reverse:
            next = head.next
            head.next = head_reverse
            head = next

            next = head_reverse.next
            head_reverse.next = head
            head_reverse = next
        
        return None