# Implement Queue using Stacks
# LeetCode 232: Implement a first-in, first-out (FIFO) queue using
# only stacks. Support push, pop, peek, and empty.
#
# A stack is LIFO and a queue is FIFO, so items must be reversed
# when you need the front.
#
# 1. MyQueue: one list as a stack. Push O(1). Each pop/peek dumps
#    all items to a temp stack, takes the front, then dumps them
#    back. O(n).
# 2. MyQueueUsingDeque: same idea, but both stacks are deques.

from collections import deque


class MyQueue:

    def __init__(self):
        self.s = []

    # Time: O(1) 
    # Space: O(1) 
    def push(self, x: int) -> None:
        self.s.append(x)

    # Time: O(n)  
    # Space: O(n) 
    def pop(self) -> int:
        s2 = []
        while self.s:
            s2.append(self.s.pop())
        ele = s2.pop()
        while s2:
            self.s.append(s2.pop())
        return ele

    # Time: O(n)  
    # Space: O(n) 
    def peek(self) -> int:
        s2 = []
        while self.s:
            s2.append(self.s.pop())
        ele = s2[-1]
        while s2:
            self.s.append(s2.pop())
        return ele

    # Time: O(1)  
    # Space: O(1) 
    def empty(self) -> bool:
        return len(self.s) == 0


class MyQueueUsingDeque:

    def __init__(self):
        self.s = deque()

    # Time: O(1)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.s.append(x)

    # Time: O(n)
    # Space: O(n)
    def pop(self) -> int:
        s2 = deque()
        while self.s:
            s2.append(self.s.pop())
        ele = s2.pop()
        while s2:
            self.s.append(s2.pop())
        return ele

    # Time: O(n)
    # Space: O(n)
    def peek(self) -> int:
        s2 = deque()
        while self.s:
            s2.append(self.s.pop())
        ele = s2[-1]
        while s2:
            self.s.append(s2.pop())
        return ele

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.s) == 0
