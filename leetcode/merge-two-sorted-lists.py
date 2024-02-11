# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        if not list1 and not list2:
            return list1
        if not list1 and list2 :
            return list2
        if not list2 and list1:
            return list1
        prev = None
        if left.val <= right.val:
            prev=left
            left=left.next
        else:
            prev=right
            right=right.next
        head=prev
        while left and right:
            if left.val <= right.val:
                prev.next=left
                prev=left
                left=left.next
                
            else:
                prev.next=right
                prev=right
                right=right.next
        if left:
            prev.next=left
        if right:
            prev.next=right
        return head



        

        