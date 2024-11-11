class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.items = []


    def push(self, element):
        # Добавляем элемент в конец списка (вершину стека)
        self.items.append(element)


    def pop(self):
        # Проверяем, пуст ли стек
        if not self.is_empty():
            # Удаляем последний добавленный элемент из списка (вершины стека)
            return self.items.pop()
        else:
            # Если стек пуст, вызываем исключение
            raise IndexError("Stack is empty")


    def peek(self):
        # Проверяем, пуст ли стек
        if not self.is_empty():
            # Возвращаем последний добавленный элемент из списка (вершину стека) без удаления
            return self.items[-1]
        else:
            # Если стек пуст, вызываем исключение
            raise IndexError("Stack is empty")


    def is_empty(self):
        # Проверяем, пуст ли стек, сравнивая длину списка с 0
        return len(self.items) == 0


    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)


print("Стек:")
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # 2
print(stack.pop())  # 2
print(stack.size())  # 1