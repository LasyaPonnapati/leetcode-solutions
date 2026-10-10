# LeetCode 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence keeps the relative order of characters, but some characters of t may be skipped.
# Example: "ace" is a subsequence of "abcde", but "aec" is not.

# Approach (two pointers):
# 1. x walks through s. y walks through t.
# 2. While both pointers are still inside their strings:
#    - If s[x] matches t[y], move both forward. That character of s has been found.
#    - Otherwise move only y forward, skipping this character of t.
# 3. If x reaches the end of s, every character of s was found in order.

# Time Complexity: O(m) - m is the length of t. y moves forward on every loop step, so the loop runs at most m times.
# Space Complexity: O(1) - only the two pointer variables are used.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        x, y = 0, 0
        while x < n and y < m:
            if s[x] == t[y]:
                x += 1
                y += 1
            else:
                y += 1
        if x == n:
            return True
        return False
