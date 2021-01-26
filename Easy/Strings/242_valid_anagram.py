# Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if len(counter_s.keys()) != len(counter_t.keys()):
            return False

        for key in counter_s.keys():
            if counter_s[key] != counter_t.get(key, 0):
                return False
        return True


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
