# LeetCode 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between
# 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times, or [0,1,2,4,5,6,7] if it was
# rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ...,
# a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the
# minimum element of this array.
# You must write an algorithm that runs in O(log n) time.

# Approach:
# 1. A rotated sorted array still has two sorted pieces. In any window,
#    at least one of the two halves around mid is fully sorted.
# 2. Keep a search window with left (l) at 0 and right (h) at the last
#    index, and track the smallest value seen so far in ans.
# 3. While the window is valid (l <= h), look at the middle index m.
# 4. If the left half is sorted (arr[l] <= arr[m]), the smallest value
#    in that half is arr[l]. Update ans, then search the right half,
#    because the true minimum may still be past the rotation.
# 5. Else the left half is not sorted, so the rotation (and the minimum)
#    is in [l, m]. arr[m] is the smallest value in the sorted right
#    piece, so update ans and search left of m.
# 6. When the window is empty, ans is the minimum.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, mid, and ans are stored.


class Solution:
    def findMin(self, arr: list[int]) -> int:
        l=0
        h=len(arr)-1
        ans=float('inf')
        while l<=h:
            m=(l+h)//2
            if arr[l]<=arr[m]:
                ans=min(arr[l],ans)
                l=m+1
            else:
                ans=min(arr[m],ans)
                h=m-1
        return ans
