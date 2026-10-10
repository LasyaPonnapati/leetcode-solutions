# LeetCode 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of
# the squares of each number, also sorted in non-decreasing order.

# Approach (two pointers):
# 1. The array is already sorted, so the biggest squares come from the ends:
#    a large negative on the left, or a large positive on the right.
# 2. x starts at the left end, y starts at the right end.
# 3. Compare the squares of nums[x] and nums[y]. Put the larger square at the next
#    open spot from the back of the result.
# 4. If nums[x] squared is bigger, move x right. Otherwise move y left.
# 5. Fill the result from the back until x and y meet.

# Time Complexity: O(n) - each element is looked at once and written into the result once.
# Space Complexity: O(n) - the result array holds n squares. The extra pointers use constant space.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        x, y, write = 0, n - 1, n - 1

        while x <= y:
            left_square = nums[x] * nums[x]
            right_square = nums[y] * nums[y]
            if left_square > right_square:
                result[write] = left_square
                x += 1
            else:
                result[write] = right_square
                y -= 1
            write -= 1

        return result
