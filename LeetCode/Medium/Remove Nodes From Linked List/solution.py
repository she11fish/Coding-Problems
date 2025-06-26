# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            new = ListNode(curr.val, curr.next)
            temp = new.next
            new.next = prev
            prev = new
            new = temp
            curr = curr.next
        curr = prev

        start = ListNode(curr.val)
        curr_start = start
        while curr:
            temp = curr.next
            while temp and curr.val > temp.val:
                temp = temp.next
            if temp is None:
                break
            curr_start.next = ListNode(temp.val)
            curr_start = curr_start.next
            curr = temp
        prev = None
        curr = start
        while curr:
            new = ListNode(curr.val, curr.next)
            temp = new.next
            new.next = prev
            prev = new
            new = temp
            curr = curr.next
        return prev
