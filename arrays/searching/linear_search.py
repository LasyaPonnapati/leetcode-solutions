# LeetCode: N/A — Linear Search (foundational DSA practice)
# Linear Search
# Given an array arr and a target value, find the target by checking each element
# from left to right. Return the element and its index when found.

# Approach:
# 1. Loop through the array once from the start.
# 2. When the current element equals target, stop and return the element and its index.

# Time Complexity: O(n) - in the worst case we look at every element once.
# Space Complexity: O(1) - we only use a loop index, no extra data structures.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return arr[i], i
    return None
