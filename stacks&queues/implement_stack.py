# Implement a Stack
# Build a last-in, first-out (LIFO) stack with push, pop, peek,
# is_empty, and size. Three versions: Python list, collections.deque,
# and queue.LifoQueue.

from collections import deque
from queue import LifoQueue, Empty


class StackWithList:
    """Stack using a Python list. The end of the list is the top."""

    def __init__(self):
        self._items = []

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, value):
        self._items.append(value)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self):
        return len(self._items) == 0

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def size(self):
        return len(self._items)


class StackWithDeque:
    """Stack using collections.deque. The right end is the top."""

    def __init__(self):
        self._items = deque()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, value):
        self._items.append(value)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self):
        return len(self._items) == 0

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def size(self):
        return len(self._items)


class StackWithLifoQueue:
    """Stack using queue.LifoQueue (thread-safe LIFO queue)."""

    def __init__(self):
        self._items = LifoQueue()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def push(self, value):
        self._items.put(value)

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def pop(self):
        try:
            return self._items.get_nowait()
        except Empty:
            raise IndexError("pop from empty stack") from None

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def peek(self):
        try:
            value = self._items.get_nowait()
        except Empty:
            raise IndexError("peek from empty stack") from None
        self._items.put(value)
        return value

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def is_empty(self):
        return self._items.empty()

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def size(self):
        return self._items.qsize()
