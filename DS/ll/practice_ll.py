class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self) -> str:
        result = ""

        curr = self.head
        while curr:
            result += f"{curr.value}"
            if curr.next:
                result += "->"
            curr = curr.next

        return result

    def append(self, value):  # O(n)
        node = Node(value)
        curr = self.head
        if not curr:
            self.head = node
            self.tail = node
        else:
            while curr.next:
                curr = curr.next
            curr.next = node
            self.tail = curr.next

    def prepend(self, value):  # O(1)
        node = Node(value)
        curr = self.head
        self.head = node
        node.next = curr
        if not curr:
            self.tail = self.head

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head, self.tail = self.tail, self.head

    def find_middle(self):  # Tortoise and hare algorithm O(N/2) = O(N)
        ptr = self.head

        fast = ptr

        while fast and fast.next:
            ptr = ptr.next
            fast = fast.next.next

        return ptr.value

    def delete(self, val):
        curr = self.head
        prev = self.head

        while curr:
            if curr.value == val:
                if curr == self.head:
                    self.head = curr.next
                else:
                    prev.next = curr.next

            prev = curr
            curr = curr.next


l = LinkedList()
l.append(129)
l.append(19)
l.prepend(129)
l.append(199)
l.append(129)
l.append(126)
