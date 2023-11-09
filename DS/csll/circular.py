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

    def insert(self, value, position):
        if position == 0:
            self.prepend(value)
        elif position >= self.length:
            raise IndexError(f"Invalid Index - Length of linked list is {self.length}")
        elif position == self.length - 1:
            self.append(value)
        else:
            node = Node(value)
            curr = self.head
            pos = 0
            while abs(pos - position) > 1:
                curr = curr.next
                pos += 1
            next = curr.next
            curr.next = node
            node.next = next

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.value)
            if curr.next == self.head:
                break
            curr = curr.next
        

            
        

cl = CSLL()
cl.prepend(20)
cl.append(90)
cl.append(19)
cl.append(29)
cl.append(49)