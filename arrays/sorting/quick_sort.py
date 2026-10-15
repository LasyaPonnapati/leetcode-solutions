# LeetCode: N/A — Quick Sort (foundational DSA practice)
# Quick Sort
# Given an array of integers nums, sort it in non-decreasing order
# using quick sort and return the sorted array.

# Approach:
# 1. If the subarray has 0 or 1 elements, it is already sorted (base case).
# 2. Pick the first element (nums[low]) as the pivot.
# 3. Partition: walk the rest of the subarray and swap so values <= pivot
#    sit on the left and values > pivot sit on the right, then put the
#    pivot in the middle. That index is now in its final sorted place.
# 4. Recursively quick-sort the left part and the right part.

# Time Complexity: O(n log n) average - each partition walks n elements,
# and balanced splits give about log n levels. O(n^2) worst case if the
# pivot is always the smallest or largest (for example an already-sorted
# array when we always pick the first element).
# Space Complexity: O(log n) average - only the recursion call stack;
# sorting is done in place. O(n) stack in the worst case.


def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[low]
    i = low
    j = high

    while i < j:
        while nums[i] <= pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]

    return j


def _quick_sort(nums: list[int], low: int, high: int) -> None:
    if low >= high:
        return

    pivot_index = partition(nums, low, high)
    _quick_sort(nums, low, pivot_index - 1)
    _quick_sort(nums, pivot_index + 1, high)


def quick_sort(nums: list[int]) -> list[int]:
    _quick_sort(nums, 0, len(nums) - 1)
    return nums
