class Node:  # Represent one binary-tree position.
     def __init__(self, value):  # Initialize a new node.
         self.value = value  # Store its label.
         self.left = None  # No left child yet.
         self.right = None  # No right child yet.

def inorder(node):  # Visit left, root, right.
    if node is None:  # Stop at an empty child.
        return []  # Empty subtree contributes nothing.
    return inorder(node.left) + [node.value] + inorder(node.right)  # Combine.


def preorder(node):  # Visit root before its children.
    if node is None:  # Stop at an empty child.
        return []  # Empty subtree contributes nothing.
    return [node.value] + preorder(node.left) + preorder(node.right)  # Combine.


def postorder(node):  # Visit root after its children.
    if node is None:  # Stop at an empty child.
        return []  # Empty subtree contributes nothing.
    return postorder(node.left) + postorder(node.right) + [node.value]  # Combine.

root = Node(8)  # Make the root.
root.left = Node(3)  # Attach the left child.
root.right = Node(10)#Attach the right child.
print(inorder(root))  # Left-root-right.
print(preorder(root))  # Root-left-right.
print(postorder(root))  # Left-right-root.