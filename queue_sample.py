class Queue:
   def __init__(self):
       self.items = []


    # проверка на пустоту
   def is_empty(self):
       return self.items == []


    # добавление элемента
   def enqueue(self, item):
       self.items.insert(0, item)


    # удаление элемента
   def dequeue(self):
       return self.items.pop()


    # проверка размера
   def size(self):
       return len(self.items)


queue = Queue()

print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())
