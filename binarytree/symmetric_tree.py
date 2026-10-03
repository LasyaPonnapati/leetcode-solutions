# LeetCode 101. Symmetric Tree
# Given the root of a binary tree, return true if the tree is symmetric around its center.
# A tree is symmetric when the left subtree is a mirror of the right subtree.

# Approach:
# 1. Compare two nodes that should mirror each other. Start with the root's left and right children.
# 2. If both nodes are None, that pair matches, so return True.
# 3. If only one node is None, the sides do not match, so return False.
# 4. If both nodes exist, their values must be equal.
# 5. Then check the outer pair (left's left with right's right)
#    and the inner pair (left's right with right's left).
# 6. The tree is symmetric only when both of those pairs are mirrors.

# Time Complexity: O(n) - every node is compared once.
# Space Complexity: O(h) - the call stack goes as deep as the height of the tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        outer = self.is_mirror(left.left, right.right)
        inner = self.is_mirror(left.right, right.left)
        return outer and inner
