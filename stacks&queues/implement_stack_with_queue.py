# Implement Stack using Queues
# LeetCode 225: Implement a last-in, first-out (LIFO) stack using
# only queues. Support push, pop, top, and empty.
#
# A queue is FIFO and a stack is LIFO, so items must be rotated.
# You cannot make push, pop, and top all O(1) with only queue ops.
#
# 1. MyStackUsingList: one list as a queue. pop(0) is O(n), so
#    pop/top are O(n^2). Push is O(1).
# 2. MyStackUsingDeque: same idea with deque. Push O(1), pop/top O(n).
# 3. MyStackUsingDequeFastPop: rotate on push so the newest item
#    sits at the front. Push O(n), pop/top O(1).
# 4. MyStackUsingTwoQueues: push into q2, move all of q1 into q2,
#    then swap. Push O(n), pop/top O(1).

from collections import deque


class MyStackUsingList:

    def __init__(self):
        self.queue = []

    # Time: O(1)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Time: O(n^2)
    # Space: O(1)
    def pop(self) -> int:
        ln = len(self.queue)
        for i in range(ln - 1):
            self.queue.append(self.queue.pop(0))
        return self.queue.pop(0)

    # Time: O(n^2)
    # Space: O(1)
    def top(self) -> int:
        ln = len(self.queue)
        for i in range(ln - 1):
            self.queue.append(self.queue.pop(0))
        ele = self.queue[0]
        self.queue.append(self.queue.pop(0))
        return ele

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStackUsingDeque:

    def __init__(self):
        self.queue = deque()

    # Time: O(1)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.queue.append(x)

    # Time: O(n)
    # Space: O(1)
    def pop(self) -> int:
        ln = len(self.queue)
        for i in range(ln - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    # Time: O(n)
    # Space: O(1)
    def top(self) -> int:
        ln = len(self.queue)
        for i in range(ln - 1):
            self.queue.append(self.queue.popleft())
        ele = self.queue[0]
        self.queue.append(self.queue.popleft())
        return ele

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStackUsingDequeFastPop:

    def __init__(self):
        self.queue = deque()

    # Time: O(n)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    # Time: O(1)
    # Space: O(1)
    def pop(self) -> int:
        return self.queue.popleft()

    # Time: O(1)
    # Space: O(1)
    def top(self) -> int:
        return self.queue[0]

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStackUsingTwoQueues:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # Time: O(n)
    # Space: O(1)
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    # Time: O(1)
    # Space: O(1)
    def pop(self) -> int:
        return self.q1.popleft()

    # Time: O(1)
    # Space: O(1)
    def top(self) -> int:
        return self.q1[0]

    # Time: O(1)
    # Space: O(1)
    def empty(self) -> bool:
        return len(self.q1) == 0
