# Valid Palindrome

# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring case

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        line = str.lower(s)
        characters = []

        for letter in line:
            if str.isalpha(letter) or str.isnumeric(letter):
                characters.append(letter)

        for i in range(int(len(characters) / 2)):
            if characters[i] != characters[-i-1]:
                return False
        return True
