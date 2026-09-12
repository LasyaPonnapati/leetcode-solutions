# LeetCode 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all nodes
# whose value equals val, and return the new head.

# Approach (skip leading matches, then unlink streaks):
# 1. While the head itself equals val, move head forward so those nodes
#    are dropped.
# 2. Walk the rest with prev (last kept node) and curr.
# 3. When curr equals val, skip any following nodes that also equal val,
#    then set prev.next past that whole streak so they are unlinked.
# 4. Move prev and curr forward and keep going until the list ends.

# Time Complexity: O(n) - each node is visited a constant number of times.
# Space Complexity: O(1) - only a few pointers; we change links in place.


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        prev = None
        curr = head
        while curr is not None:
            if curr.val == val:
                while curr.next is not None and curr.next.val == val:
                    curr = curr.next
                prev.next = curr.next
            prev = curr
            curr = curr.next
        return head
