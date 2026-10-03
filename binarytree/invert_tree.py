# LeetCode 226. Invert Binary Tree
# Given the root of a binary tree, invert the tree and return its root.
# Inverting means every node's left child and right child swap places.

# Approach:
# 1. If the current node is None, there is nothing to invert, so return None.
# 2. Swap the node's left child and right child.
# 3. Invert the new left subtree, then invert the new right subtree.
# 4. Return the current node. The root of the whole tree is the answer.

# Time Complexity: O(n) - every node is visited once.
# Space Complexity: O(h) - the call stack goes as deep as the height of the tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
