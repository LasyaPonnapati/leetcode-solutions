# LeetCode 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is a sequence of non-space characters. Words are separated
# by at least one space. Return a string of the words in reverse
# order, concatenated by a single space. Extra spaces should be
# removed (leading, trailing, and extra spaces between words).

# Approach (split, reverse, join):
# 1. s.split() with no argument splits on any whitespace and drops
#    extra spaces (leading, trailing, and between words).
#    Example: "  hello   world  " -> ["hello", "world"].
# 2. Reverse the word list with ans[::-1].
# 3. Join the reversed words with a single space.

# Time Complexity: O(n) - n is the length of s. split walks the
# string once, reversing the word list is O(k) (k <= n), and join
# builds the result string once.
# Space Complexity: O(n) - the word list, the reversed copy, and
# the output string.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


# Approach (reverse whole string, then reverse each word):
# 1. Turn s into a list of characters (Python strings cannot be
#    edited in place).
# 2. Reverse the whole list. Words are now in reverse order, but
#    each word's letters are backwards.
#    "hello world" -> "dlrow olleh"
# 3. Walk with two pointers: i reads, write copies.
#    Skip extra spaces. Copy one word, then reverse that word so
#    its letters face forward again.
# 4. Put a single space between words. Join the kept characters.

# Time Complexity: O(n) - n is the length of s. We scan each
# character a constant number of times and reverse each word once.
# Space Complexity: O(n) - the character list. Extra space cannot
# be O(1) in Python because strings are immutable.

class SolutionInPlace:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        n = len(chars)
        self._reverse(chars, 0, n - 1)

        write = 0
        i = 0
        while i < n:
            while i < n and chars[i] == " ":
                i += 1
            if i == n:
                break

            if write != 0:
                chars[write] = " "
                write += 1

            word_start = write
            while i < n and chars[i] != " ":
                chars[write] = chars[i]
                write += 1
                i += 1
            self._reverse(chars, word_start, write - 1)

        return "".join(chars[:write])

    def _reverse(self, chars, left, right):
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
