# LeetCode 509. Fibonacci Number
# Fibonacci Number
# Given n, return the nth Fibonacci number.
# F(0) = 0, F(1) = 1, and F(n) = F(n - 1) + F(n - 2) for n > 1.

# Approach:
# 1. Base cases: if n is 0, return 0; if n is 1, return 1.
# 2. Recursive case: return fibonacci(n - 1) + fibonacci(n - 2).
# 3. The two smaller answers are added to get the current number.

# Time Complexity: O(2^n) - each call splits into two more calls, so the
# number of calls grows exponentially with n.
# Space Complexity: O(n) - the deepest path of the recursion is n frames.


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
