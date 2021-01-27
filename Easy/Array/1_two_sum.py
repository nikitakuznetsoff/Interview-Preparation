# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from collections import Counter
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = Counter(nums)
        ans = []
        j = 0

        for i, key in enumerate(d.keys()):
            if d.get(target - key):
                if target == 2 * key and d[key] < 2:
                    continue
                ans.append(i)
                j = i
                break

        for i in range(j + 1, len(nums)):
            if target - nums[j] == nums[i]:
                ans.append(i)
                break
        return ans