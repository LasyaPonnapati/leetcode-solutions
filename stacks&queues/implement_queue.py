# Implement Queue
# Build a queue (FIFO: first in, first out) with push, pop, peek,
# is_empty, and size. Shown three ways: Python list, collections.deque,
# and queue.Queue.

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
