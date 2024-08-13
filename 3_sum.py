from AVL import root

# Функція для знаходження суми всіх значень в дереві
def get_sum(root):
    if not root:
        return 0
    return root.key + (get_sum(root.left) if root.left else 0) + (get_sum(root.right) if root.right else 0)

print("Сума всіх значень:", get_sum(root))