# Doubly Circular Linked List
# Combines a doubly linked list with a circular one: each node has
# prev and next, and the ends wrap around (tail.next = head,
# head.prev = tail). delete_at_end stays O(1) thanks to prev.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time: O(n) - walk from head to the given index
    # Space: O(1) - only a few pointers
    def get(self, index):
        if index < 0 or self.head is None:
            print("Invalid index")
            return None
        current = self.head
        i = 0
        while True:
            if i == index:
                return current.data
            current = current.next
            i += 1
            if current == self.head:
                break
        print("Invalid index")
        return None

    # Time: O(1) - only update head and keep both circular links
    # Space: O(1) - one new node
    def add_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        new_node.next = self.head
        new_node.prev = self.tail
        self.head.prev = new_node
        self.tail.next = new_node
        self.head = new_node

    # Time: O(1) - only update tail and keep both circular links
    # Space: O(1) - one new node
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        new_node.prev = self.tail
        new_node.next = self.head
        self.tail.next = new_node
        self.head.prev = new_node
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
        if self.head is None:
            print("Invalid index")
            return

        prev = self.head
        i = 0
        while i < index - 1:
            prev = prev.next
            i += 1
            if prev == self.head:
                print("Invalid index")
                return

        if prev == self.tail:
            self.add_at_end(data)
            return

        new_node = Node(data)
        next_node = prev.next
        new_node.prev = prev
        new_node.next = next_node
        prev.next = new_node
        next_node.prev = new_node

    # Time: O(1) - only move head and keep both circular links
    # Space: O(1) - no extra memory
    def delete_at_start(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        next_node = self.head.next
        next_node.prev = self.tail
        self.tail.next = next_node
        self.head = next_node

    # Time: O(1) - tail has a prev pointer, so no walk needed
    # Space: O(1) - no extra memory
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        back_node = self.tail.prev
        back_node.next = self.head
        self.head.prev = back_node
        self.tail = back_node

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
        while i < index - 1:
            prev = prev.next
            i += 1
            if prev == self.head:
                print("Invalid index")
                return

        if prev.next == self.head:
            print("Invalid index")
            return

        # Last node: reuse delete_at_end so tail is updated correctly
        if prev.next == self.tail:
            self.delete_at_end()
            return

        next_node = prev.next
        prev.next = next_node.next
        next_node.next.prev = prev
