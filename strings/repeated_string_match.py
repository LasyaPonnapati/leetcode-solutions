# LeetCode 686. Repeated String Match
# Return the minimum number of times you should repeat string a so that
# string b is a substring of the repeated a. If impossible, return -1.

# Approach (keep appending a until b is a substring):
# 1. Start with one copy of a and count = 1.
# 2. While the current string is shorter than b, append the original a
#    and increase the count (b cannot fit until we are at least as long).
# 3. If b is already a substring, return the count.
# 4. Append one more copy of a. This covers the wrap-around case
#    (b can start in the middle of a and spill into the next copy).
# 5. If b is still not a substring, it is impossible, so return -1.

# Time Complexity: O(n * m) - we build a string of length O(n + m) and
# each "b in s" scan takes O(len(s) * m) in the worst case, with n = len(a)
# and m = len(b).
# Space Complexity: O(n + m) - the repeated string is at most about
# len(b) + 2 * len(a) characters.

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        orig = a
        ans = 1
        while len(a) < len(b):
            a += orig
            ans += 1
        if b in a:
            return ans
        a += orig
        ans += 1
        if b in a:
            return ans
        return -1
