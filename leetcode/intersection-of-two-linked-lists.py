# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        temp = headA
        while temp:
            s.add(temp)
            temp=temp.next
        temp2 = headB
        while temp2:
            if temp2 in s:
                return temp2
            temp2 = temp2.next
        return None

        