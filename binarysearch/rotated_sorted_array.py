# LeetCode 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct
# values). Prior to being passed to your function, nums is possibly rotated
# at an unknown pivot index k (1 <= k < nums.length) such that the resulting
# array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...,
# nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at
# pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Approach:
# 1. A rotated sorted array still has two sorted pieces. In any window,
#    at least one of the two halves around mid is fully sorted.
# 2. Keep a search window with left (l) at 0 and right (h) at the last index.
# 3. While the window is valid (l <= h), look at the middle index m.
# 4. If arr[m] is the target, return m.
# 5. If the left half is sorted (arr[l] <= arr[m]):
#      - If target is in that sorted range [arr[l], arr[m]), search left.
#      - Otherwise search right.
# 6. Else the right half is sorted:
#      - If target is in that sorted range (arr[m], arr[h]], search right.
#      - Otherwise search left.
# 7. If the window becomes empty, the target is not in the array.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, and mid indices are stored.


class Solution:
    def search(self, arr: list[int], target: int) -> int:
        l=0
        h=len(arr)-1
        while l<=h:
            m=(l+h)//2
            if arr[m]==target:
                return m
            elif arr[l]<=arr[m]:
                if arr[l]<=target<arr[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if arr[m]<target<=arr[h]:
                    l=m+1
                else:
                    h=m-1
        return -1
