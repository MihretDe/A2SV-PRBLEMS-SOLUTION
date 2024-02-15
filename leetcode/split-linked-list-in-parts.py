# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        first_extra = n % k
        res = n // k
        temp = head 
        result = []
        for _ in range(k):
            result.append(temp)
            if first_extra > 0:
                part_size=res + 1
                first_extra -= 1
            else:
                part_size=res 

            for _ in range(part_size - 1):
                if temp:
                    temp = temp.next
            if temp:
                curr = temp.next
                temp.next = None
                temp = curr
                
        return result