# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(int(len(s) / 2)):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
