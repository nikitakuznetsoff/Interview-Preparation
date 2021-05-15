# 191. Number of 1 Bits

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        num = n
        counter = 0
        while num > 0:
            if num % 2 == 1:
                counter += 1
            num = int(num/2)
        return counter