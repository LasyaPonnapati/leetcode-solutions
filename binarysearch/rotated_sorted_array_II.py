# LeetCode 81. Search in Rotated Sorted Array II
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values). Before being passed to your function,
# nums is rotated at an unknown pivot index k (0 <= k < nums.length) such
# that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
# nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7]
# might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true
# if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.

# Approach:
# 1. Same idea as rotated search without duplicates: in any window, at least
#    one half around mid is sorted. Use that half to decide where target can
#    still be. Return True/False instead of an index.
# 2. Duplicates add one extra case. If arr[l], arr[m], and arr[h] are all
#    equal, you cannot tell which half is sorted (example: [1,0,1,1,1]).
#    Shrink both ends by one and continue. This is safe because mid was
#    already checked and was not the target.
# 3. If arr[l] <= arr[m] <= arr[h] but they are not all equal, this window
#    has no rotation drop, so it is fully sorted. Do normal binary search:
#    go left if target is smaller than mid, right if it is larger.
# 4. Otherwise the window is still rotated. If the left half is sorted
#    (arr[l] <= arr[m]), search left only when target is in [arr[l], arr[m]).
#    Else the right half is sorted; search right only when target is in
#    (arr[m], arr[h]].
# 5. If the window becomes empty, the target is not in the array.

# Time Complexity: O(n) worst case, O(log n) typical - each step usually
# cuts the window in half, but when l, m, and h are equal we only shrink
# the window by two indices, which can become linear on arrays like
# [1,1,1,1,1].
# Space Complexity: O(1) - only left, right, and mid indices are stored.


class Solution:
    def search(self, arr: list[int], target: int) -> bool:
        l=0
        h=len(arr)-1
        while l<=h:
            m=(l+h)//2
            if arr[m]==target:
                return True
            elif arr[l]<=arr[m]<=arr[h]:
                if arr[l]==arr[m]==arr[h]:
                    l=l+1
                    h=h-1
                    continue
                elif arr[m]>target:
                    h=m-1
                elif arr[m]<target:
                    l=m+1
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
        return False
