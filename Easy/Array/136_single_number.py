# Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for value in nums:
            ans ^= value
        return ans

test_cases = [[2,2,1], [4,1,2,1,2], [1]]
answers = [1, 4, 1]

sol = Solution()

for i, case in enumerate(test_cases):
    print(sol.singleNumber(case) == answers[i])
