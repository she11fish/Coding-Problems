# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                temp = curr.next
                while temp and curr.val == temp.val:
                    temp = temp.next
                curr.next = temp
            curr = curr.next
        return head
