# Min Stack
# LeetCode 155: Design a stack that supports push, pop, top, and
# retrieving the minimum element in constant time.
#
# Implement MinStack with:
# - MinStack() initializes the stack
# - push(val) pushes val onto the stack
# - pop() removes the top element
# - top() returns the top element
# - getMin() returns the minimum element currently in the stack
#
# Approach: Keep one stack. Each entry is (value, min_so_far), where
# min_so_far is the smallest value from the bottom up through this
# entry. Pushing stores the new min. Popping restores the previous
# min automatically because it is saved on the new top.
#
# Time: O(1) for push, pop, top, and getMin — each does a constant
#       amount of work (append, pop, or index the last item).
# Space: O(n) — the stack stores two numbers for each of the n
#        elements.


class MinStack:

    def __init__(self):
        self.s = []

    def push(self, value: int) -> None:
        if not self.s:
            minele = value
        else:
            minele = min(value, self.s[-1][1])
        self.s.append((value, minele))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
