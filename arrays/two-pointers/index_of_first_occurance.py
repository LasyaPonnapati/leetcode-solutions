# LeetCode 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first
# occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Approach 1 (try every start index):
# 1. If needle is longer than haystack, it cannot fit — return -1.
# 2. Walk every start index x in haystack.
# 3. When haystack[x] matches needle[0], check the slice haystack[x:x+m].
# 4. If the slice equals needle, return x.
# 5. If no start works, return -1.

# Time Complexity: O(n * m) - for each of up to n start positions we may compare
# up to m characters (n = len(haystack), m = len(needle)).
# Space Complexity: O(1) - only a few indices; slicing creates a short temporary string.


class Solution:
    def strStr(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if m > n:
            return -1
        x = 0
        while x < n:
            if s[x] == t[0]:
                if s[x : x + m] == t:
                    return x
            x += 1
        return -1


# Approach 2 (KMP — Knuth-Morris-Pratt):
# Brute force re-checks characters from the start of needle after a mismatch.
# KMP preprocesses needle into an lps array: lps[i] = length of the longest
# proper prefix of t[0..i] that is also a suffix of that same piece.
# When s[i] != t[j], we slide j back using lps[j-1] instead of restarting j at 0,
# so haystack index i never moves backward.
#
# 1. Build lps for needle (one pass over t).
# 2. Scan haystack with i (haystack) and j (needle). On match, advance both.
# 3. On mismatch with j > 0, set j = lps[j - 1]. If j == 0, advance i only.
# 4. When j == m, needle matched starting at i - m.

# Time Complexity: O(n + m) - each index of s and t moves forward only; lps build is O(m).
# Space Complexity: O(m) - the lps array for needle.


class Solution:
    def strStr(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        if m > n:
            return -1

        lps = [0] * m
        length = 0
        k = 1
        while k < m:
            if t[k] == t[length]:
                length += 1
                lps[k] = length
                k += 1
            elif length > 0:
                length = lps[length - 1]
            else:
                lps[k] = 0
                k += 1

        i = 0
        j = 0
        while i < n:
            if s[i] == t[j]:
                i += 1
                j += 1
                if j == m:
                    return i - m
            elif j > 0:
                j = lps[j - 1]
            else:
                i += 1
        return -1
