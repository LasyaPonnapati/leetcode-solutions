# LeetCode 767. Reorganize String
# Rearrange the characters of s so that no two adjacent characters
# are the same. If it is impossible, return "".

# Approach (count, sort by frequency, fill even indices first):
# 1. Count how many times each character appears.
# 2. If any character appears more than (n + 1) // 2 times, two of
#    that character would have to sit next to each other, so return "".
# 3. Sort characters by count, highest first.
# 4. Place them into the answer at even indices 0, 2, 4, ... then
#    wrap to odd indices 1, 3, 5, ... so the same letter is spaced out.

# Time Complexity: O(n) - we scan s once to count, sort at most 26
# letters, then write n positions in the answer.
# Space Complexity: O(n) - the answer list has length n. The count
# map has at most 26 keys.

class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        n = len(s)
        ans = [""] * n
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[i] > (n + 1) // 2:
                return ""
        chars = sorted(d, key=lambda c: d[c], reverse=True)
        idx = 0
        for char in chars:
            for _ in range(d[char]):
                ans[idx] = char
                idx += 2
                if idx >= n:
                    idx = 1
        return "".join(ans)
