class Node:  # A node holding one BST value.
     def __init__(self, value):  # Build the node.
         self.value = value  # Set its key.
         self.left = None  # Smaller subtree starts empty.
         self.right = None  # Larger subtree starts empty.

def insert(root, value):  # Return the updated root.
      if root is None:  # Empty position reached.
          return Node(value)  # Create a leaf.
      if value < root.value:  # Smaller values go left.
          root.left = insert(root.left, value)  # Update right branch
      elif value > root.value:  # Larger values go right.
          root.right = insert(root.right, value)  # Update right branch.
      return root  # Ignore a duplicate in this version.

def contains(root, value):  # Test membership.
     while root is not None:  # Follow one branch per step.
            if value == root.value:  # Match found.
                return True # Report success.
            root = root.left if value < root.value else root.right  # Choose side.
     return False  # We reached an empty branch.    
   
def inorder(root):  # Display sorted BST keys.
     if root is None:  # Empty subtree.
          return []  # No values.
     return inorder(root.left) + [root.value] + inorder(root.right)  # Walk.

root = None  # Start with an empty tree.  
for key in [8, 3, 10, 1, 6]:  # Insert keys in order.
    root = insert(root, key)  # Keep the returned root.
print(inorder(root))  # Sorted keys.
print(contains(root, 6), contains(root, 9))  # Present, absent.