# LeetCode 144. Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its node values.
# Preorder visits nodes in this order: current node, left subtree, right subtree.

# Approach:
# 1. Start with an empty result list.
# 2. If the current node is None, there is nothing to visit, so return.
# 3. Add the current value first.
# 4. Then visit the left subtree, then the right subtree.
# 5. Return the result list after the whole tree has been visited.

# Time Complexity: O(n) - every node is visited once.
# Space Complexity: O(n) - the result list stores every node value,
# and the call stack uses extra space equal to the height of the tree.


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.ans = []
        self._preorder(root)
        return self.ans

    def _preorder(self, root: TreeNode | None) -> None:
        if root is None:
            return
        self.ans.append(root.val)
        self._preorder(root.left)
        self._preorder(root.right)
