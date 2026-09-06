# LeetCode 49. Group Anagrams
# Given an array of strings strs, group the anagrams together.
# Return the groups in any order.
# An anagram is a word formed by rearranging the letters of another
# word, using all the original letters exactly once.

# Approach (hashmap keyed by sorted letters):
# 1. Two words are anagrams if they become the same string after
#    sorting their characters.
# 2. For each word, sort it and use that as a dict key.
# 3. Append the original word to the list for that key.
# 4. Return all the lists stored in the dict.

# Time Complexity: O(n * k log k) - n is the number of strings,
# k is the max string length. We sort each string once.
# Space Complexity: O(n * k) - we store every original string in
# the dict (the keys also take O(n * k) in the worst case).

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in d:
                d[key] = []
            d[key].append(s)
        for items in d:
            ans.append(d[items])
        return ans


# Approach (hashmap keyed by character counts):
# 1. For each word, count how many times each letter appears.
# 2. Turn that count map into one string (letter + count, letters
#    in sorted order) so "eat" and "tea" get the same key.
# 3. Append the original word to the list for that key.
# 4. Return all the lists stored in the dict.

# Time Complexity: O(n * k) - n strings, k max length. Counting
# letters is O(k). Sorting the unique keys in the count map is
# O(1) for a fixed alphabet (at most 26 letters).
# Space Complexity: O(n * k) - we store every original string in
# the dict (the keys also take O(n * k) in the worst case).


class SolutionCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for s in strs:
            out = ""
            d2 = {}
            for i in s:
                if i not in d2:
                    d2[i] = 0
                d2[i] += 1
            for k in sorted(d2):
                out += k
                out += str(d2[k])
            if out not in d:
                d[out] = []
            d[out].append(s)
        for items in d:
            ans.append(d[items])
        return ans
