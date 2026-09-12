# LeetCode 19. Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end
# of the list and return its head.

# Approach (count length, then unlink the node at index ln - n):
# 1. Walk the list once with temp to count how many nodes there are (ln).
# 2. If n equals ln, the node to remove is the head, so return head.next.
# 3. If n is 0, nothing needs to be removed, so return head as-is.
# 4. The node to delete is at index ln - n. Walk prev to the node just
#    before that index, then skip the next node with prev.next = prev.next.next.

# Time Complexity: O(n) - one pass to count length, one pass to reach
# the node before the one we delete (at most n nodes in total).
# Space Complexity: O(1) - only a few pointers and counters; we change
# links in place.


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        temp = head
        while temp is not None:
            ln += 1
            temp = temp.next
        if n == ln:
            head = head.next
            return head
        if n == 0:
            return head
        index = ln - n
        prev = head
        i = 0
        while i < index - 1:
            prev = prev.next
            i += 1
        prev.next = prev.next.next
        return head


# Approach 2 (fast is n nodes ahead of slow, then walk together):
# 1. Start both pointers at head. Move fast n steps so it is n nodes ahead.
# 2. If fast is then None, n equals the list length, so the head is the
#    node to remove. Return head.next.
# 3. Otherwise move both until fast is on the last node. slow is then
#    just before the node to delete.
# 4. Unlink with slow.next = slow.next.next and return head.

# Time Complexity: O(n) - each node is visited at most once.
# Space Complexity: O(1) - only two pointers; we change links in place.


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        while n != 0:
            fast = fast.next
            n -= 1
        if fast is None:
            return head.next
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
