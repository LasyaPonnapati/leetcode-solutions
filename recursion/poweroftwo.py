# LeetCode 231. Power of Two
# Power of Two
# Given an integer n, return True if n is a power of two, otherwise False.
# A number is a power of two if it equals 2^k for some integer k >= 0
# (examples: 1, 2, 4, 8, 16, ...).

# Approach:
# 1. If n is less than or equal to 0, it cannot be a power of two.
# 2. Base case: if n is 1, return True (because 2^0 = 1).
# 3. If n is odd, it cannot be a power of two, so return False.
# 4. Otherwise n is even: check whether n / 2 is a power of two
#    by calling the same function on n // 2.

# Time Complexity: O(log n) - we divide n by 2 on every call until we
# reach 1 or find an odd number.
# Space Complexity: O(log n) - the call stack has one frame per division by 2.


def is_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)
