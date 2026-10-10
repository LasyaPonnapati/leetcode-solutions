# LeetCode 1. Two Sum
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Approach 1 (dictionary):
# 1. seen maps a number we have already visited to its index.
# 2. Walk the array once. For each num, the other number we need is target - num.
# 3. If that complement is already in seen, return its index and the current index.
# 4. Otherwise store num with its index, then move on.
# 5. Check before storing so the same element is not used twice.

# Time Complexity: O(n) - one pass over the array; each dictionary lookup and insert is O(1) on average.
# Space Complexity: O(n) - seen stores up to n numbers and their indexes.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
        return []

# Approach 2 (two pointers):
# 1. Pair each value with its original index, then sort those pairs by value.
# 2. Put x at the start and y at the end of the sorted pairs.
# 3. If the two values add up to target, return their original indexes.
# 4. If the sum is smaller than target, move x forward to a larger value.
# 5. If the sum is larger than target, move y backward to a smaller value.
# 6. Stop when a pair is found or x meets y.

# Time Complexity: O(n log n) - sorting the pairs takes O(n log n), and the two-pointer scan is O(n).
# Space Complexity: O(n) - the sorted list stores a value-index pair for every element.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        x, y = 0, len(indexed_nums) - 1

        while x < y:
            current_sum = indexed_nums[x][0] + indexed_nums[y][0]
            if current_sum == target:
                return [indexed_nums[x][1], indexed_nums[y][1]]
            elif current_sum < target:
                x += 1
            else:
                y -= 1

        return []
