# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        while l1:
            nums1.append(str(l1.val))
            l1 = l1.next
        nums2 = []
        while l2:
            nums2.append(str(l2.val))
            l2 = l2.next
        temp = list(str(int("".join(nums1[::-1])) + int("".join(nums2[::-1]))))[::-1]
        start = ListNode(temp[0])
        l3 = start
        i = 1
        while i < len(temp): 
            l3.next = ListNode(temp[i])
            l3 = l3.next
            i += 1   
        return start
