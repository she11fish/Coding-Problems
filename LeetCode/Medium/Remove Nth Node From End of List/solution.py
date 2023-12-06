# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n == 1:
            return
        current = head
        i = 0
        while current:
            if not current.next:
                tail = current
            current = current.next
            i += 1
        target = i - n
        if target == 0:
            return head.next
        current = head
        current = head.next
        prev = head
        k = 1
        while current:
            if k == target:
                prev.next = current.next
                current.next = None
                return head
            prev = current
            current = current.next
            k += 1
