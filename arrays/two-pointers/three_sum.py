# LeetCode 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i, j, and k are different indexes and nums[i] + nums[j] + nums[k] == 0.
# The answer must not contain the same triplet more than once.

# Approach 1 (brute force with a set):
# 1. Pick every group of three different indexes with three nested loops.
# 2. If the three numbers add up to 0, sort those three values and add them to a set.
# 3. A set keeps each triplet once. Sorting the three values first makes
#    [-1, 0, 1] and [0, 1, -1] the same triplet.
# 4. Turn the set back into a list of lists before returning.

# Time Complexity: O(n^3) - three nested loops each walk the array, so every trio of indexes is checked once.
# Sorting three numbers and adding them to the set takes constant time for each trio.
# Space Complexity: O(m) - the set stores one copy of each unique triplet, and m is how many unique triplets are found.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.add(tuple(sorted((nums[i], nums[j], nums[k]))))

        return [list(triplet) for triplet in result]

# Approach 2 (two pointers on the right, stored in a set):
# 1. Sort nums so the two-pointer scan can move toward the target sum.
# 2. Fix one number, nums[i]. The other two numbers must add up to -nums[i].
# 3. Put x just to the right of i and y at the end. Only indexes after i are used.
# 4. If nums[x] + nums[y] equals the target, save the triplet in a set and move both pointers.
#    Keep going so later pairs for this same nums[i] are also found.
# 5. If the sum is smaller than the target, move x right to a larger value.
# 6. If the sum is larger than the target, move y left to a smaller value.
# 7. The set keeps each triplet once. Turn it back into a list of lists before returning.

# Time Complexity: O(n^2) - sorting is O(n log n). For each of the n starting numbers, x and y only move toward each other, so that scan is O(n).
# Space Complexity: O(m) extra besides the answer built from the set - m is how many unique triplets are stored. Sorting uses some extra memory in Python.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = set()

        for i in range(n):
            target = -nums[i]
            x = i + 1
            y = n - 1
            while x < y:
                current_sum = nums[x] + nums[y]
                if current_sum == target:
                    result.add((nums[i], nums[x], nums[y]))
                    x += 1
                    y -= 1
                elif current_sum < target:
                    x += 1
                else:
                    y -= 1

        return [list(triplet) for triplet in result]
