# Rotate array
# Given an array, rotate the array to the right by k steps, where k is non-negative.

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) < 2 or k == 0:
            return

        start_index = 0
        index = 0
        last_value = nums[0]

        for _ in range(len(nums)):
            index = (index + k) % len(nums)

            if index == start_index:
                nums[index] = last_value
                index = (index + 1) % len(nums)
                start_index = index
                last_value = nums[index]
                continue

            nums[index], last_value = last_value, nums[index]
