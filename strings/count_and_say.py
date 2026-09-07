# LeetCode 38. Count and Say
# The count-and-say sequence is defined by:
# countAndSay(1) = "1"
# countAndSay(n) is how you "say" countAndSay(n-1): for each run of
# the same digit, write the run length then the digit, and concatenate.

# Approach (recursion + consecutive count):
# 1. Base case: n == 1 returns "1".
# 2. Recurse to get countAndSay(n - 1).
# 3. Walk that string and count consecutive equal digits.
# 4. When a run ends, append count then that digit to the answer.

# Time Complexity: O(n * m) - n recursive steps, each scans a string
# whose length is at most m (the length of the nth term).
# Space Complexity: O(n + m) - recursion depth is n, and we store
# the answer string of length m.

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ""
        if n == 1:
            return "1"
        return self.count(self.countAndSay(n - 1), ans)

    def count(self, s, ans):
        i = 0
        count = 1
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            else:
                ans += str(count) + s[i]
                i += 1
                count = 1
        return ans
