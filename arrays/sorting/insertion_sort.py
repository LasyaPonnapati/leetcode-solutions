# LeetCode: N/A — Insertion Sort (foundational DSA practice)
# Insertion Sort
# Given an array of integers nums, sort it in non-decreasing order
# using insertion sort and return the sorted array.

# Approach:
# 1. The left part nums[0..i-1] is already sorted. Start i at 1 (one element is sorted).
# 2. Save the current value as ele = nums[i], then walk left from i.
# 3. While the left neighbor is greater than ele, shift that neighbor one step right.
# 4. Put ele into the gap. After all i, return nums.

# Time Complexity: O(n^2) - for each of n elements we may scan/shift up to i
# already-sorted elements to the left.
# Space Complexity: O(1) - sorting is done in place; only ele and j are extra.

def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        ele = nums[i]
        j = i
        while j > 0 and ele < nums[j - 1]:
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = ele
    return nums
