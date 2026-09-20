# LeetCode 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find
# the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Approach:
# 1. Binary search until we land on an index m where arr[m] == target.
# 2. That m is some occurrence, not necessarily the first or last.
# 3. Search the left half [l, m] with another binary search to find
#    the leftmost index still equal to target.
# 4. Search the right half [m, h] with another binary search to find
#    the rightmost index still equal to target.
# 5. If the outer search never finds target, return [-1, -1].

# Time Complexity: O(log n) - outer search plus two extra binary
# searches, each cutting its window in half each step.
# Space Complexity: O(1) - only a few indices and the answer pair.


class Solution:
    def searchRange(self, arr: list[int], target: int) -> list[int]:
        l=0
        h=len(arr)-1
        ans=[-1,-1]
        while l<=h:
            m=(l+h)//2
            if arr[m]==target:
                low=l
                high=m
                while low<=high:
                    mid=(low+high)//2
                    if arr[mid]==target:
                        ans[0]=mid
                        high=mid-1
                    else:
                        low=mid+1
                low=m
                high=h
                while low<=high:
                    mid=(low+high)//2
                    if arr[mid]==target:
                        ans[1]=mid
                        low=mid+1
                    else:
                        high=mid-1
                return ans
            elif arr[m]<target:
                l=m+1
            else:
                h=m-1
        return ans
