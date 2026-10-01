# LeetCode 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its node values.
# Level order visits nodes from left to right, one level at a time.
# The answer is a list of lists: one inner list per level.


from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Queue approach:
    # 1. If the root is None, return an empty list.
    # 2. Use a queue. A queue gives nodes back in the order they were added (first in, first out).
    # 3. Start by putting the root in the queue.
    # 4. While the queue is not empty, the nodes currently in it are exactly one level.
    # 5. Take each of those nodes out, add its value to this level's list,
    #    and put its left child, then its right child, at the back of the queue.
    # 6. Those children become the next level. Repeat until the queue is empty.
    #
    # Time Complexity: O(n) - every node is added to the queue once and removed once.
    # Space Complexity: O(n) - the result list stores every node value,
    # and the queue holds the widest level, which can be up to about n/2 nodes.
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []

        ans = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(level)

        return ans

    # Recursive approach:
    # 1. Start with an empty result list. Each inner list will hold one level.
    # 2. If the current node is None, there is nothing to visit, so return.
    # 3. Pass the level number along with the node. The root is level 0.
    # 4. When we first reach a level, create a new inner list for it.
    # 5. Add the current value to that level's list.
    # 6. Then visit the left child and the right child at the next level.
    #
    # Time Complexity: O(n) - every node is visited once.
    # Space Complexity: O(n) - the result list stores every node value,
    # and the call stack uses extra space equal to the height of the tree.
    def levelOrderRecursive(self, root: TreeNode | None) -> list[list[int]]:
        self.ans = []
        self._levelorder(root, 0)
        return self.ans

    def _levelorder(self, root: TreeNode | None, level: int) -> None:
        if root is None:
            return
        if len(self.ans) == level:
            self.ans.append([])
        self.ans[level].append(root.val)
        self._levelorder(root.left, level + 1)
        self._levelorder(root.right, level + 1)
