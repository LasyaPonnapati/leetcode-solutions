# LeetCode 83. Remove Duplicates from Sorted List
# Given the head of a sorted linked list, delete all duplicates so that
# each value appears only once. Return the list, still sorted.

# Approach (prev stays on the first copy, curr skips extra copies):
# 1. Start prev and curr at head. They always begin a group together.
# 2. If the next nodes have the same value, move curr to the last copy
#    of that value.
# 3. Set prev.next past those extra copies so only the first copy remains.
# 4. Jump both prev and curr to the next distinct value and repeat.

# Time Complexity: O(n) - each node is visited a constant number of times.
# Space Complexity: O(1) - only two pointers; we change links in place.


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head
        while curr is not None:
            while curr.next is not None and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
            curr = curr.next
            prev = curr
        return head
