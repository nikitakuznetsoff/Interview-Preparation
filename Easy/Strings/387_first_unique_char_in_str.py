# First Unique Character in a String

# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, v in enumerate(s):
            if counter.get(v, 0) == 1:
                return i
        return -1
