# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None:
            return head
        prev = None
        curr = head
        next = curr.next
        duplicate = None
        start = None
        while curr:
            if not next:
                if curr.val != duplicate:
                    prev = curr
                    if start == None:
                        start = prev
                else:
                    if prev:
                        prev.next = next
                break
            if curr.val != next.val:
                if curr.val != duplicate:
                    prev = curr
                    if start == None:
                        start = prev
                else:
                    if prev:
                        prev.next = next
                curr = curr.next
                next = next.next
            else:
                duplicate = curr.val
                curr = curr.next
                next = curr.next
        return start