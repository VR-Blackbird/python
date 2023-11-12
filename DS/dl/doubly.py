class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node-{self.value}"


class DLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head

        while node:
            yield node
            node = node.right

    def prepend(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            curr = self.head
            curr.left = node
            node.right = curr
            self.head = node
        self.length += 1

    def append(self, value):
        node = Node(value)

        if self.tail:
            self.tail.right = node
            node.left = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.length += 1

    def insert(self, value, position):
        node = Node(value)
        if position >= self.length:
            return
        if position == 0:
            self.prepend(value)
        elif position == self.length - 1:
            self.append(value)
        else:
            curr = self.head
            count = 0
            while count != position:
                curr = curr.right
                count += 1
            prev = curr.left
            node.left = prev
            node.right = curr
            curr.left = node
            prev.right = node
        self.length += 1

    def reverse(self):
        if self.head:
            curr = self.tail
            while curr:
                curr.left, curr.right = curr.right, curr.left
                curr = curr.right
            self.head, self.tail = self.tail, self.head
            print("Linked list reversed")

    def pop_first(self):
        if self.head:
            self.head = self.head.right

            self.length -= 1

    def pop(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        if self.head:
            last = self.tail.left
            self.tail = last
            last.right = None
            self.length -= 1

    def remove(self, position):
        if position >= self.length:
            return

        if position == 0:
            self.pop_first()
        elif position == self.length - 1:
            self.pop()

        else:
            curr = self.head
            count = 0
            while count != position:
                curr = curr.right
                count += 1
            prev = curr.left
            next = curr.right
            prev.right = next
            next.left = prev
        self.length -= 1


d = DLL()
