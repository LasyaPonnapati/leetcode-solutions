# Bubble Sort
# Given an array of integers nums, sort it in non-decreasing order
# using bubble sort and return the sorted array.

# Approach:
# 1. Make n - 1 passes over the array (outer loop with i). After pass i, the next
#    largest remaining value has "bubbled" to the end, so the last i elements are sorted.
# 2. In each pass, walk the unsorted part with j from 0 to n - i - 2.
# 3. Compare neighbors nums[j] and nums[j + 1]. If they are out of order, swap them.
# 4. After all passes, return nums.

# Time Complexity: O(n^2) - the outer loop runs about n times, and the inner loop
# also runs up to about n comparisons on each pass.
# Space Complexity: O(1) - sorting is done in place with swaps only.

def bubble_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
                # if in any pass, no swaps are made, the array is sorted
                # and we can break out of the loop
        if not swapped:
            break
    return nums
