# Remove Duplicates from Sorted Array
#
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once
# and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != nums[counter]:
                nums[counter + 1] = nums[i]
                counter += 1
        return counter + 1

sol = Solution()
test_cases = [[1,1,2], [0,0,1,1,1,2,2,3,3,4]]
answers = [2, 5]

for i, case in enumerate(test_cases):
    print(sol.removeDuplicates(case) == answers[i])
