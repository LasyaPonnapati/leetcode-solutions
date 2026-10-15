# LeetCode 739. Daily Temperatures
# Given an array of integers temperatures, return an array answer such that
# answer[i] is the number of days you have to wait after the ith day to get a
# warmer temperature. If there is no future day for which this is possible,
# keep answer[i] == 0.

# Approach:
# 1. Scan temperatures from right to left with a stack of indices.
# 2. The stack holds indices of days that are still waiting for a warmer day.
# 3. For each day i, compare with the top of the stack; pop while the top day
#    is not warmer than day i.
# 4. If the stack is empty after that, no warmer day exists (answer[i] = 0).
# 5. Otherwise the top index is the next warmer day (answer[i] = index - i).
# 6. Push index i onto the stack and continue.

# Time Complexity: O(n) - each index is pushed and popped at most once.
# Space Complexity: O(n) - the stack can hold up to n indices in the worst case.


class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        ans = [0] * len(t)
        s = []
        for i in range(len(t) - 1, -1, -1):
            if not s:
                ans[i] = 0
            else:
                if t[s[-1]] > t[i]:
                    ans[i] = s[-1] - i
                else:
                    while t[s[-1]] < t[i] and not s:
                        s.pop()
                    if not s:
                        ans[i] = 0
                    else:
                        ans[i] = s[-1] - i
            s.append(i)
        return ans
