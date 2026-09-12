# LeetCode 21. Merge Two Sorted Lists
# Given the heads of two sorted linked lists list1 and list2, merge them
# into one sorted list and return the head of the merged list.

# Approach (build a new list by always taking the smaller current value):
# 1. Walk both lists with curr1 and curr2. Keep list3 as the new head
#    and curr3 as the tail of that new list.
# 2. add_node() is a small helper inside this function so the
#    "first node vs append to tail" logic is written only once.
# 3. While both lists still have nodes, compare curr1.val and curr2.val.
#    Add a new node with the smaller value, then advance that list.
# 4. When one list ends, copy whatever is left in the other list
#    using the same helper.
# 5. If both lists were empty, list3 stays None.

# Time Complexity: O(n + m) - each node from both lists is visited once.
# Space Complexity: O(n + m) - we create a new node for every value
# instead of reusing the original nodes.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        list3 = None
        curr3 = list3

        def add_node(val):
            nonlocal list3, curr3
            new_node = ListNode(val)
            if curr3 is None:
                list3 = new_node
                curr3 = new_node
            else:
                curr3.next = new_node
                curr3 = curr3.next

        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                add_node(curr1.val)
                curr1 = curr1.next
            else:
                add_node(curr2.val)
                curr2 = curr2.next
        while curr1 is not None:
            add_node(curr1.val)
            curr1 = curr1.next
        while curr2 is not None:
            add_node(curr2.val)
            curr2 = curr2.next
        return list3


# Approach 2 (splice runs in place, no new nodes):
# 1. Walk both lists. Whichever current node is smaller, keep moving
#    along that list while its next value is still <= the other list's
#    current value. That stretch is one sorted "run".
# 2. Save the node after the run (next_node), then point the run's last
#    node at the other list so those remaining nodes are linked in.
# 3. Continue from next_node (the leftover of the list we just left).
# 4. Stop when one pointer becomes None: the last splice already attached
#    whatever was left of the other list.
# 5. Return the original head with the smaller first value (or the
#    non-empty list if one input was empty).

# Time Complexity: O(n + m) - each node is visited a constant number of times.
# Space Complexity: O(1) - we only change existing next pointers.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1 = list1
        curr2 = list2
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                while curr1.next is not None and curr1.next.val <= curr2.val:
                    curr1 = curr1.next
                next_node = curr1.next
                curr1.next = curr2
                curr1 = next_node
            else:
                while curr2.next is not None and curr2.next.val <= curr1.val:
                    curr2 = curr2.next
                next_node = curr2.next
                curr2.next = curr1
                curr2 = next_node

        if list2.val < list1.val:
            return list2
        return list1