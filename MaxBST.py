class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_max_value_bst(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.key


# Приклад використання
bst_root = TreeNode(20)
bst_root.left = TreeNode(10)
bst_root.right = TreeNode(30)
bst_root.left.left = TreeNode(5)
bst_root.left.right = TreeNode(15)
bst_root.right.left = TreeNode(25)
bst_root.right.right = TreeNode(35)

max_value = find_max_value_bst(bst_root)
print("Найбільше значення в BST:", max_value)

