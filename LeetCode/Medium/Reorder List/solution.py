# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next: return
        n = 0
        current = head
        while current:
            if not current.next:
                tail = current
            current = current.next
            n += 1
        i = 0
        current = head
        while (n + 1) // 2 != i:
            i += 1
            if (n + 1) // 2 == i:
                new_current = current.next
                current.next = None
                current = new_current
                continue
            current = current.next
        prev = current
        current = current.next
        prev.next = None
        while current:
            new_current = current.next
            current.next = prev
            prev = current
            current = new_current 
        current = head
        prev = tail
        while current and prev:
            new_current = current.next
            new_prev = prev.next
            current.next = prev
            prev.next = new_current
            current = new_current
            prev = new_prev
        return
