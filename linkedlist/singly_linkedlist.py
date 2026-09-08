# Singly Linked List
# A linear data structure where each node stores data and a pointer
# to the next node. The list keeps a head (first node) and a tail
# (last node) so we can add/remove at both ends without extra scans
# when the operation is at the start or the end.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time: O(n) - walk from head to the given index
    # Space: O(1) - only a few pointers
    def get(self, index):
        if index < 0:
            print("Invalid index")
            return None
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current.data
            current = current.next
            i += 1
        print("Invalid index")
        return None

    # Time: O(1) - only update head (and tail if list was empty)
    # Space: O(1) - one new node
    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    # Time: O(1) - only update tail (and head if list was empty)
    # Space: O(1) - one new node
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # Time: O(n) - walk to the node before the insert index
    # Space: O(1) - one new node
    def add_at_middle(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.add_at_beginning(data)
            return

        prev = self.head
        i = 0
        while prev is not None and i < index - 1:
            prev = prev.next
            i += 1

        if prev is None:
            print("Invalid index")
            return

        if prev.next is None:
            self.add_at_end(data)
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    # Time: O(1) - only move head (and clear tail if one node)
    # Space: O(1) - no extra memory
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next

    # Time: O(n) - must walk to the node before tail (no prev pointer)
    # Space: O(1) - no extra memory
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        prev.next = None
        self.tail = prev

    # Time: O(n) - walk to the node before the given index
    # Space: O(1) - no extra memory
    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.delete_at_start()
            return

        prev = self.head
        i = 0
        while prev.next is not None and i < index - 1:
            prev = prev.next
            i += 1

        if prev.next is None:
            print("Invalid index")
            return

        if prev.next == self.tail:
            self.delete_at_end()
            return

        prev.next = prev.next.next
