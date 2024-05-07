# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = []
        
        # loop through linked list
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        nums2 = []
        
        # loop through linked list
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
            
        
        # Adding placeholders for addition
        nums1 = nums1[::-1]
        nums2 = nums2[::-1]
        while len(nums1) != len(nums2):
            if len(nums1) < len(nums2):
                nums1.insert(0, 0)
            else:
                nums2.insert(0, 0)
                
        # Addition
        result = []
        placeholder = 0
        for i in range(len(nums1)-1,-1,-1):
            num1 = nums1[i]
            num2 = nums2[i]
            total = num1 + num2 + placeholder
            if total > 9:
                placeholder = 1
                result.append(total % 10)
            else:
                placeholder = 0
                result.append(total)
        if placeholder == 1:
            result.append(1)
            
        head = ListNode(result[0])
        curr = head
        for i in range(1, len(result)):
            curr.next = ListNode(result[i])
            curr = curr.next
        curr.next = None
        
        return head
                
        