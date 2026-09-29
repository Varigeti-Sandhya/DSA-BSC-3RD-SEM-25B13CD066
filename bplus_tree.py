class Leaf:  # Store actual record keys in a leaf.
    def __init__(self, keys):  # Build a leaf page.
        self.keys = keys  # Sorted values live here.
        self.next = None  # Link to the next leaf.
class Internal:  # Route requests to children.
    def __init__(self, children):  # Build an internal page.
        self.children = children  # Keep child pages.
        self.keys = [first(c) for c in children[1:]]  # Separators.
def first(node):  # Find the smallest key below a page.
    while isinstance(node, Internal):  # Descend through internal pages.
        node = node.children[0]  # Follow leftmost child.
    return node.keys[0]  # First leaf key.
def build(keys, leaf_size=2, fanout=3):  # Bulk-load distinct sorted keys.
    keys = sorted(set(keys))  # Sort and remove duplicates.
    if not keys:  # Empty index has no root.
        return None  # Nothing to search.
    leaves = [Leaf(keys[i:i + leaf_size]) for i in range(0, len(keys), leaf_size)]  # Chunk.
    for left, right in zip(leaves, leaves[1:]):  # Link adjacent leaves.
        left.next = right  # Enable range scans.
    level = leaves  # Begin at the leaf level.
    while len(level) > 1:  # Build parent levels.
        level = [Internal(level[i:i + fanout]) for i in range(0, len(level), fanout)]  # Group.
    return level[0]  # Root of the index.
def leaf_for(root, key):  # Locate candidate leaf.
    node = root  # Begin at root.
    while isinstance(node, Internal):  # While not at a leaf.
        i = 0  # Begin at first child.
        while i < len(node.keys) and key >= node.keys[i]:  # Compare separators.
            i += 1  # Move right.
        node = node.children[i]  # Descend into chosen child.
    return node  # Return the leaf.
def range_keys(root, low, high):  # Return keys in a closed interval.
    if root is None:  # Handle an empty tree.
        return []  # No matches.
    node = leaf_for(root, low)  # Start near lower bound.
    result = []  # Collect matches.
    while node is not None:  # Walk linked leaves.
        for key in node.keys:  # Inspect keys in this leaf.
            if key > high:  # Past the upper bound.
                return result  # Stop early.
            if key >= low: # Within both bounds.
                result.append(key)  # Keep it.
        node = node.next  # Continue along the leaf chain.
    return result  # Return matching keys.
root = build([2, 5, 8, 11, 14, 17])  # Bulk-load the demo.
print(root.keys)  # Root separators.
print(11 in leaf_for(root, 11).keys)  # Exact membership.
print(range_keys(root, 5, 14))  # Range scan.