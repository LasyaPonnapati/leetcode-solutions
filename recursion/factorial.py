# LeetCode: N/A — Factorial (foundational DSA / recursion practice)
# Factorial of n
# Given a non-negative integer n, return n! (n factorial).
# n! = n * (n - 1) * (n - 2) * ... * 1, and 0! is defined as 1.

# Approach:
# 1. Base case: if n is 0 or 1, return 1.
# 2. Recursive case: n! = n * factorial(n - 1).
# 3. Each call waits for the smaller factorial, then multiplies by n.

# Time Complexity: O(n) - we make one recursive call for each value from n down to 1.
# Space Complexity: O(n) - the call stack holds n frames until we hit the base case.


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)
