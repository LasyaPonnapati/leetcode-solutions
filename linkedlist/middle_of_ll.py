# LeetCode 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second middle node.

# Approach 1 (count, then walk to the middle index):
# 1. Walk the list once and count how many nodes there are.
# 2. The middle index is count // 2 (this picks the second middle when n is even).
# 3. Walk from head again until that index and return that node.

# Time Complexity: O(n) - we walk the list twice, each pass is O(n).
# Space Complexity: O(1) - only a few pointers and counters, no extra list.


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        index = count // 2
        i = 0
        curr = head
        while i < index:
            curr = curr.next
            i += 1
        return curr


# Approach 2 (tortoise and hare / slow and fast pointers):
# 1. Start slow and fast at head.
# 2. Move slow 1 step and fast 2 steps until fast cannot take two steps.
# 3. When fast reaches the end, slow is at the middle (the second
#    middle when n is even).

# Time Complexity: O(n) - fast still visits about n/2 nodes; one pass.
# Space Complexity: O(1) - only two pointers.


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
