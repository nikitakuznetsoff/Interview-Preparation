# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        while x > 0 or y > 0:
            counter += x%2 != y%2
            x = int(x/2)
            y = int(y/2)
        return counter


sol = Solution()
print(sol.hammingDistance(1, 4))