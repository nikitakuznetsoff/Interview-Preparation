# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_borders = ['(', '{', '[']
        for value in s:
            if value in open_borders:
                stack.append(value)
            else:
                if len(stack) > 0:
                    if value == ')' and stack[-1] == '(':
                        stack.pop()
                    elif value == '}' and stack[-1] == '{':
                        stack.pop()
                    elif value == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0


sol = Solution()
arr = "]"
print(sol.isValid(arr))