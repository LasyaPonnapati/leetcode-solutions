# LeetCode: N/A — Implement Queue (foundational DSA practice)
# Implement Queue
# Build a queue (FIFO: first in, first out) with push, pop, peek,
# is_empty, and size. Shown three ways: Python list, collections.deque,
# and queue.Queue.

# Approach:
# 1. QueueUsingList: append at the back; pop(0) from the front (O(n) pop).
# 2. QueueUsingDeque: append and popleft for O(1) push and pop.
# 3. QueueUsingQueue: thread-safe queue.Queue with put/get.

# Time Complexity: push/peek/is_empty/size are O(1) for deque and queue.Queue;
# list-based pop is O(n). See per-method comments for each class.
# Space Complexity: O(n) to store n elements in the queue.

from collections import deque
from queue import Queue


class QueueUsingList:
    def __init__(self):
        self.items = []

    # Time: O(1) 
    # Space: O(1)
    def push(self, x):
        self.items.append(x)

    # Time: O(n)
    # Space: O(1)
    def pop(self):
        if self.is_empty():
            print("empty")
        else:
            return self.items.pop(0)

    # Time: O(1)
    # Space: O(1)
    def peek(self):
        if self.is_empty():
            print("empty")
        else:
            return self.items[0]

    # Time: O(1)
    # Space: O(1)
    def is_empty(self):
        return len(self.items) == 0

    # Time: O(1)
    # Space: O(1)
    def size(self):
        return len(self.items)


class QueueUsingDeque:
    def __init__(self):
        self.items = deque()

    # Time: O(1)
    # Space: O(1)
    def push(self, x):
        self.items.append(x)

    # Time: O(1)
    # Space: O(1)
    def pop(self):
        if self.is_empty():
            print("empty")
        else:
            return self.items.popleft()

    # Time: O(1)
    # Space: O(1)
    def peek(self):
        if self.is_empty():
            print("empty")
        else:
            return self.items[0]

    # Time: O(1)
    # Space: O(1)
    def is_empty(self):
        return len(self.items) == 0

    # Time: O(1)
    # Space: O(1)
    def size(self):
        return len(self.items)


class QueueUsingQueue:
    def __init__(self):
        self.q = Queue()

    # Time: O(1)
    # Space: O(1)
    def push(self, x):
        self.q.put(x)

    # Time: O(1)
    # Space: O(1)
    def pop(self):
        if self.is_empty():
            print("empty")
        else:
            return self.q.get_nowait()

    # Time: O(1)
    # Space: O(1)
    def peek(self):
        if self.is_empty():
            print("empty")
        else:
            with self.q.mutex:
                return self.q.queue[0]

    # Time: O(1)
    # Space: O(1)
    def is_empty(self):
        return self.q.empty()

    # Time: O(1)
    # Space: O(1)
    def size(self):
        return self.q.qsize()
