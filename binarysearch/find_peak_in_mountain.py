# LeetCode 852. Peak Index in a Mountain Array
# You are given a mountain array arr. A mountain array of length n is
# guaranteed to have some peak index i (0 < i < n - 1) such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[n - 1]
# Return the index of the peak. You must solve it in O(log n) time.

# Approach:
# 1. Values increase up to the peak, then decrease, so binary search works.
# 2. Keep a search window with left (l) at 0 and right (h) at the last index.
# 3. While the window is valid (l <= h), look at the middle index m.
# 4. If arr[m] > arr[m + 1], m is on the decreasing side, so m could be the
#    peak, but a peak further left is still possible. Save m and search left.
# 5. If arr[m] < arr[m + 1], m is on the increasing side, so the peak is
#    strictly to the right. Search the right half (l = m + 1).
# 6. When the window is empty, the saved index is the peak.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, mid, and answer variables are stored.


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l=0
        h=len(arr)-1
        ans=0
        while l<=h:
            m=(l+h)//2
            if arr[m]>arr[m+1]:
                ans = m
                h=m-1
            elif arr[m]<arr[m+1]:
                l=m+1
        return ans
