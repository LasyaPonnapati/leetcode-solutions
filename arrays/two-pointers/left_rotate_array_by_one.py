# Left Rotate an Array by One
# Given an array arr, move every element one place to the left.
# The first element wraps around and becomes the last element.
# Example: [1, 2, 3, 4, 5] becomes [2, 3, 4, 5, 1].

# Approach 1 (slicing):
# 1. arr[1:] is every element after the first one.
# 2. arr[:1] is a one-element list holding the first element.
# 3. Join them so the first element ends up at the back.
# 4. This returns a new list. The original arr is unchanged.

# Time Complexity: O(n) - slicing and joining copy every element once.
# Space Complexity: O(n) - the new list stores all n elements.

class Solution:
    def leftRotate(self, arr: list[int]) -> list[int]:
        return arr[1:] + arr[:1]

# Approach 2 (hold and shift):
# 1. Save arr[0] in hold so it is not lost when the shift starts.
# 2. Move each next element one place to the left: arr[i] = arr[i + 1].
# 3. After the loop, the last slot is free of its old value (it was copied left).
# 4. Put hold into the last position.

# Time Complexity: O(n) - the loop visits each element after the first one once.
# Space Complexity: O(1) - only hold is extra; the array is changed in place.

class Solution:
    def leftRotate(self, arr: list[int]) -> None:
        hold = arr[0]
        for i in range(len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = hold
