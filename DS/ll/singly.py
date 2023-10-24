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
        self.length = 1

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
            self.length += 1
            self.tail = node

    def append(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head
        self.length += 1

    def insert(self, value, position):
        if position > self.length:
            print(f"Index value {position} exceeds the length of Linked List")

        elif position not in (0, self.length):
            pos_count = 0
            ptr = self.head
            while abs(pos_count - position) != 1:
                ptr = ptr.next
                pos_count += 1
            node = Node(value)
            node.next = ptr.next
            ptr.next = node
        else:
            print("Try other methods for inserting in beginning or end")

    def search(self, value):
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1
    
    def get(self, index):
        current = self.head
        int_index = 0

        while current:
            if int_index == index:
                return current.value
            current = current.next
            int_index += 1
        
    def set(self, index, value):

        current = self.head
        int_index = 0

        while current:
            if int_index == index:
                current.value = value
            current = current.next
            int_index += 1
        
        


l = LinkedList(10)
l.create_list([11, 12, 13, 14])
print(l.head)
l.insert(111, 6)
l.insert(111, 5)
l.insert(111, 2)
l.append(112)
l.prepend(100)
print(l.head)
print(l.search(190))  # Not found
print(l.search(12))  # Found

print(l.get(index=2))
l.set(index=2, value=300)
