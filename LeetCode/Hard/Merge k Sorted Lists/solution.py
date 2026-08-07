# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        if len(lists) == 1:
            if lists[0] is None:
                return 
            return lists[0]
        for i in range(len(lists) - 1):
            list1 = lists[i + 1]
            list2 = lists[i]
            if list2 is None:
                continue
            if list1 is None:
                lists[i], lists[i + 1] = lists[i + 1], lists[i]
                continue
            curr1 = None
            curr2 = None
            if list1.val <= list2.val:
                curr1 = list1
                curr2 = list2
            else:
                curr1 = list2
                curr2 = list1
            head = ListNode()
            ls = head
            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    ls.next = curr1
                    curr1 = curr1.next
                else:
                    ls.next = curr2
                    curr2 = curr2.next
                ls = ls.next
            ls.next = curr1 or curr2
            lists[i + 1] = head.next
        return lists[-1]