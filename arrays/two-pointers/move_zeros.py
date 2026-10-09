# LeetCode 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements. You must do this in-place.

# Approach (two-pointer):
# 1. x is the write pointer for the next non-zero position; y is the read pointer.
# 2. Move y from left to right across the array.
# 3. When nums[y] is not 0, swap nums[x] and nums[y], then move x forward.
# 4. Always move y forward. Non-zero elements shift left in order; zeros end up at the back.

# Time Complexity: O(n) - y visits each element once, and x moves at most n times.
# Space Complexity: O(1) - only two pointer variables are used.

class Solution:
    def moveZeroes(self, nums:list[int]) -> None:
        x, y = 0, 0
        while y < len(nums):
            if nums[y] != 0:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
            y += 1
