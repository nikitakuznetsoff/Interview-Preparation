# Merge Sorted Array

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough space
# to hold additional elements from nums2.

import copy
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            return

        index_1, index_2 = 0, 0
        nums_first = copy.copy(nums1)

        for i in range(len(nums1)):
            if index_1 == m:
                nums1[i] = nums2[index_2]
                index_2 += 1
                continue
            if index_2 == n:
                nums1[i] = nums_first[index_1]
                index_1 += 1
                continue
            if nums_first[index_1] < nums2[index_2]:
                nums1[i] = nums_first[index_1]
                index_1 += 1
            else:
                nums1[i] = nums2[index_2]
                index_2 += 1

sol = Solution()
sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
