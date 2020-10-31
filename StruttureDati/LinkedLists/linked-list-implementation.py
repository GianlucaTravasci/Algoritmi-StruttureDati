class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self): #this function init the head of the linked list
        self.head = None
        self.tail = None
        self.length = 0
        
    def preappend(self, data): #this function insert a new node at the begining of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head=new_node
        self.length+=1
    
    def append(self, data): #this function insert a new node at the end of the list
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    def insert(self, index, data): #this function insert a new node in a specific position of the linked list
        new_node = Node(data)
        counter_index = 0
        temp = self.head
        if index >= self.length:
            self.append(data)
            return 
        if index == 0:
            self.preappend(data)
            return 
        while counter_index < self.length:
            if counter_index == index-1:
                temp.next, new_node.next = new_node, temp.next
                self.length += 1
            temp = temp.next
            counter_index += 1
        
    def remove(self, index):
        temp = self.head
        counter_index = 0
        if index >= self.length:
            print('index out of range')
        
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return 
        
        while counter_index < self.length:
            if counter_index == index-1:
                temp.next = temp.next.next
                self.length -= 1 
                break
            counter_index += 1
        
    def print_linked_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        print('Lenght = ' + str(self.length))

    def invert_list(self):
        prev = None
        self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp


ll = LinkedList()
ll.append(55)
ll.append(5)
ll.append(34)
ll.preappend(3)
ll.insert(4, 100)
ll.remove(2)
ll.invert_list()
ll.print_linked_list()