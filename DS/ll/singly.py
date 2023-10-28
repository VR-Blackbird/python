class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"


def mergeTwoLists(l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = l1.head
        curr2 = l2.head
        prev = curr
        if not curr:
            l1.head = curr2
            return curr2
        elif not curr2:
            l1.head = curr
            return curr
        
        while curr:

            while curr2 and curr2.value <= curr.value:
                node = Node(curr2.value)
                node.next = curr

                if prev == curr:
                    l1.head = node
                else:
                    prev.next = node

                next_curr = curr2.next
                del curr2
                curr2 = next_curr
                l2.head = curr2
                prev = prev.next

            curr2 = l2.head
            prev = curr

            curr = curr.next
        l1.tail.next = l2.head
        del l2
        return l1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def create_list(self, value_list):  # O(n)
        for value in value_list:
            self.append(value)

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        self.length += 1

    def prepend(self, value):  # O(1)
        node = Node(value)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head
        self.length += 1

    def insert(self, value, position):  # O(n)
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
            self.length += 1
        else:
            print("Try other methods for inserting in beginning or end")

    def search(self, value):  # O(n)
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def get(self, index):  # O(n)
        current = self.head
        int_index = 0

        while current:
            if int_index == index:
                return current.value
            current = current.next
            int_index += 1

    def set(self, index, value):  # O(n)
        current = self.head
        int_index = 0

        while current:
            if int_index == index:
                current.value = value
            current = current.next
            int_index += 1

    def pop_left(self):  # O(1)
        current = self.head

        if self.length == 0:
            return None

        popped_value = current.value
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            self.head = current.next
        del current
        self.length -= 1
        return popped_value

    def pop(self):  # O(n)
        current = self.head

        if self.length == 0:
            return None

        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            while current.next != self.tail:
                current = current.next

            self.tail = current
            self.tail.next = None
        popped_value = popped_node.value
        del popped_node

        self.length -= 1

        return popped_value

    def remove(self, index):
        curr = self.head

        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None

            else:
                curr_head = self.head
                self.head = curr_head.next

                del curr_head

        else:
            idx_start = 0

            while idx_start != index - 1:
                curr = curr.next
                idx_start += 1
            deleting_node = curr.next
            curr.next = deleting_node.next
            self.length -= 1

            if idx_start == self.length - 1:
                self.tail = curr

            del deleting_node

    def reverse(self):
        prev_node = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head, self.tail = self.tail, self.head

    def find_middle(self):
        # TODO

        curr = self.head
        mid = self.length // 2
        idx = 0

        while idx != mid:
            curr = curr.next
            idx += 1
        return curr

    def remove_duplicates(self):
        # TODO
        visited = set()
        curr = self.head
        prev = curr

        while curr:
            if curr.value in visited:
                prev.next = curr.next
                if not curr.next:
                    self.tail = prev
                    self.tail.next = None
                self.length -= 1
            else:
                visited.add(curr.value)
                prev = curr
            curr = prev.next


l1 = LinkedList()
# l1.create_list([1, 2, 4])
l2 = LinkedList()
l2.create_list([0])
# l.remove_duplicates()
mergeTwoLists(l1, l2)