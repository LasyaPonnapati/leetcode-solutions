# LeetCode 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded
# down to the nearest integer. You must not use a built-in exponent
# function or operator (no pow, no x ** 0.5).

# Approach:
# 1. The integer square root is the largest integer m such that m * m <= x.
#    Possible answers lie in the sorted range 0 ... x, so binary search works.
# 2. Keep a search window with left (l) at 0 and right (r) at x.
# 3. While the window is valid (l <= r), look at the middle value m.
# 4. If m * m == x, m is the exact square root, so return m.
# 5. If m * m < x, m could still be the answer, but a bigger value might
#    also work, so save m and search the right half (l = m + 1).
# 6. If m * m > x, m is too big, so search the left half (r = m - 1).
# 7. When the window is empty, the saved value is floor(sqrt(x)).

# Time Complexity: O(log x) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, mid, and answer variables are stored.


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0
        while l <= r:
            m = (l + r) // 2
            square = m * m
            if square == x:
                return m
            elif square < x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans
