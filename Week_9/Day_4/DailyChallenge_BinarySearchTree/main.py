from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'\t(Node value: {self.value}:\n' \
               f'\t<--: {self.left}' \
               f'\t-->: {self.right})||'


def insert(new_value, root):
    if root is None:
        root = Node(new_value)
        return root
    if new_value < root.value:
        root.left = insert(new_value, root.left)
    elif new_value > root.value:
        root.right = insert(new_value, root.right)
    return root


def search(value, root):
    if root is None:
        return False
    elif root.value == value:
        return True
    elif root.value > value:
        return search(value, root.left)
    else:
        return search(value, root.right)


root = insert(14, None)
for _ in range(10):
    node_value = randint(-40, 40)
    insert(node_value, root)

# insert(-23, root)
print(str(root))
print(search(-23, root))



