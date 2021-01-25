# Plus One

# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list,
# and each element in the array contains a single digit.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        for i in reversed(range(1, len(digits))):
            if digits[i] > 9:
                digits[i] = 0
                digits[i - 1] += 1
        if digits[0] > 9:
            digits[0] = 0
            ans = [1]
            ans.extend(digits)
            return ans
        return digits
  
