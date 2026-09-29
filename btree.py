class Node:  # A B-tree node holding several keys.
    def __init__(self, leaf=True):  # Create a new node.
        self.keys = []  # Sorted keys in this node.
        self.children = []  # Child pointers between keys.
        self.leaf = leaf  # Mark whether there are children.
class BTree:  # Minimum degree 2: at most three keys per node.
    def __init__(self):  # Start an empty tree.
        self.root = Node()  # An empty leaf is the root.
    def split(self, parent, index):  # Split one full child.
        full = parent.children[index]  # Identify the full node.
        right = Node(full.leaf)  # Create a sibling.
        middle = full.keys[1]  # Median moves upward.
        right.keys = full.keys[2:]  # Larger keys move right.
        full.keys = full.keys[:1]  # Smaller key stays left.
        if not full.leaf:  # Internal nodes also have children.
            right.children = full.children[2:]  # Move right children.
            full.children = full.children[:2]  # Keep left children.
        parent.keys.insert(index, middle)  # Promote median.
        parent.children.insert(index + 1, right)  # Attach sibling.
    def insert_nonfull(self, node, key):  # Descend into nonfull node.
        if node.leaf:  # Leaf receives the key.
            node.keys.append(key)  # Add at the end.
            node.keys.sort()  # Restore sorted order.
            return  # Insertion complete.
        i = 0  # Find a suitable child interval.
        while i < len(node.keys) and key > node.keys[i]:  # Scan separators.
            i += 1  # Move right.
        if len(node.children[i].keys) == 3:  # Child is full.
            self.split(node, i)  # Split before descent.
            if key > node.keys[i]:  # Median changed the boundary.
                i += 1  # Enter the new right child.
        self.insert_nonfull(node.children[i], key)  # Continue downward.
    def insert(self, key):  # Add a distinct integer key.
        if self.search(self.root, key):  # This version rejects duplicates.
            return  # Keep unique keys only.
        if len(self.root.keys) == 3:  # Root is full.
            old = self.root  # Keep its pointer.
            self.root = Node(False)  # Grow tree height.
            self.root.children = [old]  # Old root becomes child.
            self.split(self.root, 0)  # Split old root.
        self.insert_nonfull(self.root, key)  # Insert below root.
    def search(self, node, key):  # Look for a key.
        i = 0  # Start at the first separator.
        while i < len(node.keys) and key > node.keys[i]:  # Skip smaller keys.
            i += 1  # Move to next position.
        if i < len(node.keys) and key == node.keys[i]:  # Found key.
            return True  # Success.
        return False if node.leaf else self.search(node.children[i], key)  # Descend.
    def levels(self):  # Show each level for checking.
        queue = [self.root]  # Start at root.
        while queue:  # Continue until all nodes are visited.
            print([node.keys for node in queue])  # Print this level.
            queue = [child for node in queue for child in node.children]  # Next.
bt = BTree()  # Build an order-4 B-tree.
for key in [10, 20, 5, 6]:  # Insert test keys.
    bt.insert(key)  # Insert one by one.
bt.levels()  # Show the structure.
print(bt.search(bt.root, 6), bt.search(bt.root, 9))  # Membership.