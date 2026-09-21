# LeetCode 540. Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every
# element appears exactly twice, except for one element which appears
# exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

# Approach:
# 1. Pairs sit on even/odd indexes before the unique element:
#    (0,1), (2,3), ... After the unique element, pairing shifts.
# 2. Binary search the middle index m.
# 3. If arr[m] is not equal to either neighbor (watch the ends), m is unique.
# 4. If m is even: a matching arr[m+1] means pairs are still intact, so
#    search right; otherwise search left.
# 5. If m is odd: a matching arr[m-1] means pairs are still intact, so
#    search right; otherwise search left.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, and mid indexes are stored.


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n=len(arr)
        l=0
        h=n-1
        while l<=h:
            m=(l+h)//2
            if (m==0 or arr[m-1]!=arr[m]) and (m==n-1 or arr[m]!=arr[m+1]):
                return arr[m]
            if m%2==0:
                if arr[m]==arr[m+1]:
                    l=m+1
                else:
                    h=m-1
            else:
                if arr[m]==arr[m-1]:
                    l=m+1
                else:
                    h=m-1
