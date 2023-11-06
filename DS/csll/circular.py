class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class CSLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self) -> str:
        result = ""
        circle = -1
        curr = self.head
        while curr and circle <= 0:
            if curr == self.head:
                circle += 1
            result += f"{curr.value}"
            if curr.next and circle != 1:
                result += "->"
            curr = curr.next

        return result

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        node.next = self.head
        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
            node.next = self.head
        else:
            curr = self.head
            node.next = curr
            self.head = node
            self.tail.next = self.head
        self.length += 1


cl = CSLL()
