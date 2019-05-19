class Node:
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def insert_node_in_sub_tree(root, node):
        """Given a root node and node to be inserted, this function inserts node at correct position"""
        if node.id >= root.id:
            if root.right is None:
                root.right = node
                return
            else:
                return BinaryTree.insert_node_in_sub_tree(root.right, node)
        else:
            if root.left is None:
                root.left = node
                return
            else:
                return BinaryTree.insert_node_in_sub_tree(root.left, node)

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("You can insert objects of type Node")

        if self.root is None:
            self.root = node
        else:
            BinaryTree.insert_node_in_sub_tree(self.root, node)

    def delete(self, id):
        pass


bt = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(5)
n4 = Node(6)

bt.insert(n1)
bt.insert(n2)
bt.insert(n3)
bt.insert(n4)
print("Ends here")
