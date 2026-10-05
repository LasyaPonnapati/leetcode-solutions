# LeetCode 110. Balanced Binary Tree
# Given the root of a binary tree, return true if the tree is height-balanced.
# A tree is height-balanced when, for every node, the height of the left subtree
# and the height of the right subtree differ by at most 1.
# An empty tree is balanced. Its height is 0.

# Approach:
# 1. Walk the tree once. For each node, find the height of the left subtree
#    and the height of the right subtree.
# 2. If either subtree is already unbalanced, stop and report that.
# 3. If the two heights differ by more than 1, this node is unbalanced, so stop.
# 4. Otherwise this node is balanced. Its height is 1 plus the taller child.
# 5. Use -1 as the signal that a subtree is unbalanced.
#    A real height is always 0 or more, so -1 cannot be confused with a height.
# 6. The whole tree is balanced only when the walk from the root does not return -1.

# Time Complexity: O(n) - every node is visited once.
# Space Complexity: O(h) - the call stack goes as deep as the height of the tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return self.height(root) != -1

    def height(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        left = self.height(node.left)
        if left == -1:
            return -1
        right = self.height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
