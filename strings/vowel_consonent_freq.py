# LeetCode 3541. Find Most Frequent Vowel and Consonant
# Given a string s of lowercase English letters, find the vowel
# ('a', 'e', 'i', 'o', 'u') with the highest frequency and the
# consonant with the highest frequency. Return the sum of those
# two frequencies. If there are no vowels or no consonants, treat
# that frequency as 0.

# Approach 1 (frequency map):
# 1. Count how many times each character appears in s.
# 2. Walk the counts. If the character is a vowel, track the max
#    vowel count; otherwise track the max consonant count.
# 3. Return max vowel frequency + max consonant frequency.

# Time Complexity: O(n) - n is the length of s. We scan s once to
# count, then scan the unique letters (at most 26).
# Space Complexity: O(1) - the dictionary stores at most 26 letters,
# which does not grow with n.


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_cv = 0
        max_cc = 0
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        for k, v in d.items():
            if k in vowels:
                if v > max_cv:
                    max_cv = v
            else:
                if v > max_cc:
                    max_cc = v
        return max_cv + max_cc


# Approach 2 (fixed-size ASCII count array):
# Letters are ASCII, so there are only 128 possible characters.
# 1. Make a list of 128 zeros.
# 2. For each character in s, add 1 at index ord(i).
# 3. Walk the 128 slots. If that character is a vowel, track the max
#    vowel count; otherwise track the max consonant count.
# Same counting idea as the dict, but lookup is a list index (no hashing).

# Time Complexity: O(n) - n is the length of s. We scan s once to
# count, then scan a fixed 128 slots.
# Space Complexity: O(1) - the list size is always 26, independent of n.


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_cv = 0
        max_cc = 0
        freq = [0] * 26
        for i in s:
            freq[ord(i)] += 1
        for i in range(26):
            v = freq[i]
            if chr(i) in vowels:
                if v > max_cv:
                    max_cv = v
            else:
                if v > max_cc:
                    max_cc = v
        return max_cv + max_cc

