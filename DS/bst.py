class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BSTNode(data)


    def in_order(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.in_order()


        if self.right:
            elements += self.right.in_order()

        elements.append(self.data)

        return elements


def build_tree(elems):
    root = BSTNode(elems[0])

    for i in elems[1:]:
        root.add_child(i)

    return root


elements = [14,12,11, 15]
tree = build_tree(elements)
print(tree.in_order())
