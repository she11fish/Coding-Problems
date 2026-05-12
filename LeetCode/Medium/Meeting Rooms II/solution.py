"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        import heapq

        remaining = sorted(intervals, key=lambda e: e.start)
        heap = []
        s = 0
        while remaining:
            t = []
            for interval in remaining:
                if not heap:
                    heapq.heappush(heap, -interval.end)
                    continue
                if interval.start >= -heap[0]:
                    heapq.heappush(heap, -interval.end)
                else:
                    t.append(interval)
            remaining = t
            heap = []
            s += 1
        return s
