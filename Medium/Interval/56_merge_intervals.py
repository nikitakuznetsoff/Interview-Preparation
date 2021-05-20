# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            if intervals[i-1][1] < intervals[i][0]:
                results.append(intervals[i-1])
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = intervals[i-1][0]
            if intervals[i][1] <= intervals[i-1][1]:
                intervals[i][1] = intervals[i-1][1]
        results.append(intervals[-1])


sl = Solution()
print(sl.merge([[1,4],[0,4]]))
            
  