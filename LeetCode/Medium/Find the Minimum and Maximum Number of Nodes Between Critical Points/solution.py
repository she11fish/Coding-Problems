# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        next_node = head.next.next
        curr_critical_point, index = None, None
        first_critical_point, first_index = None, None
        min_distance = float('inf')
        max_distance = float('-inf')
        i = 1
        while next_node:
            is_local_min = curr.val < prev.val and curr.val < next_node.val
            is_local_max = curr.val > prev.val and curr.val > next_node.val
            is_critical_point = is_local_min or is_local_max
            if is_critical_point and curr_critical_point is not None:
                print(i, index)
                delta_distance = i - first_index
                if delta_distance > max_distance:
                    max_distance = delta_distance
                delta_distance = i - index
                if delta_distance < min_distance:
                    min_distance = delta_distance
                curr_critical_point, index = curr, i
            elif is_critical_point:
                curr_critical_point, index = curr, i
                first_critical_point, first_index = curr, i
            i += 1
            prev = prev.next
            curr = curr.next
            next_node = next_node.next
        if min_distance == float('inf') or max_distance == float('-inf'):
            return [-1, -1]
        return [min_distance, max_distance]
