# Reverse bits of a given 32 bits unsigned integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = str(bin(n))[2:]
        shift = 32 - len(reversed_num)
        result = 0
        for i in range(len(reversed_num)):
            if reversed_num[i] == '1':
                result += 2**(i+shift)
        return result


sl = Solution()
print(sl.reverseBits(43261596))