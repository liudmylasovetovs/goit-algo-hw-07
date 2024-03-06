class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def sum_tree(root):
    if root is None:
        return 0
    else:
        return sum_tree(root.left) + root.key + sum_tree(root.right)

# Приклад використання
root = Node(10, Node(5), Node(15, Node(12), Node(20)))
sum = sum_tree(root)
print(f"Сума всіх ключів: {sum}")
