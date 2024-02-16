# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        temp = head
        for i in range(left-1):
            temp = temp.next
        while left < right:
            curr_right = temp
            for i in range(left,right):
                curr_right = curr_right.next
            y = curr_right.val
            curr_right.val=temp.val
            temp.val=y
            temp=temp.next
            left+=1
            right-=1
        return head
            
