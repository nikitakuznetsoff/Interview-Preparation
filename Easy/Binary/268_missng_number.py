# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_value = 0
        for i in range(1, len(nums)+1):
            missing_value ^= i
        for v in nums:
            missing_value ^= v
        return missing_value

sol = Solution()
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))