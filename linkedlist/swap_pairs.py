# LeetCode 24. Swap Nodes in Pairs
# Given the head of a linked list, swap every two adjacent nodes and
# return the new head. You must not change node values, only the links.

# Approach (swap each pair in place with prev / curr / next_node):
# 1. If the list is empty or has one node, there is no pair to swap.
# 2. After the first swap, the original second node becomes the new head,
#    so save that before the loop.
# 3. For each pair, next_node is curr's neighbor. Point curr past the
#    pair, then point next_node back at curr so the two nodes swap.
# 4. If a previous pair exists, connect it to next_node (the new front
#    of this pair). Then prev becomes curr, and curr moves to the start
#    of the next pair.

# Time Complexity: O(n) - we walk the list once and swap each pair with
# a constant amount of pointer work.
# Space Complexity: O(1) - only a few pointers; we rewrite next links
# in place and do not use extra list storage.


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        head = head.next
        prev = None
        while curr is not None and curr.next is not None:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr
            if prev is not None:
                prev.next = next_node
            prev = curr
            curr = curr.next
        return head
