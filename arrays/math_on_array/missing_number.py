# LeetCode 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Approach 1 (brute force):
# 1. The array length is n, so the full range is 0, 1, 2, ..., n.
# 2. Check each number in that range to see if it is present in nums.
# 3. The number that is not present is the answer.

# Time Complexity: O(n^2) - there are n + 1 numbers to check, and each "in" scan
# looks through up to n elements.
# Space Complexity: O(1) - only the loop variable is used.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n + 1):
            if i not in nums:
                return i

# Approach 2 (sort):
# 1. Sort the array so the numbers are in ascending order.
# 2. The first element should be 0. If it is not, 0 is missing.
# 3. Each next element should be exactly 1 bigger than the one before it.
# 4. The first gap is the missing number.
# 5. If there is no gap, every number from 0 to n - 1 is present, so n is missing.

# Time Complexity: O(n log n) - sorting dominates; the gap scan is O(n).
# Space Complexity: O(n) - Python's sort uses extra memory proportional to the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                return nums[i - 1] + 1
        return len(nums)

# Approach 3 (sum):
# 1. The full range [0, n] should contain numbers 0 to n. Here, one number is missing.
# 2. Compute range_sum = sum of 0 to n-1 using sum(range(n)).
# 3. Compute list_sum by adding all numbers in nums.
# 4. The difference list_sum - range_sum gives the missing number.
# 5. If the difference is 0, every number from 0 to n-1 is present, so the missing number is n.

# Time Complexity: O(n) - one pass to compute list_sum; range_sum is computed in O(n).
# Space Complexity: O(1) - only a few variables are used.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = sum(range(n))
        list_sum = 0
        for num in nums:
            list_sum += num
        difference = list_sum - range_sum
        if difference == 0:
            return n
        return difference
