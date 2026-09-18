# LeetCode 278. First Bad Version
# You have n versions [1, 2, ..., n]. All versions after the first bad
# version are also bad. You are given an API isBadVersion(version) that
# returns True if that version is bad. Find the first bad version while
# minimizing API calls.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Approach:
# 1. Versions are sorted: good versions come first, then all remaining
#    versions are bad. That sorted pattern lets us use binary search.
# 2. Search in the range 1 ... n. Keep left (l) at 1 and right (h) at n.
# 3. While the window is valid (l <= h), look at the middle version m.
# 4. If m is bad, it might be the first bad version, or an earlier one
#    might still exist. Save m as a candidate and search the left half
#    (h = m - 1).
# 5. If m is good, every version before m is also good, so the first bad
#    version is to the right (l = m + 1).
# 6. When the window is empty, the saved candidate is the first bad version.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, mid, and answer variables are stored.


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        h = n
        ans = 0
        while l <= h:
            m = (l + h) // 2
            if isBadVersion(m):
                ans = m
                h = m - 1
            else:
                l = m + 1
        return ans
