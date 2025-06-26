# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            if head.val == val:
                return None
            return head
        while head and head.val == val:
            head = head.next
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                temp = curr.next
                while temp and temp.val == val:
                    temp = temp.next
                curr.next = temp
            curr = curr.next
        return head
