# Linked lists are, as the name suggests, a list which is linked. It consists of nodes which contain data and a
# pointer to the next node in the list. The list is connected with the help of these pointers. These nodes are
# scattered in memory, quite like the buckets in a hash table. The node where the list starts is called the head of
# theblist and the node where it ends, or last node, is called the tail of the list. The average time complexity of
# some operations invloving linked lists are as follows: Look-up : O(n) Insert : O(n) Delete : O(n) Append : O(1)
# Prepend : O(1) Python doesn't have a built-in implementation of linked lists, we have to build it on our own

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # this function init the head of the linked list
        self.head = None
        self.tail = None
        self.length = 0

    # For this, we will call the prepend method and pass the value we want to enter, which will create a new object
    # of the node class Then we will make the 'next' of the new node point to the head ,as the head is currently
    # pionting to the first node of the list And then we will update the head to point to new node as we want the new
    # node to be new first node, i.e, the new head. And ofcourse, we'll increase the length by 1
    def preappend(self, data):  # this function insert a new node at the begining of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # To do this, we will just pass the data we want to append. The append method will create a new instance of the
    # Node class, Effectively creating a new node, with the data passed to the instance, so that the new node will
    # contain the data the user wants to enter Then we will check if the list is empty. If it is, we will point the
    # head to the new node just created and the tail to the head, as there is only one node in the list, so the head
    # and tail point to the same node. Also, we will set the length equal to 1. If the list isn't empty, then we will
    # make the 'next' pointer of the last node(pointed at by 'tail') point to the new node And update the tail to
    # point to the new node as this has become the last node in the list now. And we'll increase the length.
    def append(self, data):  # this function insert a new node at the end of the list
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    # If the position is greater than the length of the list, we simply follow the procedure of the append method
    # where we add the node to the end of the list If the position is equal to 0, we follow the prepend procedure,
    # where we append the node at the head If the postition is somewhere in between, then we create a temporary node
    # which traverses the list upto the previous position of the position we want to enter the new node Now the
    # 'next' of the temporary node is pointing to the next node in the list, wehre we want to insert our new node So
    # first we link the new node and the node at the desired position by making the 'next' of the new node equal to
    # the 'next' of the temporary node The temporary node and the new node point to the same position now,
    # the position we want to insert the new node So we update the 'next' of the temporary node to point to the new
    # node. This way, our new node occupies the position it intended to and the node which was originally there,
    # gets pushed to the next position Since this requires traversal of the list, it is an O(n) operation.
    def insert(self, index, data):  # this function insert a new node in a specific position of the linked list
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
            if counter_index == index - 1:
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
            if counter_index == index - 1:
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
