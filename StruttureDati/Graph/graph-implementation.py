# Graphs are data structures which contain nodes or vertices, which are connected to each other through edges. Tress
# and Linked Lists are basically graphs having nodes and connections between the nodes. Now, graphs are primarily
# classified by three properties - Cyclic/Acyclic, Weighted/Unweighted/, Directed/Undirected Graphs There are many
# many applications of graphs and many opertions can be performed on them. A graph can be represented in 3 ways -
# Adjacency List, Adjacency Matrix, Edge List. Adjacency list stores the nodes with which a particular node is
# connected to in a linked list or array. All these lists or arrays can be stored in a hash table with the keys being
# the nodes and the values being their respective lists Adjcaency matrix is a nXn matrix where n is the number of
# nodes. M[i][j] = 1 if nodes i and j are connected otherwise 0 Edge list contains all the pairs of nodes which are
# connected, and if the graph is weighted, then the weight of each edge as well Here we will build an undirected
# graph using an adjacency list.
class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacency_list = {}

    # We will add the value of the node as a key in the adjacency list and initialize the value of the key to be an
    # empty array
    def insert_node(self, data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1

    # First we will check if an edge already exists by checking the adjacency list of either of the two nodes.
    # If the other node is present it means the edge already exists, if not then the edge doesn't exist.
    # So we add the edge by adding the complimentary node in the adjacency list of either node
    def insert_edge(self, node1, node2):
        if node2 not in self.adjacency_list[node1]:
            self.adjacency_list[node1].append(node2)
            self.adjacency_list[node2].append(node1)
            return
        return "Edge already exists"

    def show_connection(self):
        for node in self.adjacency_list:
            print(f'{node} --> {" ".join(map(str, self.adjacency_list[node]))}')


my_graph = Graph()
my_graph.insert_node(1)
my_graph.insert_node(2)
my_graph.insert_node(3)
my_graph.insert_edge(1, 2)
my_graph.insert_edge(2, 3)
my_graph.insert_edge(1, 3)
print("This is the undirected graph")
my_graph.show_connection()
