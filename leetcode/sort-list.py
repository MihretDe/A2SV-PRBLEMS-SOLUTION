# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1 , list2):
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
        def get_mid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def merge_sort(head):
            if not head or head.next == None:
                return head
            left = head
            right = get_mid (head)
            tmp = right.next
            right.next= None
            right = tmp
            left = merge_sort(left)
            right =  merge_sort(right)
            return merge(left , right)
        h = merge_sort(head)
        return h
           
    
