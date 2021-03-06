class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            # Do not add duplicate values -> Binary Tree contains unique values
            return

        if data < self.data:
            # add child node to the left subtree
            if self.left:  # check if it;s a leaf node
                self.left.add_child(data)
            else:
                # Not a leaf node
                self.left = BinarySearchTreeNode(data)
        else:
            # add child node to the right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right subtree
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = []
        #visit base node
        elements.append(self.data)

        #visit left subtree
        if self.left:
            elements += self.left.pre_order_traversal()

        #visit right subtree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        #visit left subtree
        if self.left:
            elements += self.left.post_order_traversal()

        #visit right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        #visit base node
        elements.append(self.data)
        return elements

    def search_tree(self, val):
        if val == self.data:
            return True

        if val < self.data:
            # search in left subtree
            if self.left:
                return self.left.search_tree(val)
            else:
                return False

        if val > self.data:
            # search in right subtree
            if self.right:
                return self.right.search_tree(val)
            else:
                return False
            return False

    def find_maximum(self):
        if self.right:
            return self.right.find_maximum()
        else:
            return self.data

    def find_minimum(self):
        if self.left:
            return self.left.find_minimum()
        else:
            return self.data

    def find_min(self):
        elements = []

        if self:
            elements += self.in_order_traversal()
            return elements[0]
        else:
            return -1

    def find_max(self):
        elements = []

        if self:
            elements += self.in_order_traversal()
            max_index = len(elements)-1
            return elements[max_index]
        else:
            return -1

    def clear_node(self):
        self.left = None
        self.right = None
        self.data = None

    def remove_node(self, value, parent=None):
        if value < self.data and self.left:
            return self.left.remove_node(value, self)
        elif value < self.data:
            return
        elif value > self.data and self.right:
            return self.right.remove_node(value, self)
        elif value > self.data:
            return
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()
            elif self.left is None and self.right and self == parent.right:
                parent.right = self.right
                self.clear_node()
            elif self.left is None and self.right and self == parent.left:
                parent.left = self.right
                self.clear_node()
            else:
                self.data = self.right.find_minimum()
                self.right.remove_node(self.data, self)
            return

    def delete_node(self, value):
        if value > self.data:
            if self.right:
                self.right = self.right.delete_node(value)
        elif value < self.data:
            if self.left:
                self.left = self.left.delete_node(value)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            min_val = self.right.find_minimum()
            self.data = min_val
            self.right = self.right.delete_node(min_val)

        return self


def build_tree(elements):
    # create root node
    root = BinarySearchTreeNode(elements[0])
    # create child nodes
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    numbers = [4, 15, 17, 12, 1, 14, 19, 21, 35, 4, 15, 17]
    numbers_tree = build_tree(numbers)
    print(numbers_tree)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.search_tree(12))

    # find_max
    print(numbers_tree.find_max())

    # find_min
    print(numbers_tree.find_min())

    print(max(numbers))
    print(min(numbers))

    # find_maximum
    print(numbers_tree.find_maximum())

    # find_minimum
    print(numbers_tree.find_minimum())


    print(sorted(numbers))
    print(sorted(numbers,reverse=True))
    print('Removing Node')
   # numbers_tree.remove_node(17)
    print(numbers_tree.in_order_traversal())

    numbers_tree.delete_node(17)
    print(numbers_tree.in_order_traversal())

    #strings = ['Pixel', 'Chromebook', 'Nest', 'Youtube', 'Maps', 'Alphabet','Google']
    #strings_tree = build_tree(strings)
    #print(strings_tree.in_order_traversal())
    #print(strings_tree.search_tree('Nest'))




