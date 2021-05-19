# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        condition = False
        left_new, right_new = newInterval[0], newInterval[1]
        
        if not intervals:
            return [newInterval]
        
        if right_new < intervals[0][0]:
            result.append(newInterval)
        
        for i, interval in enumerate(intervals):
            if interval[1] < left_new:
                result.append(interval)
            elif interval[0] <= left_new and right_new <= interval[1]:
                result.append(interval)    
            elif left_new < interval[0] and interval[1] < right_new:
                condition = True
                continue
            elif interval[0] <= right_new and right_new <= interval[1]:
                right_new = interval[1]
                condition = True
            elif interval[0] <= left_new and left_new <= interval[1]:
                left_new = interval[0]
                condition = True
            elif right_new < interval[0]:
                if i > 0:
                    if intervals[i-1][1] < left_new:
                        condition = True
                if condition:
                    result.append([left_new, right_new])
                condition = False
                result.append(interval)
        
        if condition:
            result.append([left_new, right_new])
        
        if intervals[-1][1] < left_new:
            result.append(newInterval)
        
        return result
                    
                
