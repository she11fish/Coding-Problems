# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            if current == head:
                temp = current.next
                current.next = None
                prev = current
                if not temp:
                    break
                current = temp
            else:
                temp = current.next
                current.next = prev
                prev = current
                if not temp:
                    break
                current = temp
        return current
