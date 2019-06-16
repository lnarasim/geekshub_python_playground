class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def insert_node_in_sub_tree(root, node):
        """Given a root node and node to be inserted, this function inserts node at correct position"""
        if node.identifier >= root.identifier:
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

    @staticmethod
    def in_order(root):
        if root.left:
            BinaryTree.in_order(root.left)
        print(root.identifier)
        if root.right:
            BinaryTree.in_order(root.right)

    @staticmethod
    def post_order(root):
        if root.left:
            BinaryTree.in_order(root.left)
        if root.right:
            BinaryTree.in_order(root.right)
        print(root.identifier)

    @staticmethod
    def pre_order(root):
        print(root.identifier)
        if root.left:
            BinaryTree.in_order(root.left)
        if root.right:
            BinaryTree.in_order(root.right)

    @staticmethod
    def in_order_successor(root):
        if not root or (not root.left and not root.right):
            return None
        if not root.left:
            return root

    @staticmethod
    def search_node(root, identifier):
        if root is None:
            return None
        if root.identifier == identifier:
            return root
        if identifier > root.identifier:
            return BinaryTree.search_node(root.right, identifier)
        else:
            return BinaryTree.search_node(root.left, identifier)

    def insert(self, node):
        if not isinstance(node, Node):
            raise TypeError("You can insert objects of type Node")

        if self.root is None:
            self.root = node
        else:
            BinaryTree.insert_node_in_sub_tree(self.root, node)

    def delete(self, identifier):
        node_to_be_deleted = None
        parent_node = None


bt = BinaryTree()
n1 = Node(10)
n2 = Node(20)
n3 = Node(5)
n4 = Node(6)

bt.insert(n1)
bt.insert(n2)
bt.insert(n3)
bt.insert(n4)
bt.in_order(bt.root)
print(bt.search_node(bt.root, 6).identifier)
print("Ends here")
