class StackWithArray:
    def __init__(self):
        self.array = []
        self.lenght = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):
        return self.array[self.lenght-1]

    def push(self, value):
        self.array.append(value)
        self.lenght += 1

    def pop(self):
        poped_item = self.array[self.lenght-1]
        del self.array[self.lenght-1]
        self.lenght -= 1
        return poped_item

stack = StackWithArray()
stack.push('asd')
stack.push('asasdd')
stack.push('eerwew')
stack.push('asfhrghd')
stack.push('a432532sd')
stack.push('atedsd')
print('last item picked ' + stack.peek())
print('popped item ' + stack.pop())
print(f'final stack {stack}')
