from AVL import root

# Функція для знаходження вузла з найменшим значенням
def min_value_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

print("Найменше значення:", min_value_node(root).key)