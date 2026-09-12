# LeetCode 234. Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome,
# or false otherwise.

# Approach (copy values into a list, then compare with the reverse):
# 1. Walk the list and append each node's value to a Python list.
# 2. A palindrome reads the same forwards and backwards, so check if
#    that list equals its reverse (l[::-1]).
# 3. Return True if they match, otherwise False.

# Time Complexity: O(n) - one pass to copy n values, plus one pass to reverse/compare.
# Space Complexity: O(n) - the extra list stores one value per node.


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        curr = head
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
        if l[::-1] == l:
            return True
        return False


# Approach 2 (stack of values, then compare while popping):
# 1. First walk: push every node's value onto a stack.
# 2. Second walk: compare the current node's value with the top of the stack.
#    If they match, pop and move forward. If they do not match, return False.
# 3. If the stack is empty and we have reached the end of the list, return True.
# A stack is LIFO, so the second walk compares first-with-last, second-with-second-last, and so on.

# Time Complexity: O(n) - one pass to fill the stack, one pass to compare and pop.
# Space Complexity: O(n) - the stack stores one value per node.


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        while curr is not None:
            if stack[-1] == curr.val:
                stack.pop()
            else:
                return False
            curr = curr.next

        if not stack and curr is None:
            return True
        return False


# Approach 3 (find middle, reverse second half, compare — O(1) extra space):
# 1. Use slow (1 step) and fast (2 steps) to find the middle.
# 2. Reverse the second half in place (same pointer reversal as reverse linked list).
# 3. Walk the first half and the reversed second half together.
#    If every pair of values matches, it is a palindrome.
# Note: this changes the original list (we reverse half of it).

# Time Complexity: O(n) - find middle, reverse half, and compare; each is one pass.
# Space Complexity: O(1) - only a few pointers; no extra list or stack.


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        # find middle
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev = None
        curr = slow
        while curr is not None:
            nxtnode = curr.next
            curr.next = prev
            prev = curr
            curr = nxtnode

        # compare first half and second half
        first = head
        second = prev
        while second is not None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
 