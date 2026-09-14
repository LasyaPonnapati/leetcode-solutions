# LeetCode 61. Rotate List
# Given the head of a linked list, rotate the list to the right by k
# places and return the new head.

# Approach (make the list circular, then break it at the new tail):
# 1. If the list is empty or has one node, rotation cannot change it.
# 2. Walk to the last node while counting length ln. After this, curr
#    is the tail.
# 3. Connect tail.next to head so the list becomes a circle.
# 4. k can be larger than ln, so the real rotation is k % ln. From the
#    tail, walk ln - (k % ln) steps. That lands on the new last node.
# 5. The node after that is the new head. Break the circle there.

# Time Complexity: O(n) - one pass to find the tail and length, then at
# most n more steps to reach the new tail.
# Space Complexity: O(1) - only a few pointers and counters; we reuse
# the existing nodes and change next links in place.


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        ln = 1
        while curr.next is not None:
            ln += 1
            curr = curr.next
        curr.next = head
        k = k % ln
        num = ln - k
        while num != 0:
            curr = curr.next
            num -= 1
        head = curr.next
        curr.next = None
        return head
