# LeetCode 189. Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example: nums = [1, 2, 3, 4, 5, 6, 7], k = 3 -> [5, 6, 7, 1, 2, 3, 4]

# Approach 1 (slicing):
# 1. k = k % n, because rotating by the full length brings the array back to the start.
# 2. arr[-k:] is the last k elements. After a right rotate, those belong at the front.
# 3. arr[:-k] is everything before those last k elements.
# 4. Join them in that order and return the new list. The original arr is unchanged.

# Time Complexity: O(n) - slicing and joining copy every element once.
# Space Complexity: O(n) - the new list stores all n elements.
# This uses more memory than the reverse approach below, which only needs a few index variables.

class Solution:
    def rotate(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        k = k % n
        return arr[-k:] + arr[:-k]

# Approach 2 (hold last element and shift right, k times):
# 1. k = k % n, so we do not repeat a full cycle that leaves the array unchanged.
# 2. Save the last element in hold.
# 3. Move every element one place to the right, starting from the end so values are not overwritten.
# 4. Put hold at index 0. That is one right rotation.
# 5. Repeat steps 2 to 4, k times.

# Time Complexity: O(n * k) - each of the k rotations shifts about n elements.
# Space Complexity: O(1) - only hold is extra; the array is changed in place.
# This is slower than the reverse approach, which finishes in one pass over the array.

class Solution:
    def rotate(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        k = k % n
        for _ in range(k):
            hold = arr[-1]
            for i in range(n - 1, 0, -1):
                arr[i] = arr[i - 1]
            arr[0] = hold
        return arr

# Approach 3 (reverse three times):
# 1. k = k % n, because rotating by the full length brings the array back to the start.
# 2. Reverse the whole array.
# 3. Reverse the first k elements. Those are the values that should sit at the front.
# 4. Reverse the remaining elements so they are back in their original order.
# Example with [1, 2, 3, 4, 5, 6, 7] and k = 3:
# reverse all        -> [7, 6, 5, 4, 3, 2, 1]
# reverse first 3    -> [5, 6, 7, 4, 3, 2, 1]
# reverse the rest   -> [5, 6, 7, 1, 2, 3, 4]

# Time Complexity: O(n) - each reverse walks its section once, and together they touch each element a constant number of times.
# Space Complexity: O(1) - only the index variables inside reverse are extra; swaps happen in the same array.

class Solution:
    def rotate(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        k = k % n
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        reverse(arr, 0, n - 1)
        reverse(arr, 0, k - 1)
        reverse(arr, k, n - 1)
        return arr
