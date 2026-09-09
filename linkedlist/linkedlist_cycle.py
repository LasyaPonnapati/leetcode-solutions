# LeetCode 141. Linked List Cycle
# Given the head of a linked list, return true if there is a cycle, else false.
# A cycle means some node can be reached again by following next pointers.

# Approach (set of visited nodes):
# 1. Walk the list one node at a time.
# 2. If the current node is already in the set, we have seen it before → cycle.
# 3. Otherwise add it to the set and move to next.
# 4. If we reach None, the list ended → no cycle.

# Time Complexity: O(n) - we visit each node at most once.
# Space Complexity: O(n) - the set can store every node if there is no cycle.


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        curr = head
        while curr is not None:
            if curr in s:
                return True
            s.add(curr)
            curr = curr.next
        return False


# Approach 2 (tortoise and hare / slow and fast pointers):
# 1. Start slow and fast at head.
# 2. Move slow 1 step and fast 2 steps each round.
# 3. If they ever land on the same node, there is a cycle.
# 4. If fast reaches the end (None), there is no cycle.

# Time Complexity: O(n) - fast walks the list; in a cycle they meet within O(n) steps.
# Space Complexity: O(1) - only two pointers, no set.


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False

        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

