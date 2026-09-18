# Next Greater Element II
# LeetCode 503: nums is circular. For each nums[i], find the first
# greater number walking forward (and wrapping to the start if
# needed). If none exists, use -1.


# Approach: For each i, scan the next n-1 positions in a circle
# using indices i+1 .. i+n-1. idx = j-n maps those into nums
# (negative idx when j < n, wrap-around when j >= n).
#
# Time: O(n^2) — for each of n elements we may scan up to n-1 others.
# Space: O(n) — ans stores one result per element (not counting input).


class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            for j in range(i + 1, i + n):
                idx = j - n
                if nums[idx] > nums[i]:
                    ans[i] = nums[idx]
                    break
        return ans


# Approach 2: Walk a doubled circular view right to left (i = 2n-1 .. 0).
# The stack holds values to the right. For i >= n we only maintain the
# stack (the wrap-around copy). For i < n we also write ans[i].
#
# Time: O(n) — each value is pushed and popped at most twice (once per copy).
# Space: O(n) — the stack and ans are both size n.


class SolutionUsingStack:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = []
        ans = [-1] * n
        for i in range(2 * n - 1, -1, -1):
            # Wrap-around copy: only build the stack, do not fill ans
            if i >= n:
                idx = i - n
                if not s:
                    s.append(nums[idx])
                    continue
                if nums[idx] < s[-1]:
                    s.append(nums[idx])
                    continue
                while s and s[-1] <= nums[idx]:
                    s.pop()
                s.append(nums[idx])
                continue

            # Real index: same stack rules, and record the answer
            if not s:
                s.append(nums[i])
                continue
            if nums[i] < s[-1]:
                ans[i] = s[-1]
                s.append(nums[i])
                continue
            while s and s[-1] <= nums[i]:
                s.pop()
            if s:
                ans[i] = s[-1]
            s.append(nums[i])
        return ans
