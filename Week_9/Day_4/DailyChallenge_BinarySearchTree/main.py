from random import randint

class Node:
    counter = 0
    root = None

    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None
        if self.counter == 0:
            Node.root = self
            Node.counter += 1

    def __repr__(self):
        return f'\t(Node value: {self.value}:' \
               f'\t<--: {self.left}' \
               f'\t-->: {self.right})||'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, node_value):
        self._value = node_value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node):
        self._left = left_node if isinstance(left_node, Node) else None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node):
        self._right = right_node if isinstance(right_node, Node) else None

    @staticmethod
    def is_None(child):
        return True if child is None else False

    @staticmethod
    def add_node(self, other):
        if self.value >= other.value:
            if self.is_None(self.left):
                self.left = other
            else:
                self.add_node(self.left, other)
        else:
            if self.is_None(self.right):
                self.right = other
            else:
                self.add_node(self.right, other)

    @staticmethod
    def searching(cls, value):
        print(f'\t- Current node: {cls.value}')
        if value == cls.value:
            print(f"{value} is in the binary tree.")
            return True
        else:
            if value <= cls.value and cls.left is not None:
                cls.searching(cls.left, value)
            elif value > cls.value and cls.right is not None:
                cls.searching(cls.right, value)
            else:
                print(f"{value} isn't in the binary tree.")
                return False

    @staticmethod
    def search_result(value):
        print(f'Searching {value} in binary search tree.')
        Node.searching(Node.root, value)


n1 = Node(4)
# test = Node(-300)
# n1.add_node(n1, test)

for _ in range(10):
    n1.add_node(n1, Node(randint(-100, +100)))

searching_value = 40
n1.search_result(searching_value)
