# Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].
#  00
#  01
#  10
#  11
#  100
#  101
#  110
#  111
#  1000


from typing import List

class Solution:
    def countBits(self, num: int) -> List[int]:
        results = [0, 1, 1, 2]
        if num < 4:
            return results[:num+1]

        category = 4
        counter = 0
        for i in range(4, num+1):
            index = i - category
            results.append(results[index]+1)
            counter += 1

            if counter == category:
                category *= 2
                counter = 0
        return results


sol = Solution()
print(sol.countBits(5))