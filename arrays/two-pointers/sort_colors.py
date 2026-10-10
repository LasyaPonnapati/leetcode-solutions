# LeetCode 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so same colors sit together, in the order red, white, blue.
# 0 means red, 1 means white, and 2 means blue. Do not use the library sort function.

# Approach (two pointers, three passes from the right):
# 1. x is the next spot on the right for the color we are gathering. y walks from right to left.
# 2. First pass: when y sees a 2, swap it with x and move x one step left. All 2s end up at the back.
# 3. y has walked off the left end, so set y back to x and do the same for 1s. Those 1s land just left of the 2s.
# 4. Set y back to x again and do the same for 0s. The 0s fill the front.

# Time Complexity: O(n) - three passes, and each pass looks at each index at most once, so the work is about 3n steps.
# Space Complexity: O(1) - the array is sorted in place; only a few variables are used.

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        x, y = n - 1, n - 1
        x, y = self.gather_color(nums, x, y, 2)
        x, y = self.gather_color(nums, x, y, 1)
        self.gather_color(nums, x, y, 0)

    def gather_color(self, nums: list[int], x: int, y: int, color: int) -> tuple[int, int]:
        while y >= 0:
            if nums[y] == color:
                nums[x], nums[y] = nums[y], nums[x]
                x -= 1
            y -= 1
        y = x
        return x, y
