class Stack:
   def __init__(self):
       self.items = []


    # проверка на пустоту
   def is_empty(self):
       return self.items == []


    # добавление элемента
   def push(self, item):
       self.items.append(item)


    # удаление элемента
   def pop(self):
       return self.items.pop()


    # просмотр последнего элемента
   def peek(self):
       return self.items[-1]


stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())
