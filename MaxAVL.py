class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def find_max_value_avl(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.key


# Приклад використання
avl_root = AVLNode(20)
avl_root.left = AVLNode(10)
avl_root.right = AVLNode(30)
avl_root.left.left = AVLNode(5)
avl_root.left.right = AVLNode(15)
avl_root.right.left = AVLNode(25)
avl_root.right.right = AVLNode(35)

max_value_avl = find_max_value_avl(avl_root)
print("Найбільше значення в AVL-дереві:", max_value_avl)
