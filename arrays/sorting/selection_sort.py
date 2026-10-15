# LeetCode: N/A — Selection Sort (foundational DSA practice)
# Selection Sort
# Given an array of integers nums, sort it in non-decreasing order
# using selection sort and return the sorted array.

# Approach:
# 1. Make n - 1 passes over the array (outer loop with i). After pass i, the
#    smallest remaining value sits at index i, so the left part nums[0..i] is sorted.
# 2. In the unsorted part nums[i..n-1], find the index of the smallest value.
# 3. Swap that value with nums[i] so it is placed in its correct position.
# 4. After all passes, return nums.

# Time Complexity: O(n^2) - the outer loop runs about n times, and each pass
# scans the remaining unsorted part (up to n elements) to find the minimum.
# Space Complexity: O(1) - sorting is done in place with a min index and swaps only.

def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums