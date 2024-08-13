class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1  # Висота вузла
        self.left = None  # Лівий нащадок вузла
        self.right = None  # Правий нащадок вузла

    def __str__(self):
        return str(self.key)

# Функція для отримання висоти вузла
def get_height(node):
    if not node:
        return 0
    return node.height

# Функція для отримання балансу вузла
def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

# Лівий поворот навколо вузла
def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

# Правий поворот навколо вузла
def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

# Функція вставки нового ключа в AVL-дерево
def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    # Оновлення висоти кореневого вузла
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Отримання балансу кореневого вузла
    balance = get_balance(root)

    # Лівий випадок
    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Правий випадок
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# Функція для побудови AVL-дерева з даного списку ключів
def get_binary_tree(lst):
    root = None
    for key in lst:
        root = insert(root, key)
    return root

# Функція для візуалізації дерева
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        if root.right:
            print_tree(root.right, level + 1, "R--- ")


# Приклад використання
keys = [10, 20, 30, 40, 50, 25, 35, 45, 55, 5, 0]
root = get_binary_tree(keys)

# print("\nВізуалізація дерева:")
# print_tree(root)