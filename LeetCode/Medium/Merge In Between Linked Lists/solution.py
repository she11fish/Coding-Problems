# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr2 = list2
        while curr2.next:
            curr2 = curr2.next
        head = list2
        tail = curr2
        curr1 = list1
        i = 0
        node_start = None
        while curr1:
            if i == a - 1:
                node_start = curr1
                break
            curr1 = curr1.next
            i += 1
        curr1 = list1
        i = 0
        node_end = None
        while curr1:
            if i == b + 1:
                node_end = curr1
                break
            curr1 = curr1.next
            i += 1
        node_start.next = head
        tail.next = node_end
        return list1
