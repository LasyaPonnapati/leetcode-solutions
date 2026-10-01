# LeetCode 145. Binary Tree Postorder Traversal
# Given the root of a binary tree, return the postorder traversal of its node values.
# Postorder visits nodes in this order: left subtree, right subtree, current node.

# Approach:
# 1. Start with an empty result list.
# 2. If the current node is None, there is nothing to visit, so return.
# 3. Visit the left subtree, then the right subtree.
# 4. Add the current value after both subtrees are done.
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
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        self.ans = []
        self._postorder(root)
        return self.ans

    def _postorder(self, root: TreeNode | None) -> None:
        if root is None:
            return
        self._postorder(root.left)
        self._postorder(root.right)
        self.ans.append(root.val)
