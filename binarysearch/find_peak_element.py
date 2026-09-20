# LeetCode 162. Find Peak Element
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of
# the peaks.
# You may imagine that nums[-1] = nums[n] = -infinity. In other words, an
# element is always considered to be strictly greater than a neighbor that
# is outside the array.
# You must write an algorithm that runs in O(log n) time.

# Approach:
# 1. Keep a search window with left (l) at 0 and right (h) at the last index.
# 2. Imagine nums[n] = -infinity, so the last index can still be a peak.
# 3. While the window is valid (l <= h), look at the middle index m.
# 4. If m is the last index, or nums[m] is greater than nums[m+1], the slope
#    is falling (or we are at the end). m is a peak candidate, so save it and
#    search the left half (h = m - 1).
# 5. Else nums[m] < nums[m+1], so the slope is rising. A peak must be to the
#    right, so search the right half (l = m + 1).
# 6. Return the last saved peak candidate.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, mid, and ans indices are stored.


class Solution:
    def findPeakElement(self, arr: list[int]) -> int:
        l=0
        n=len(arr)
        h=n-1
        ans=0
        while l<=h:
            m=(l+h)//2
            if m==n-1 or arr[m]>arr[m+1]:
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
