class Node: # Store AVL key, children and height.
    def __init__(self, key):  # Create a leaf.
        self.key = key  # Store key.
        self.left = self.right = None  # Start without children.
        self.height = 1  # A leaf has height one.

def height(n):  # Read height safely.
    return n.height if n else 0  # Empty tree height is zero.

def update(n):  # Recompute height after a change.
    n.height = 1 + max(height(n.left), height(n.right))  # Taller side wins.

def rotate_right(y):  # Repair a left-heavy subtree.
    x = y.left  # New root is old left child.
    middle = x.right  # Save its right branch.
    x.right = y  # Move old root down to the right.
    y.left = middle  # Reattach the saved branch.
    update(y)  # Repair lower height first.
    update(x)  # Then new root height.
    return x  # Hand back the new root.

def rotate_left(x):  # Mirror of right rotation.
    y = x.right  # New root is old right child.
    middle = y.left  # Save its left branch.
    y.left = x  # Move old root down to left.
    x.right = middle  # Reattach saved branch.
    update(x)  # Repair lower height first.
    update(y)  # Then new root height.
    return y  # Hand back new root.

def insert(n, key):  # Insert and restore AVL balance.
    if n is None:  # Found an empty position.
        return Node(key)  # Make a leaf.
    if key < n.key:  # Search the left side.
        n.left = insert(n.left, key)  # Insert recursively.
    elif key > n.key:  # Search the right side.
        n.right = insert(n.right, key)  # Insert recursively.
    else:  # Duplicate key.
         return n  # Ignore duplicates.

    update(n)  # Children changed: refresh height.
    balance = height(n.left) - height(n.right)  # Left minus right.
    if balance > 1:  # Left side too tall.
        if key > n.left.key:  # Left-right case.
            n.left = rotate_left(n.left)  # Convert to left-left.

        return rotate_right(n)  # Fix left-heavy case.
    if balance < -1:  # Right side too tall.
        if key < n.right.key:  # Right-left case.
            n.right = rotate_right(n.right)  # Convert to right-right.
        return rotate_left(n)  # Fix right-heavy case.
    return n  # Balanced root stays unchanged.

root = None  # Start empty.
for key in [30, 20, 10]:  # Trigger LL rotation.  
    root = insert(root, key)  # Keep a possibly new root.
print(root.key, root.left.key, root.right.key)  # Balanced shape.