class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root
        self.number_of_nodes = 0

    def lookup(self, data):
        if self.root == None:
            return 'Tree is empty'
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    return 'Value not found'
                if current_node.data == data:
                    return f'Found value {data}'
                elif current_node.data > data:
                    current_node = current_node.left
                elif current_node.data < data:
                    current_node = current_node.right

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes +=1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.value > current_node.