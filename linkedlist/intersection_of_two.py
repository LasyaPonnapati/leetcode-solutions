# LeetCode 160. Intersection of Two Linked Lists
# Given the heads of two singly linked lists, return the node where they
# intersect. If they do not intersect, return None.
# The lists may have different lengths. Intersection means they share the
# same node object from that point onward (same next pointers), not just
# the same values.

# Approach 1 (set of seen nodes):
# 1. Walk the first list and store each node object in a set.
# 2. Walk the second list. If the current node is already in the set,
#    that same node belongs to both lists → it is the intersection.
# 3. If we finish the second list with no match, return None.
#
# Note: store the node itself, not node.val and not node.next.
# Values can repeat without any shared node. Storing .next would miss
# an intersection at a head, and None (end of a list) would look like
# a duplicate even when the lists never meet.
# This problem asks for the intersection node (or None), not True/False.

# Time Complexity: O(n + m) - we visit every node of both lists once.
# Space Complexity: O(n) - the set stores every node of the first list.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        t1 = headA
        while t1 is not None:
            s.add(t1)
            t1 = t1.next

        t2 = headB
        while t2 is not None:
            if t2 in s:
                return t2
            t2 = t2.next

        return None


# Approach 2 (count lengths, skip the extra prefix, then walk together):
# 1. Walk list A and list B separately to get their lengths l1 and l2.
# 2. Reset both pointers to the heads.
# 3. Skip |l1 - l2| nodes on the longer list so both pointers have the
#    same number of nodes left.
# 4. Walk both lists one step at a time. The first node that is the same
#    object on both lists is the intersection.
# 5. If we reach the end without a match, there is no intersection.

# Time Complexity: O(n + m) - we walk each list once to count, then once
# to skip and compare. n and m are the lengths of the two lists.
# Space Complexity: O(1) - only a few pointers and length counters.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1 = 0
        t1 = headA
        while t1 is not None:
            l1 += 1
            t1 = t1.next

        l2 = 0
        t2 = headB
        while t2 is not None:
            l2 += 1
            t2 = t2.next

        t1 = headA
        t2 = headB

        if l1 > l2:
            l = l1 - l2
            while l != 0:
                t1 = t1.next
                l -= 1
        if l2 > l1:
            l = l2 - l1
            while l != 0:
                t2 = t2.next
                l -= 1

        while t1 is not None and t2 is not None:
            if t1 == t2:
                return t1
            t1 = t1.next
            t2 = t2.next

        return None


# Approach 3 (two pointers, jump to the other list at the end):
# 1. Start t1 at headA and t2 at headB, then walk both one step at a time.
# 2. When a pointer reaches None, send it to the other list's head.
#    t1 walks A then B. t2 walks B then A. Both travel n + m steps.
# 3. After that, they are aligned. The first shared node is the
#    intersection. If there is none, they both become None together.
# Compare the current nodes (t1 == t2), not t1.next. Switching happens
# after a pointer is already None, not when .next is None — otherwise
# you skip the other list's head. Use == / is for checks, not =.

# Time Complexity: O(n + m) - each pointer walks both lists at most once.
# Space Complexity: O(1) - only two pointers.


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        t1 = headA
        t2 = headB
        while t1 != t2:
            if t1 is None:
                t1 = headB
            else:
                t1 = t1.next
            if t2 is None:
                t2 = headA
            else:
                t2 = t2.next
        return t1
