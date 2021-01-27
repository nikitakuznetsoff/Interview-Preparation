# Longest Common Prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        i = 0
        while i < len(strs[0]):
            prefix = strs[0][:i+1]
            for s in strs:
                if not s.startswith(prefix):
                    return strs[0][:i]
            i += 1
        return strs[0][:i]


sol = Solution()
print(sol.longestCommonPrefix(["ab", "a"]))
