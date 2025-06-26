# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        prev = None
        while curr:
            new = ListNode(curr.val)
            new.next = prev
            prev = new
            curr = curr.next
        curr = head
        end = new
        while curr:
            if curr.val != end.val:
                return False
            curr = curr.next
            end = end.next
        return True
