# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def prefix_function(s: str) -> List[int]:
            prefix = [-1] * len(s)
            prefix[0] = 0
            for i in range(1, len(s)):
                j = prefix[i-1]
                while (j > 0 and s[i] != s[j]):
                    j = prefix[j-1]
                if (s[i] == s[j]):
                    j += 1
                prefix[i] = j
            return prefix

        if needle == "":
            return 0
        prefix = prefix_function(needle + "#" + haystack)
        for i in range(len(prefix)):
            if prefix[i] == len(needle):
                return i - 2 * len(needle)
        return -1


sol = Solution()
print(sol.strStr("hello", "ll"))
