# LeetCode 1781. Sum of Beauty of All Substrings
# The beauty of a string is the difference in frequencies between
# the most frequent and least frequent characters.
# Given a string s, return the sum of beauty of all of its substrings.

# Approach (expand each substring and track letter counts):
# 1. For each start index i, start a new frequency map.
# 2. Count s[i], then grow the substring by moving j to the right.
# 3. After each new character, add max(count) - min(count) to the
#    answer. Only letters that appear in this substring are in the
#    map, so min is the least frequent letter that actually appears.
# 4. Length-1 substrings have beauty 0, so we skip them.

# Time Complexity: O(n^2) - two nested loops over the string. Each
# inner step updates one count and scans the map (at most 26 keys).
# Space Complexity: O(1) - the map holds at most 26 letters.

class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            d = {}
            if s[i] not in d:
                d[s[i]] = 0
            d[s[i]] += 1
            for j in range(i + 1, len(s)):
                if s[j] not in d:
                    d[s[j]] = 0
                d[s[j]] += 1
                ans += max(d.values()) - min(d.values())
        return ans
