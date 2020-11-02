class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        temp = self.first.next
        dequeued = self.first
        if temp == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1

    def print_linked_list(self):
        temp = self.first
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        print('Lenght = ' + str(self.length))


queue = Queue()
queue.enqueue('google')
queue.enqueue('microsoft')
queue.enqueue('facebook')
queue.enqueue('netflix')
queue.dequeue()
print(queue.peek())
queue.print_linked_list()