# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        curr = None
        while fast and fast.next:
            fast = fast.next.next
            curr = slow
            slow = slow.next
        if fast:
            slow = slow.next
        prev = None
        curr1 = slow
        while curr1:
            temp = curr1.next
            curr1.next = prev
            prev = curr1
            curr1 = temp 
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
        

        