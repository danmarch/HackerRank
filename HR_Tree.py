#The following functions correspond to the Trees problems from the data
#structures subsection of HackerRank challenges. Solutions by Dan March.

#The functions feature Nodes that are defined as:

# self.left (the left child of the node)
# self.right (the right child of the node)
# self.data (the value of the node)

def preOrder(root):
    """Prints out the pre-order of the nodes of a binary search tree as a string
    in a single line.
    @param root: The root node of the BST."""
    print_lst = []
    def visit(node):
        if node == None:
            return
        print_lst.append(node.data)
        visit(node.left)
        visit(node.right)
    visit(root)
    print(*print_lst,sep=" ")

def postOrder(root):
    """Prints out the post-order of the nodes of a binary search tree as a
    string in a single line.
    @param root: The root node of the BST."""
    print_lst = []
    def visit(node):
        if node == None:
            return
        visit(node.left)
        visit(node.right)
        print_lst.append(node.data)
    visit(root)
    print(*print_lst,sep=" ")

def inOrder(root):
    """Prints out the in-order of the nodes of a binary search tree as a string
    in a single line.
    @param root: The root node of the BST."""
    print_lst = []
    def visit(node):
        if node == None:
            return
        visit(node.left)
        print_lst.append(node.data)
        visit(node.right)
    visit(root)
    print(*print_lst,sep=" ")

def height(root):
    """Returns the height of a binary search tree.
    @param root: The root of the BST."""
    if root == None or (root.left == None and root.right == None):
        return 0
    return 1 + max(height(root.left),height(root.right))
