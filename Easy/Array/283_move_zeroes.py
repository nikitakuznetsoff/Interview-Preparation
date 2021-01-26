# Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ind = 0
        ind = 1

        while ind < len(nums) and zero_ind < len(nums):
            while zero_ind < len(nums) and nums[zero_ind] != 0:
                zero_ind += 1

            if ind < zero_ind:
                ind = zero_ind

            while ind < len(nums) and nums[ind] == 0:
                ind += 1

            if zero_ind < len(nums) and ind < len(nums):
                nums[ind], nums[zero_ind] = nums[zero_ind], nums[ind]
