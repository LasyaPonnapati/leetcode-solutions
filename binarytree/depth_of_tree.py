# LeetCode 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth (also called its height).
# The depth of a tree is the number of nodes on the longest path from the root down to a leaf.
# An empty tree has depth 0. A tree with only the root has depth 1.

# Approach:
# 1. If the current node is None, this branch has no nodes, so its depth is 0.
# 2. Ask the left subtree for its depth, and ask the right subtree for its depth.
# 3. The deeper of those two answers is the taller child.
# 4. Add 1 for the current node, then return that number.
# 5. The answer at the root is the depth of the whole tree.

# Time Complexity: O(n) - every node is visited once.
# Space Complexity: O(h) - the call stack goes as deep as the height of the tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
