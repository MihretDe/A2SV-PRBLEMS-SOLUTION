# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        y = 0
        temp = head
        while temp:
            y += 1
            temp = temp.next
        d = y - n
        if d == 0:
            return head.next

        y = 0
        temp = head
        while y < d - 1:
            temp = temp.next
            y += 1

        temp.next = temp.next.next

        return head
        # slow = head
        # y =0
        # fast=head
        # while y < n:
        #     fast=fast.next
        #     y+=1
        # while 

        