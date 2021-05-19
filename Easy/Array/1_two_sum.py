# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
# test
from collections import Counter
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = Counter(nums)
        first, second = 0, 0
        results = []

        for key in d.keys():
            if d.get(target - key):
                if target == 2 * key and d[key] < 2:
                    continue
                first = key
                second = target - key
                break
        
        i = 0
        while len(results) < 2:
            if nums[i] == first:
                results.append(i)
            elif nums[i] == second:
                results.append(i)
            i += 1
        return sorted(results)

sl = Solution()
print(sl.twoSum([2,7,11,15], 9))
