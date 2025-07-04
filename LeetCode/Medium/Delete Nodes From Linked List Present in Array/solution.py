# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hash_set = set(nums)
        curr = head
        prev = None
        while curr:
            if curr.val in hash_set:
                if prev is None:
                    head = curr.next
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
