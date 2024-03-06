class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_minimum_value(root):
    current = root

    # Шукаємо вузол з найменшим значенням (лівий край дерева)
    while current.left is not None:
        current = current.left

    return current.key

# Приклад використання:
# Задаємо структуру дерева
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Знаходимо найменше значення
min_value = find_minimum_value(root)
print("Найменше значення у дереві:", min_value)
