# LeetCode 394. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is k[encoded_string]: the substring inside the
# brackets is repeated exactly k times. k is a positive integer.
# The input is always valid (brackets match). Digits appear only as
# the repeat count k, never as part of the original letters.

# Approach (two stacks):
# 1. s1 holds repeat counts. s2 holds letters and '['.
# 2. Digit: fold it into num (12 is 1 then 2, not just 2).
# 3. '[': push num onto s1, reset num, push '[' onto s2.
# 4. Letter: push it onto s2.
# 5. ']': pop from s2 until '[', rebuild that inner string in
#    order, pop k from s1, push (inner * k) back onto s2.
# 6. What is left on s2 at the end is the decoded string.

# Time Complexity: O(m) - m is the length of the decoded string.
# We scan s once and build the output by repeating inner pieces.
# Space Complexity: O(m) - both stacks hold pieces of the result.

class Solution:
    def decodeString(self, s: str) -> str:
        s1 = []
        s2 = []
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            elif i == "[" or i.isalpha():
                if i == "[":
                    s1.append(num)
                    num = 0
                s2.append(i)
            else:
                temp = ""
                while s2 and s2[-1] != "[":
                    temp = s2.pop() + temp
                if s2:
                    s2.pop()
                k = s1.pop()
                s2.append(temp * k)
        return "".join(s2)
