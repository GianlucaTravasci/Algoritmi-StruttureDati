# Binary trees implementation for start the BFS algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

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
                            parent_node.right = current_node.right
                elif current_node.left is None and current_node.right is None:  # the node has no child
                    if parent_node is None:
                        current_node = None
                        return
                    if parent_node.data > current_node:
                        parent_node.left = None
                        return
                    else:
                        parent_node.right = None
                        return
                elif current_node.left is not None and current_node.right is not None:  # node has left and rigth child
                    del_node = current_node.right
                    del_node_parent = current_node.right
                    while del_node.left is not None:  # loop to reach the left most node of the right subtree of the current node
                        del_node_parent = del_node
                        del_node = del_node.left
                    current_node.data = del_node.data  # the value to be replaced
                    if del_node == del_node_parent:  # if the node to be replaced is the exact right of the current node
                        current_node.right = del_node.right
                        return
                    if del_node.right is None:  # if the left most node of the right subtree of the current node has
                        # no right subtree
                        del_node_parent.left = None
                    else:  # if it has a right subtree, we simply link it to the parent of the del_node
                        del_node_parent.left = del_node.right
                        return
        return 'Not Found'

    