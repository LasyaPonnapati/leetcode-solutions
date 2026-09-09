# LeetCode 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list and return the new head.

# Approach (stack of values, then rebuild):
# 1. Walk the list and push every node's value onto a stack.
# 2. Pop to create a new list. Because a stack is LIFO, values come out reversed.
# 3. If the list is empty, return None (there is nothing to pop).

# Time Complexity: O(n) - one pass to fill the stack, one pass to rebuild the list.
# Space Complexity: O(n) - the stack stores one value per node, plus a new list of n nodes.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next

        head = ListNode(stack.pop())
        curr = head
        while stack:
            new_node = ListNode(stack.pop())
            curr.next = new_node
            curr = curr.next
        return head


# Approach 2 (in-place pointer reversal):
# 1. If the list is empty or has one node, return head (already reversed).
# 2. Keep three pointers: prev, curr, and nxtnode.
# 3. For each node, save curr.next, point curr.next to prev, then slide prev
#    and curr forward until curr is None.
# 4. prev is the new head.

# Time Complexity: O(n) - we visit each node once.
# Space Complexity: O(1) - only a few pointers; we reverse links in place.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        prev = None
        curr = head
        while curr is not None:
            nxtnode = curr.next
            curr.next = prev
            prev = curr
            curr = nxtnode
        head = prev
        return head

