class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root
        self.number_of_nodes = 0

    def __str__(self):
        return str(self.__dict__)

    def lookup(self, data):
        if self.root is None:
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

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.number_of_nodes += 1
            return
        else:
            current_node = self.root
            while (current_node.left != new_node) and (current_node.right != new_node):
                if new_node.data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                    else:
                        current_node = current_node.right
                elif new_node.data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                    else:
                        current_node = current_node.left
        self.number_of_nodes += 1
        return

    def remove(self, data):
        if self.root is None:
            return 'Tree is empty'
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if current_node.data > data:
                # current node is greater then the value we are looking for so check to the left
                parent_node = current_node
                current_node = current_node.left
            elif current_node.data < data:
                # current node is less then the value we are looking for so check into the right
                parent_node = current_node
                current_node = current_node.right
            else:  # we found the node the we wanna delete but we have to manage multiple cases
                if current_node.right is None:  # the node we want to delete have only a left child
                    if parent_node is None:
                        self.root = current_node.left
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.left
                            return
                        else:
                            parent_node.right = current_node.left
                            return
                elif current_node.left is None:  # the node we want to delete have only a right child
                    if parent_node is None:
                        self.root = current_node.right
                        return
                    else:
                        if parent_node.data > current_node.data:
                            parent_node.left = current_node.right
                            return
                        else:
                            parent_node.right = current_node.right7
                elif current_node.left is None and current_node.right is None:  #the node has no child
                    if parent_node is None:
                        current_node = None
                        return
                    if parent_node.data > current_node:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
