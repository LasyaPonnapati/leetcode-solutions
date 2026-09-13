# LeetCode 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd
# indices together followed by the nodes with even indices, and return
# the reordered list. The first node is considered odd, the second even,
# and so on. Relative order inside the odd group and inside the even
# group should stay the same.

# Approach (two pointers: one on odd nodes, one on even nodes):
# 1. If the list is empty or has one node, nothing to reorder. Return head.
# 2. Keep ocurr on the current odd node, ecurr on the current even node,
#    and estart on the first even node (so we can attach the even chain
#    after the last odd node at the end).
# 3. While both the current odd and even nodes still have a next node,
#    skip ahead by two: the next odd is ocurr.next.next, the next even
#    is ecurr.next.next. Relink, then move both pointers forward.
# 4. After the loop, the odd chain is done. Point the last odd node at
#    estart so the even chain follows it.

# Time Complexity: O(n) - we visit each node a constant number of times
# while walking the list once and rewriting next pointers.
# Space Complexity: O(1) - only a few pointers; we reorder links in place.


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        ocurr = head
        ecurr = head.next
        estart = head.next
        while ocurr.next is not None and ecurr.next is not None:
            onext = ocurr.next.next
            enext = ecurr.next.next
            ocurr.next = onext
            ecurr.next = enext
            ocurr = onext
            ecurr = enext
        ocurr.next = estart
        return head
