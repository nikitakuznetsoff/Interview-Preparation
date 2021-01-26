# Contains Duplicates
# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i, v in enumerate(nums):
            if v in d:
                return True
            else:
                d[v] = 1
        return False
