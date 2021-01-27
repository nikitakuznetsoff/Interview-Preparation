# Count and Say

# he count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
#     countAndSay(1) = "1"
#     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
#     which is then converted into a different digit string.

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
            
        number = "1"

        for i in range(1, n):
            counter = 1
            temp_number = ""
            for i in range(1, len(number)):
                if number[i-1] == number[i]:
                    counter += 1
                else:
                    temp_number += str(counter) + str(number[i-1])
                    counter = 1
            temp_number += str(counter) + str(number[-1])
            number = temp_number

        return number+'\"'


sol = Solution()
print(sol.countAndSay(4))
