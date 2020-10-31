class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def check_till_the_index(self, index):
        current_node = self.head
        counterIndex = 0
        if index >= 0:
            while counterIndex != index:
                current_node = current_node.next
                counterIndex += 1
            return current_node
        else:
            print('No negative index')

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
        else:
            loader = self.check_till_the_index(index-1)
            holder = loader.next
            loader.next = new_node
            new_node.next = holder
            new_node.prev = loader
            holder.prev = new_node
            self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        loader = self.check_till_the_index(index-1)
        unwanted_node = loader.next
        holder = unwanted_node.next
        loader.next = holder
        holder.prev = loader
        self.length -= 1

    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        print('Lenght = ' + str(self.length))


d = DoubleLinkedList()
d.append(1)
d.append(2)
d.append(3)
d.append(4)
d.prepend(5)
d.insert(4, 100)
d.insert(0, 34)
d.insert(22, 22)
d.remove(3)
d.print_linked_list()