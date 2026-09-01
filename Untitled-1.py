class BSTNode:    
    def __init__(self, data):    
        self.data  = data    # value stored in this node    
        self.left  = None    # pointer to left child    
        self.right = None    
class BST:    
    def __init__(self):    
        self.root = None     
    def insert(self, data):    
        if self.root is None:    
            self.root = BSTNode(data)    
            print(f"INSERT {data} → Root node created")    
        else:    
            self._insert_recursive(self.root, data)    
         
    def _insert_recursive(self, node, data):    
        if data < node.data:                      # go LEFT    
            if node.left is None:    
                node.left = BSTNode(data)    
                print(f"INSERT {data} → Placed LEFT of {node.data}")    
            else:    
                self._insert_recursive(node.left, data)   # recurse deeper    
        
        elif data > node.data:                    # go RIGHT    
            if node.right is None:    
                node.right = BSTNode(data)    
                print(f"INSERT {data} → Placed RIGHT of {node.data}")    
            else:    
                self._insert_recursive(node.right, data)  # recurse deeper    
         
        else:    
            print(f"INSERT {data} → Duplicate, skipped")    
         
    # INORDER: Left → Root → Right    
    def inorder(self):    
        result = []    
        self._inorder_recursive(self.root, result)    
        return result    
         
    def _inorder_recursive(self, node, result):    
        if node is not None:    
            self._inorder_recursive(node.left, result)   # visit left first    
            result.append(node.data)                     # then current    
            self._inorder_recursive(node.right, result)  # then right    
         
    # PREORDER: Root → Left → Right    
    def preorder(self):    
        result = []    
        self._preorder_recursive(self.root, result)    
        return result    
         
    def _preorder_recursive(self, node, result):    
        if node is not None:    
            result.append(node.data)                      # visit current first    
            self._preorder_recursive(node.left, result)    
            self._preorder_recursive(node.right, result)    
         
    # POSTORDER: Left → Right → Root    
    def postorder(self):    
        result = []    
        self._postorder_recursive(self.root, result)    
        return result    
         
    def _postorder_recursive(self, node, result):    
        if node is not None:    
            self._postorder_recursive(node.left, result)    
            self._postorder_recursive(node.right, result)    
            result.append(node.data)                      # visit current last    
         
    def search(self, data):    
        return self._search_recursive(self.root, data, steps=[])    
         
    def _search_recursive(self, node, data, steps):    
        if node is None:    
            steps.append("NOT FOUND")    
            return False, steps    
        steps.append(f"Visit {node.data}")    
        if data == node.data:    
            steps.append(f"FOUND {data}!")    
            return True, steps    
        elif data < node.data:    
            steps.append(f"{data} < {node.data} → go LEFT")    
            return self._search_recursive(node.left, data, steps)    
        else:    
            steps.append(f"{data} > {node.data} → go RIGHT")    
            return self._search_recursive(node.right, data, steps)    
         
def height(self):    
    return self._height_recursive(self.root)    
         
def _height_recursive(self, node):    
    if node is None:    
        return 0    
    left_height  = self._height_recursive(node.left)    
    right_height = self._height_recursive(node.right)    
    return 1 + max(left_height, right_height)    
         
# --- Test ---    
bst = BST()    
         
print("Step 1: Insert nodes")    
for v in [50, 30, 70, 20, 40, 60, 80]:    
    bst.insert(v)    
         
print("""    
Step 2: Tree structure    
         50          ← Root    
        /  \\    
      30    70    
     / \\   / \\    
    20  40 60  80    
""")    
         
print("Step 3: Inorder (Left→Root→Right)")    
print("Result:", bst.inorder())    
print("NOTE: Inorder of BST always gives SORTED output!")    
         
print("\nStep 4: Preorder (Root→Left→Right)")    
print("Result:", bst.preorder())    
         
print("\nStep 5: Postorder (Left→Right→Root)")    
print("Result:", bst.postorder())    
         
print("\nStep 6: Search with step trace")    
found, steps = bst.search(40)    
print("Searching for 40:")    
for step in steps:    
    print(f"  → {step}")    
         
found2, steps2 = bst.search(55)    
print("\nSearching for 55:")    
for step in steps2:    
    print(f"  → {step}")    
         
print(f"\nStep 7: Tree height = {bst.height()}")    
         
print("\nStep 8: Insert more, verify inorder stays sorted")    
for v in [25, 45, 65]:    
    bst.insert(v)    
print("Inorder:", bst.inorder())