# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater = None
        less = None
        ptr = head
        gr=None
        while ptr:
            if ptr.val  < x:
                if less==None:
                    less=ptr
                    head = less

                else:
                    less.next=ptr
                    less=ptr
            else:
                if greater ==None:
                    greater = ptr
                    gr = greater
                else:
                    greater.next=ptr
                    greater = ptr
            ptr = ptr.next
        if greater:
            greater.next=None
        if less:
            less.next=gr

        return head
