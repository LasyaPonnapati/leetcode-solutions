# LeetCode 100. Same Tree
# Given the roots of two binary trees, p and q, return true if they are the same tree.
# Two trees are the same when they have the same shape and the same node values.

# Approach:
# 1. Compare the current node in p with the current node in q.
# 2. If both nodes are None, this pair matches, so return True.
# 3. If only one node is None, the trees differ, so return False.
# 4. If both nodes exist, their values must be equal.
# 5. Then the left subtrees must be the same, and the right subtrees must be the same.
# 6. Return True only when both sides match.

# Time Complexity: O(n) - every node in the smaller tree is visited once, and we stop early on a mismatch.
# In the worst case both trees are the same and every node is compared.
# Space Complexity: O(h) - the call stack goes as deep as the height of the taller tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
