# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        substr = set()
        max_length = 0
        
        while right < len(s):
            # print(s[right], substr, left, right)
            if s[right] not in substr:
                substr.add(s[right])
            else:
                while s[right] in substr and left < right:
                    substr.remove(s[left])
                    left += 1
                substr.add(s[right])
            right += 1
            if max_length < len(substr):
              max_length = len(substr)
        return max_length
        

sl = Solution()
print(sl.lengthOfLongestSubstring("abcabcbb"))