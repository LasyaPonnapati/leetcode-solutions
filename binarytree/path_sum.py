# LeetCode 112. Path Sum
# Given the root of a binary tree and an integer targetSum, return true if the tree
# has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Approach:
# 1. If the current node is None, this path does not exist, so return False.
# 2. Subtract the current node's value from the remaining sum.
# 3. If the node is a leaf (no left child and no right child), the path is complete.
#    Return True only when the remaining sum is 0.
# 4. Otherwise, check the left child and the right child with the new remaining sum.
# 5. Return True if either side finds a matching path.

# Time Complexity: O(n) - in the worst case every node is visited once.
# Space Complexity: O(h) - the call stack goes as deep as the height of the tree.
# A balanced tree uses about log n stack frames. A skewed tree uses n stack frames.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        remaining = targetSum - root.val
        if root.left is None and root.right is None:
            return remaining == 0
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)
