class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

def get_height(node):
    if node is None:
        return 0
    else:
        return node.height

def get_balance_factor(node):
    if node is None:
        return 0
    else:
        return get_height(node.left) - get_height(node.right)

def sum_tree(root):
    if root is None:
        return 0
    else:
        balance_factor = get_balance_factor(root)
        if balance_factor not in [-1, 0, 1]:
            raise ValueError("Дерево не є AVL-деревом")
        return sum_tree(root.left) + root.key + sum_tree(root.right)

# Приклад використання
root = Node(10, Node(5), Node(15, Node(12), Node(20)))
sum = sum_tree(root)
print(f"Сума всіх ключів: {sum}")
