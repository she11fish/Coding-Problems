# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if list1:
                return list1
            if list2:
                return list2
            return list1
        arr1 = []
        while list1:
            arr1.append(list1.val)
            list1 = list1.next
        arr2 = []
        while list2:
            arr2.append(list2.val)
            list2 = list2.next
        new_arr = arr1 + arr2
        new_arr.sort()
        new_list = ListNode(new_arr[0])
        head = new_list
        for i in range(1, len(new_arr)):
            new_list.next = ListNode(new_arr[i])
            new_list = new_list.next
        return head
