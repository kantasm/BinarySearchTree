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

    # find_max
    print(numbers_tree.find_min())

    print(max(numbers))
    print(min(numbers))
    print(sorted(numbers))
    print(sorted(numbers,reverse=True))

    #strings = ['Pixel', 'Chromebook', 'Nest', 'Youtube', 'Maps', 'Alphabet','Google']
    #strings_tree = build_tree(strings)
    #print(strings_tree.in_order_traversal())
    #print(strings_tree.search_tree('Nest'))




