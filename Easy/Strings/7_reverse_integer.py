# Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        numbers = []
        number = abs(x)

        if number == 0:
            return 0

        while number > 0:
            numbers.append(int(number % 10))
            number = int(number / 10)

        if numbers[0] == 0:
            numbers = numbers[1:]

        answer = 0
        for i in range(len(numbers)):
            answer += (10**i) * numbers[-i-1]

        if answer > 2**31 - 1:
            return 0

        if x < 0:
            answer *= -1

        return answer


sol = Solution()
print(sol.reverse(120))
