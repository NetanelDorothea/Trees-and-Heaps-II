class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, doctor, report, side, current_node=None):
        """inserts doctors"""
    # Case 1: Empty Tree
        if self.root is None:
            print("Tree is empty. Cannot insert without root")
            return False
        
        if side not in ["left", "right"]:
            print(f"Invalid side: {side}. Use 'left' or 'right'.")
            return False
    
        # Start from root if not part of recursive call
        if current_node is None:
            current_node = self.root 
    
        # Case 2: Found the parent node
        if current_node.name == doctor: 
            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(report) 
                print(f"✅ {report} added under {doctor} on the left.") 
                return True 
            elif side == "right" and current_node.right is None: 
                current_node.right = DoctorNode(report) 
                print(f"✅ {report} added under {doctor} on the right.") 
                return True 
            else: 
                print(f"{doctor} already has a {side} subordinate.") 
                return False
        
        # Case 3: Search the subtrees
        found_left = False
        found_right = False
        
        if current_node.left:
            found_left = self.insert(doctor, report, side, current_node.left)
        
        if current_node.right and not found_left:
            found_right = self.insert(doctor, report, side, current_node.right)
        
        # Case 4: Parent node not found
        if not(found_left or found_right):
            # Only print if we are at the root of the search to avoid multiple messages
            if current_node == self.root:
                print(f"Doctor {doctor} not found in the tree")
            return False
    
        return True
    
    def preorder(self, node):
        """a tree traversal method that follows a Root-Left-Right order"""
        if node is None: # Base case, we've reached a leaf
            return []
        result = [node.name]
        # Recursive cases to append list 
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        # Return the result
        return result
    
    def inorder(self, node):
        """a tree traversal method that follows a Left-Root-Right order"""
        if node is None: # Base case, we've reached a leaf
            return []
        result = []
        result += self.inorder(node.left)
        result.append(node.name)
        result += self.inorder(node.right)

        return result

    def postorder(self, node):
        """a tree traversal method that follows a Left-Right-Root order"""
        if node is None: # Base case, we've reached a leaf
            return []
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.name)

        return result

# Test your DoctorTree and DoctorNode classes here

tree = DoctorTree()
tree.root = DoctorNode("Dr. Smith")

tree.insert("Dr. Smith", "Dr. Adams", "left") # ✅ Dr. Adams added under Dr. Smith on the left.
tree.insert("Dr. Smith", "Dr. Brown", "right") # ✅ Dr. Brown added under Dr. Smith on the right.
tree.insert("Dr. Adams", "Dr. Clark", "left") # ✅ Dr. Clark added under Dr. Adams on the left.
tree.insert("Dr. Unknown", "Dr. White", "left") # Doctor Dr. Unknown not found in the tree
tree.insert("Dr. Smith", "Dr. Wilson", "left") # Dr. Smith already has a left subordinate.
tree.insert("Dr. Brown", "Dr. Taylor", "middle") # Invalid side: middle. Use 'left' or 'right'.
print("Preorder:", tree.preorder(tree.root)) # Preorder: ['Dr. Smith', 'Dr. Adams', 'Dr. Clark', 'Dr. Brown']
print("Inorder:", tree.inorder(tree.root)) # Inorder: ['Dr. Clark', 'Dr. Adams', 'Dr. Smith', 'Dr. Brown']
print("Postorder:", tree.postorder(tree.root)) # Postorder: ['Dr. Clark', 'Dr. Adams', 'Dr. Brown', 'Dr. Smith']