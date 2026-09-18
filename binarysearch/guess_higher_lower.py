# LeetCode 374. Guess Number Higher or Lower
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, the pre-defined API guess(num) tells you
# whether your guess is higher or lower than the picked number.
# Return the number that was picked.
#
# guess(num) returns:
#   -1 if num is higher than the picked number
#    1 if num is lower than the picked number
#    0 if num equals the picked number

# Approach:
# 1. The answer is some integer in the sorted range 1 ... n, so binary search works.
# 2. Keep a search window with left (l) at 1 and right (h) at n.
# 3. While the window is valid (l <= h), look at the middle value m.
# 4. If guess(m) is 0, m is the picked number, so return m.
# 5. If guess(m) is -1, m is too high, so search the left half (h = m - 1).
# 6. If guess(m) is 1, m is too low, so search the right half (l = m + 1).
# 7. If the window becomes empty, return -1 (should not happen if a pick exists).

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, and mid variables are stored.


class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        h=n
        while l<=h:
            m=(l+h)//2
            if guess(m)==0:
                return m
            elif guess(m)==-1:
                h=m-1
            elif guess(m)==1:
                l=m+1
        return -1
