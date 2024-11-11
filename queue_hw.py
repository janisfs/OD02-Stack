class Queue:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов очереди
        self.items = []


    def enqueue(self, element):
        # Добавляем элемент в конец списка (хвост)
        self.items.append(element)


    def dequeue(self):
        # Проверяем, пуст ли стек
        if not self.is_empty():
            # Удаляем первый элемент из списка (голова)
            # Используем pop(0), чтобы удалить первый элемент
            return self.items.pop(0)
        else:
            # Если стек пуст, вызываем исключение
            raise IndexError("Queue is empty")


    def peek(self):
        # Проверяем, пуст ли стек
        if not self.is_empty():
            # Возвращаем первый элемент из списка (голова) без удаления
            return self.items[0]
        else:
            # Если стек пуст, вызываем исключение
            raise IndexError("Queue is empty")


    def is_empty(self):
        # Проверяем, пуст ли стек, сравнивая длину списка с 0
        return len(self.items) == 0


    def size(self):
        # Возвращаем количество элементов в стеке
        return len(self.items)


print("\nОчередь:")
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())  # 1
print(queue.dequeue())  # 1
print(queue.size())  # 1