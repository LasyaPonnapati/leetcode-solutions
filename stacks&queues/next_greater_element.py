# Next Greater Element I
# LeetCode 496: nums1 is a subset of nums2 (both have distinct
# values). For each x in nums1, find the first number to the right
# of x in nums2 that is greater than x. If none exists, use -1.


# Approach 1: For each value in nums1, scan nums2 until that value
# is found, then keep scanning right for the first larger number.
#
# Time: O(n * m) — n = len(nums1), m = len(nums2). Each nums1 value
#       may scan all of nums2 to find it, then the rest for a greater.
# Space: O(n) — ans stores one result per nums1 value.


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums1)):
            j = 0
            while nums2[j] != nums1[i]:
                j += 1
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    ans.append(nums2[j])
                    break
                j += 1
            if j == len(nums2):
                ans.append(-1)
        return ans


# Approach 2: Walk nums2 right to left. The stack holds values to
# the right, decreasing from top to bottom, so the top is the next
# greater of the current value (or the stack is empty → -1). Then
# map each nums1 value to that answer.
#
# Time: O(n + m) — each nums2 value is pushed and popped at most
#       once, then we fill n answers from the map.
# Space: O(m) — the stack and the next-greater array are both size m.


class SolutionUsingStack:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = [0] * len(nums2)
        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            element = nums2[i]

            # If empty, no next greater element
            if not stack:
                stack.append(element)
                next_greater[i] = -1
                continue

            # If top of stack is greater, it is the next greater
            if stack[-1] > element:
                next_greater[i] = stack[-1]
                stack.append(element)
                continue

            # Remove all elements smaller than or equal to element
            while stack and stack[-1] <= element:
                stack.pop()

            if not stack:
                next_greater[i] = -1
            else:
                next_greater[i] = stack[-1]
            stack.append(element)

        index = {}
        for i in range(len(nums2)):
            index[nums2[i]] = i

        ans = []
        for x in nums1:
            ans.append(next_greater[index[x]])
        return ans
