# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        binary_a = str(bin(a))[2:]
        binary_b = str(bin(b))[2:]

        diff = abs(len(binary_b) - len(binary_a))
        if len(binary_a) < len(binary_b):
            binary_a = '0' * diff + binary_a
        else:
            binary_b = '0' * diff + binary_b
        
        result = [0] * len(binary_a)
        memory = []
        last_index = len(result) - 1
        for i in range(len(result)):
            result[i] = int(binary_a[last_index-i]) ^ int(binary_b[last_index-i])
            if len(memory) > 0:
                if result[i] == 0:
                    result[i] = 1
                    memory.pop()
                elif result[i] == 1:
                    result[i] = 0

            if binary_a[last_index-i] == binary_b[last_index-i] and binary_a[last_index-i] == '1':
                memory.append(1)
            
        if len(memory) > 0:
            result.append(1)

        result_num = 0
        for i in range(len(result)):
            if result[i] == 1:
                result_num += 2 ** i

        return result_num

sl = Solution()
print(sl.getSum(1, 2))