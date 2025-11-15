class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        count = 0
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                if intervals[i][0] >= intervals[i + 1][1] and intervals[i][1] <= intervals[i + 1][1]:
                    count += 1
                    intervals.pop(i + 1)
                    continue
                if intervals[i + 1][0] >= intervals[i][1] and intervals[i + 1][1] <= intervals[i][1]:
                    count += 1
                    intervals.pop(i)
                    continue
                intervals.pop(max(i, i + 1, key=lambda t: intervals[t][1]))
                count += 1
            else:
                i += 1
        return count
