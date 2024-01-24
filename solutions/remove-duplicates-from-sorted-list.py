# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        temp = head.next
        while temp:
            if curr.val != temp.val:
                curr.next = temp
                curr = curr.next

            temp = temp.next
        curr.next=None
        return head
