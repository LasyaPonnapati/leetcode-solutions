# LeetCode: N/A — Merge Sort (foundational DSA practice)
# Merge Sort
# Given an array of integers nums, sort it in non-decreasing order
# using merge sort and return the sorted array.

# Approach:
# 1. If the array has 0 or 1 elements, it is already sorted (base case).
# 2. Split the array into two halves around the middle index.
# 3. Recursively sort the left half and the right half.
# 4. Merge the two sorted halves into one sorted array and return it.

# Time Complexity: O(n log n) - the array is split in half log n times,
# and each level of merging walks through all n elements.
# Space Complexity: O(n) - merge needs extra lists of size n, plus
# O(log n) call-stack frames from the recursion.


def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)
