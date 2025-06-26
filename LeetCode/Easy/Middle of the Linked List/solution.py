# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        desired_index = n // 2
        i = 0
        curr = head
        while curr:
            if i == desired_index:
                return curr
            curr = curr.next
            i += 1
        
        
