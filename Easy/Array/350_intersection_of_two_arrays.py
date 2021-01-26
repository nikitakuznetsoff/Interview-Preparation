# Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.

from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_first = Counter(nums1)
        counter_second = Counter(nums2)
        answer = []
        for key, value in counter_first.items():
            if counter_second.get(key):
                answer.extend([key] * min(counter_first[key], counter_second[key]))
        return answer

sol = Solution()
ans = sol.intersect([4,9,5], [9,4,9,8,4])
print(ans)
print(ans == [4,9])
