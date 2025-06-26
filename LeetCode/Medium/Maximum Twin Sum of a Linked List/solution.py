# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        curr = head
        n = 0
        while curr:
            start = ListNode(curr.val)
            start.next = prev
            prev = start
            curr = curr.next
            n += 1
        tail = prev
        curr = head
        middle = n // 2
        i = 0
        maximum = float('-inf')
        while i < middle:
            if maximum < (curr.val + tail.val):
                maximum = curr.val + tail.val
            curr = curr.next
            tail = tail.next
            i += 1 
        return maximum
        
