# LeetCode 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its node values.
# Inorder visits nodes in this order: left subtree, current node, right subtree.

# Approach:
# 1. Start with an empty result list for this call.
# 2. If the current node is None, there is nothing to visit, so return.
# 3. If the node is a leaf (no left child and no right child), add its value and return.
# 4. Otherwise visit the left subtree, add the current value, then visit the right subtree.
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
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.ans = []
        self._inorder(root)
        return self.ans

    def _inorder(self, root: TreeNode | None) -> None:
        if root is None:
            return
        self._inorder(root.left)
        self.ans.append(root.val)
        self._inorder(root.right)
