# Valid Parentheses
# LeetCode 20: Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string
# is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type of brackets.
# 2. Open brackets are closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the
#    same type.
#
# Approach: Scan left to right. Push opening brackets onto a stack.
# When you see a closer, it must match the most recent unmatched
# opener (the top of the stack). Pop if it matches; otherwise the
# string is invalid. At the end the stack must be empty (no leftover
# openers).
#
# Time: O(n) — each character is pushed and/or popped at most once.
# Space: O(n) — the stack can hold up to n opening brackets.


class Solution:
    def isValid(self, s: str) -> bool:
        opn = ['[', '(', '{']
        stack = []
        for i in s:
            if i in opn:
                stack.append(i)
            elif len(stack) != 0 and i == ']' and stack[-1] == '[':
                stack.pop()
            elif len(stack) != 0 and i == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) != 0 and i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
