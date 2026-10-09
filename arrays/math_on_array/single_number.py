# LeetCode 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.

# Approach 1 (brute force):
# 1. Pick each number in the array.
# 2. Scan the whole array and count how many times that number appears.
# 3. If the count is 1, that number is the answer.

# Time Complexity: O(n^2) - for each of the n numbers, we scan all n elements again.
# Space Complexity: O(1) - only the count is stored.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]

# Approach 2 (hash map):
# 1. Count how many times each number appears using a dictionary.
# 2. Scan the dictionary and return the number whose count is 1.

# Time Complexity: O(n) - one pass to count, one pass to find the single number.
# Space Complexity: O(n) - the dictionary can store up to n different keys.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            if count == 1:
                return num

# Approach 3 (sort):
# 1. Sort the array so equal numbers become neighbors.
# 2. Check pairs starting at index 0: nums[0] with nums[1], nums[2] with nums[3], and so on.
# 3. If a number has no matching neighbor, or it is the last element alone, it is the answer.

# Time Complexity: O(n log n) - sorting dominates; the pair scan is O(n).
# Space Complexity: O(1) - sorting is done in-place on nums.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i + 1 >= len(nums) or nums[i] != nums[i + 1]:
                return nums[i]

# Approach 4 (XOR):
# 1. XOR all numbers in the array.
# 2. Pairs of equal numbers cancel out (a ^ a = 0).
# 3. The remaining result is the number that appeared only once.

# Time Complexity: O(n) - one pass through the array.
# Space Complexity: O(1) - only the result variable is used.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
