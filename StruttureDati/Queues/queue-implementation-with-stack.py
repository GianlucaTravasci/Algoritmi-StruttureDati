class QueueWithStack:
    def __init__(self):
        self.first = []
        self.last = []

    def peek(self):
        if len(self.first) == 0:
            return 0
        else:
            return self.first[len(self.first)-1]

    def enqueue(self, value):
        for i in range(len(self.first)):
            item = self.first.pop()
            self.last.append(item)
        self.first.append(value)
        for i in range(len(self.last)):
            item = self.last.pop()
            self.first.append(item)
        return

    def dequeue(self):
        if len(self.first) == 0:
            return 0
        else:
            return self.first.pop()

    def print_queue(self):
        if len(self.first) == 0:
            return 0
        for i in range(len(self.first)-1, 0, -1):
            print(f'{self.first[i]} <-- ', end='')
        print(self.first[0])
        return

queue = QueueWithStack()
queue.enqueue('Joy')
queue.enqueue('Sam')
queue.enqueue('Lerry')
print(queue.peek())
queue.print_queue()
