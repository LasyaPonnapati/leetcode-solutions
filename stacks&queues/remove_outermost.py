# Remove Outermost Parentheses
# LeetCode 1021: A valid parentheses string s is primitive if it
# cannot be split into two non-empty valid parentheses strings.
# Given a valid parentheses string s, remove the outermost
# parentheses of every primitive string in the primitive
# decomposition of s, and return s after the removals.
#
# Example: "(()())(())" decomposes into "(()())" + "(())".
# After removing the outer pair of each part, the result is "()()()".
#
# Approach: Scan left to right and keep unmatched '(' on a stack.
# A '(' is outermost if the stack is empty before we push it, so we
# skip it. A ')' is outermost if it closes that last remaining '(',
# so we skip it too. Every other bracket is inner and goes into ans.
#
# Time: O(n) — each character is pushed/popped at most once and
#       appended to ans at most once.
# Space: O(n) — the stack can hold up to n/2 opening brackets, and
#        ans can grow to length n.


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                if len(stack) != 0:
                    ans += s[i]
                stack.append(s[i])
            else:
                if len(stack) != 1:
                    ans += s[i]
                stack.pop()
        return ans
