# String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string
# to a 32-bit signed integer (similar to C/C++'s atoi function).


class Solution:
    def myAtoi(self, s: str) -> int:
        text = s.lstrip()
        if len(text) == 0:
            return 0

        arr_number = []
        index = 0
        is_negative = text[index] == '-'

        if text[index] == '-' or text[index] == '+':
            index += 1

        while index < len(text) and str.isnumeric(text[index]):
            arr_number.append(text[index])
            index += 1

        if len(arr_number) == 0:
            return 0


        result_num = 0
        for i in range(len(arr_number)):
            arr_number[i] = ord(arr_number[i]) - 48
            result_num += (10 ** (len(arr_number)-1-i)) * arr_number[i]

        if is_negative:
            result_num *= -1

        if result_num > 2**31 - 1:
            return 2**31 - 1

        if result_num < -2**31:
            return -2**31

        return result_num


sol = Solution()
print(sol.myAtoi("+1"))
