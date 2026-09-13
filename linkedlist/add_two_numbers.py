# LeetCode 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each node contains
# a single digit. Add the two numbers and return the sum as a linked list.

# Approach (add digit by digit from the front, keep a carry):
# 1. Walk both lists together. Each node is already the next place value
#    (ones, then tens, then hundreds), so we add temp1.val + temp2.val
#    plus the carry from the previous place (the code calls this borrow).
# 2. If the sum is greater than 9, the digit we store is val % 10, and
#    the new carry is val // 10. We must compute the carry before we
#    overwrite val with val % 10.
# 3. After one list ends, keep walking the longer list and adding carry.
# 4. If a carry is still left at the end (example: 5 + 5), append one more node.

# Time Complexity: O(max(n, m)) - we visit each node of the longer list once.
# Space Complexity: O(max(n, m)) - we build a new list whose length is the
# longer input, plus one extra node if there is a leftover carry.


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        l3 = None
        temp3 = l3
        borrow = 0
        while temp1 is not None and temp2 is not None:
            val = temp1.val + temp2.val
            if borrow != 0:
                val += borrow
            if val > 9:
                borrow = val // 10
                val = val % 10
            else:
                borrow = 0
            new_node = ListNode(val)
            if l3 is None:
                l3 = new_node
                temp3 = new_node
            else:
                temp3.next = new_node
                temp3 = temp3.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1 is not None:
            val = temp1.val
            if borrow != 0:
                val += borrow
            if val > 9:
                borrow = val // 10
                val = val % 10
            else:
                borrow = 0
            new_node = ListNode(val)
            if l3 is None:
                l3 = new_node
                temp3 = new_node
            else:
                temp3.next = new_node
                temp3 = temp3.next
            temp1 = temp1.next
        while temp2 is not None:
            val = temp2.val
            if borrow != 0:
                val += borrow
            if val > 9:
                borrow = val // 10
                val = val % 10
            else:
                borrow = 0
            new_node = ListNode(val)
            if l3 is None:
                l3 = new_node
                temp3 = new_node
            else:
                temp3.next = new_node
                temp3 = temp3.next
            temp2 = temp2.next
        if borrow != 0:
            new_node = ListNode(borrow)
            if l3 is None:
                l3 = new_node
                temp3 = new_node
            else:
                temp3.next = new_node
        return l3


# Approach 2 (same math, one loop, dummy head):
# 1. A dummy node sits before the real answer. We always append onto
#    dummy.next, so we never special-case "is the result list empty?"
# 2. Keep going while either list still has a node, or a carry is left.
# 3. A missing node counts as digit 0, so leftover digits and a final
#    carry all use the same loop as the overlapping part.
# 4. Digit is val % 10, carry is val // 10 (same as borrow in Approach 1).
# 5. Return dummy.next, which is the true head of the sum list.

# Time Complexity: O(max(n, m)) - we still visit each node once.
# Space Complexity: O(max(n, m)) - new list of that length, plus one
# extra node if there is a leftover carry. The dummy node is O(1).


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp3 = dummy
        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1 is not None or temp2 is not None or carry != 0:
            val = carry
            if temp1 is not None:
                val += temp1.val
                temp1 = temp1.next
            if temp2 is not None:
                val += temp2.val
                temp2 = temp2.next
            carry = val // 10
            val = val % 10
            temp3.next = ListNode(val)
            temp3 = temp3.next
        return dummy.next
