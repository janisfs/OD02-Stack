# Класс Node представляет собой узел дерева
class Node:
    def __init__(self, value):
        # Инициализируем узел с заданным значением
        self.value = value
        # Инициализируем список детей узла
        self.children = []


# Класс Tree представляет собой дерево
class Tree:
    def __init__(self, root):
        # Инициализируем дерево с корневым узлом
        self.root = Node(root)


    # Метод add_child добавляет дочерний узел к заданному родительскому узлу
    def add_child(self, parent, child):
        # Находим родительский узел в дереве
        parent_node = self.find_node(parent)
        if parent_node:
            # Добавляем дочерний узел к родительскому узлу
            parent_node.children.append(Node(child))


    # Метод find_node находит узел с заданным значением в дереве
    def find_node(self, value):
        # Вызываем рекурсивный метод _find_node для поиска узла
        return self._find_node(self.root, value)


    # Метод _find_node является рекурсивным методом для поиска узла в дереве
    def _find_node(self, node, value):
        # Если значение узла совпадает с заданным значением, возвращаем узел
        if node.value == value:
            return node
        # Иначе, рекурсивно вызываем метод _find_node для детей узла
        for child in node.children:
            found_node = self._find_node(child, value)
            if found_node:
                return found_node
        # Если узел не найден, возвращаем None
        return None


# Создаем дерево с корневым узлом 1
tree = Tree(1)

# Добавляем дочерние узлы к корневому узлу
tree.add_child(1, 2)
tree.add_child(1, 3)

# Добавляем дочерние узлы к узлу 2
tree.add_child(2, 4)
tree.add_child(2, 5)

# Добавляем дочерние узлы к узлу 3
tree.add_child(3, 6)
tree.add_child(3, 7)

# Выводим значение корневого узла
print("Корневой узел:", tree.root.value)

# Выводим значения детей корневого узла
print("Дети корневого узла:", [child.value for child in tree.root.children])

# Выводим значение узла 2
print("Узел 2:", tree.find_node(2).value)

# Выводим значения детей узла 2
print("Дети узла 2:", [child.value for child in tree.find_node(2).children])

#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7