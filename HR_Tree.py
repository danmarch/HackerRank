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
    def _preOrder(node):
        if node == None:
            return
        print_lst.append(node.data)
        _preOrder(node.left)
        _preOrder(node.right)
    _preOrder(root)
    print(*print_lst,sep=" ")

def postOrder(root):
    """Prints out the post-order of the nodes of a binary search tree as a
    string in a single line.
    @param root: The root node of the BST."""
    print_lst = []
    def _postOrder(node):
        if node == None:
            return
        _postOrder(node.left)
        _postOrder(node.right)
        print_lst.append(node.data)
    _postOrder(root)
    print(*print_lst,sep=" ")

def inOrder(root):
    """Prints out the in-order of the nodes of a binary search tree as a string
    in a single line.
    @param root: The root node of the BST."""
    print_lst = []
    def _inOrder(node):
        if node == None:
            return
        _inOrder(node.left)
        print_lst.append(node.data)
        _inOrder(node.right)
    _inOrder(root)
    print(*print_lst,sep=" ")

def height(root):
    """Returns the height of a binary search tree.
    @param root: The root of the BST."""
    if root == None or (root.left == None and root.right == None):
        return 0
    return 1 + max(height(root.left),height(root.right))

def levelOrder(root):
    """Prints out the level-order of the nodes of a binary search tree as a
    string in a single line. Implements the ADT queue with a list.
    @param root: The root node of the BST."""
    if root == None:
        return
    print_lst = []
    qu = []
    qu.append(root)
    while len(qu) > 0:
        new_item = qu[0]
        qu = qu[1:]
        print_lst.append(new_item.data)
        if new_item.left != None:
            qu.append(new_item.left)
        if new_item.right != None:
            qu.append(new_item.right)
    print(*print_lst,sep=" ")
