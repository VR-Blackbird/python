from collections import namedtuple


# Node = namedtuple("Node", ["value", "next"])

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node

    def create_list(self, value_list):
        for value in value_list:
            node = Node(value)
            if not self.head.next:
                self.head.next = node
            else:
                traverse = self.head
                while True:
                    if not traverse.next:
                        traverse.next = node
                        break
                    else:
                        traverse = traverse.next
            self.tail = node

    def insert_element_end(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node

    def insert_element_start(self, value):
        node = Node(value)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head

    # def insert(self, value):
    #     node = Node(value)
    #     self.head.next=node
    #     self.tail = node


l = LinkedList(10)
l.create_list([11, 12, 13, 14])
print(l.head)