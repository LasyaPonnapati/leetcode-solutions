# LeetCode 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums2 into nums1 as one sorted array in-place. nums1 has length m + n.

# Approach 1 (extra array):
# 1. Copy the first m elements of nums1 into an extra array n1.
# 2. Use a write pointer in nums1 starting at 0.
# 3. x points to n1, y points to nums2. Compare n1[x] and nums2[y], place the smaller in nums1.
# 4. Move x if n1's element was used, move y if nums2's element was used. Always move the write pointer.
# 5. When one array ends, copy the remaining elements from the other array.

# Time Complexity: O(m + n) - each element is compared and written once.
# Space Complexity: O(m) - extra array n1 stores the original m elements from nums1.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        n1 = nums1[:m]
        x, y, write = 0, 0, 0

        while x < m and y < n:
            if n1[x] <= nums2[y]:
                nums1[write] = n1[x]
                x += 1
            else:
                nums1[write] = nums2[y]
                y += 1
            write += 1

        while x < m:
            nums1[write] = n1[x]
            x += 1
            write += 1

        while y < n:
            nums1[write] = nums2[y]
            y += 1
            write += 1

# Approach 2 (merge from the back):
# 1. nums1 has n empty slots at the end, so start writing at the last index.
# 2. x points at the last real value in nums1, y points at the last value in nums2.
# 3. Compare those two values and place the larger one at the write index.
# 4. Move x if nums1's element was used, move y if nums2's element was used. Always move the write pointer left.
# 5. If nums2 runs out first, the leftover nums1 values are already in the right places.
# 6. If nums1 runs out first, copy the leftover nums2 values into the front.

# Time Complexity: O(m + n) - each element is written once.
# Space Complexity: O(1) - only the pointer variables are used.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        x, y, write = m - 1, n - 1, m + n - 1

        while x >= 0 and y >= 0:
            if nums1[x] >= nums2[y]:
                nums1[write] = nums1[x]
                x -= 1
            else:
                nums1[write] = nums2[y]
                y -= 1
            write -= 1

        while y >= 0:
            nums1[write] = nums2[y]
            y -= 1
            write -= 1
