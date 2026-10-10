# LeetCode 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that, together with the x-axis, form a container holding the most
# water. Return the maximum amount of water that container can store.
# You may not slant the container.

# Approach 1 (brute force):
# 1. Pick every pair of lines. x is the left line, y is a line to its right.
# 2. The water between them is the shorter height times the distance (y - x).
# 3. Compare that area with the biggest area seen so far and keep the larger one.
# 4. After every pair has been checked, return that biggest area.

# Time Complexity: O(n^2) - for each left line, every line to its right is checked, so every pair is calculated once.
# Space Complexity: O(1) - only a few variables are stored besides the input array.

class Solution:
    def maxArea(self, arr: list[int]) -> int:
        n = len(arr)
        area = 0
        for x in range(n):
            for y in range(x + 1, n):
                area = max(area, min(arr[x], arr[y]) * (y - x))
        return area

# Approach 2 (two pointers):
# 1. x starts at the left end and y starts at the right end, so the width is as
#    large as it can be.
# 2. The water between two lines is the shorter height times the distance (y - x).
# 3. Keep the biggest area seen so far.
# 4. The shorter line limits the area, so move that pointer inward to look for a
#    taller line. If the heights are equal, move x right.
# 5. Stop when x and y meet.

# Time Complexity: O(n) - x and y only move toward each other, so each index is visited once.
# Space Complexity: O(1) - only a few variables are stored besides the input array.

class Solution:
    def maxArea(self, arr: list[int]) -> int:
        n = len(arr)
        x = 0
        y = n - 1
        area = 0
        while x < y:
            area = max(area, min(arr[x], arr[y]) * (y - x))
            if arr[x] <= arr[y]:
                x += 1
            else:
                y -= 1
        return area
