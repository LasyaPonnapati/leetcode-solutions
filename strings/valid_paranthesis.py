# LeetCode 921. Minimum Add to Make Parentheses Valid
# A parentheses string is valid if it is empty, is the concatenation
# of two valid strings, or is a valid string wrapped in a pair of
# parentheses. Given a string s of '(' and ')', return the minimum
# number of parentheses you must add to make s valid.

# Approach (stack):
# 1. Walk the string left to right.
# 2. Push each '(' onto a stack.
# 3. On ')', pop a matching '(' if the stack is non-empty; otherwise count one
#    extra ')' that needs a '(' added.
# 4. After the loop, every unmatched '(' on the stack needs a ')' added.
# 5. Return count of extra closes plus the number of leftover opens.

# Time Complexity: O(n) - we look at each character once.
# Space Complexity: O(n) - the stack can hold up to n opening brackets.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        count=0
        for s in s:
            if s=='(':
                stack.append(s)
            else:
                if stack:
                    stack.pop()
                else:
                    count+=1
        return count+len(stack)
        

# Approach (count unmatched opens and extra closes):
# 1. Walk the string left to right.
# 2. c1 = number of unmatched '(' so far.
# 3. If we see '(', increase c1.
# 4. If we see ')':
#    - if c1 > 0, this ')' matches one unmatched '(', so decrease c1
#    - else this ')' has no match, so we must add one '(' (ans += 1)
# 5. After the loop, every leftover unmatched '(' needs a ')' (ans += c1).

# Time Complexity: O(n) - we look at each character once.
# Space Complexity: O(1) - only a few counters, no extra data structures.

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c1 = 0
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == '(':
                c1 += 1
            else:
                if c1 > 0:
                    c1 -= 1
                else:
                    ans += 1
            i += 1
        ans += c1
        return ans
