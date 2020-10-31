class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackWithList:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.bottom == None:
            self.bottom = new_node
            self.top = self.bottom
            self.length += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.length += 1

    def pop(self):
        if not self.top:
            return None
        holderPointer = self.top
        self.top = self.top.next
        self.length -= 1
        if self.length == 0:
            self.bottom = None
        return holderPointer.data

    def printStack(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print()
        print('Lenght = ' + str(self.length))

s = StackWithList()
s.push(1)
s.push(2)
s.push(4)
s.push(32)
s.push(12)
s.push(45)
s.push(99)
s.pop()
print(s.peek())
s.printStack()