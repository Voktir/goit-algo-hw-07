from AVL import root

# Функція для знаходження вузла з найбільшим значенням
def max_value_node(root):
    current = root
    while current.right is not None:
        current = current.right
    return current

print("Найбільше значення:", max_value_node(root).key)