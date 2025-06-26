# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        start = ListNode()
        another_curr = start
        while curr:
            while curr and curr.val == 0:
                curr = curr.next
            total = 0
            while curr and curr.val != 0:
                total += curr.val
                curr = curr.next
            if total != 0:
                another_curr.next = ListNode(total)
            another_curr = another_curr.next
        return start.next
