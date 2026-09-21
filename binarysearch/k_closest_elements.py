# LeetCode 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k
# closest integers to x in the array. The result should also be sorted
# in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or |a - x| == |b - x| and a < b.

# Approach:
# 1. Binary search for x. If found, start the window at that index m.
# 2. If x is missing, the search ends with h just left of the insert
#    point and l just right of it. Start at whichever of arr[h] or
#    arr[l] is closer to x (on a tie, pick the smaller, arr[h]).
# 3. Grow a window [left, right] from that start until it has k
#    elements. At each step compare the next left and next right
#    candidate; expand toward the closer one (tie -> left).
# 4. If one side is out of bounds, expand the other side.

# Time Complexity: O(log n + k) - binary search finds the start, then
# the window grows by 1 at most k-1 times.
# Space Complexity: O(1) extra - only indexes are stored; the answer
# slice is the required output.


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        n=len(arr)
        h=n-1
        m=0
        while l<=h:
            m=(l+h)//2
            if arr[m]==x:
                break
            elif arr[m]>x:
                h=m-1
            else:
                l=m+1
        # case where x is not found in the array, then we need to find the closest element to x
        else:
            if h<0:
                m=0
            elif l>=n:
                m=n-1
            elif x-arr[h]<=arr[l]-x:
                m=h
            else:
                m=l
        left=m
        right=m
        k-=1
        while k!=0:
            if left==0:
                right+=1
            elif right==n-1:
                left-=1
            elif x-arr[left-1]<=arr[right+1]-x:
                left-=1
            else:
                right+=1
            k-=1
        return arr[left:right+1]
