# Doubly Linked List
# Same idea as a singly linked list, but each node also stores a
# pointer to the previous node. That makes delete_at_end O(1),
# because tail already knows its previous node.

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
        self.head.prev = new_node
        self.head = new_node

    # Time: O(1) - only update tail (and head if list was empty)
    # Space: O(1) - one new node
    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
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
        next_node = prev.next
        new_node.prev = prev
        new_node.next = next_node
        prev.next = new_node
        next_node.prev = new_node

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
        next_node=self.head.next
        self.head.next=None
        next_node.prev=None
        self.head=next_node

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
        back_node=self.tail.prev
        self.tail.prev=None
        back_node.next=None
        self.tail=back_node

    # Time: O(n) - walk to the node at the given index
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
        while prev is not None and i < index-1:
            prev = prev.next
            i += 1

        if prev is None or prev.next is None:
            print("Invalid index")
            return

        # Last node: reuse delete_at_end so tail is updated correctly
        if prev.next.next is None:
            self.delete_at_end()
            return

        next_node = prev.next
        prev.next = next_node.next
        next_node.next.prev = prev
        next_node.next = None
        next_node.prev = None
