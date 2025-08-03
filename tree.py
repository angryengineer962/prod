#!/bin/python3
#--------------------------------------------------------
# Program by Bruce Wayne
#
#
# Version   Date    Info
# 1.0       2023    Initial Version
#
#--------------------------------------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    def insert(self, value):
        """Insert a value into the binary tree"""
        if not self.root:
            self.root = TreeNode(value)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            
            if not current.left:
                current.left = TreeNode(value)
                return
            else:
                queue.append(current.left)
                
            if not current.right:
                current.right = TreeNode(value)
                return
            else:
                queue.append(current.right)
    
    def search(self, value):
        """Search for a value in the tree (BFS)"""
        if not self.root:
            return False
            
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False
    
    def inorder_traversal(self, node):
        """Left -> Root -> Right"""
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        """Root -> Left -> Right"""
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        """Left -> Right -> Root"""
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')
    
    def level_order_traversal(self):
        """Breadth-First Search (level order)"""
        if not self.root:
            return
            
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    def height(self, node):
        """Calculate height of the tree"""
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def count_nodes(self, node):
        """Count all nodes in the tree"""
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(3)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)
    
    print("Inorder Traversal:")
    tree.inorder_traversal(tree.root)
    print("\n\nPreorder Traversal:")
    tree.preorder_traversal(tree.root)
    print("\n\nPostorder Traversal:")
    tree.postorder_traversal(tree.root)
    print("\n\nLevel Order Traversal:")
    tree.level_order_traversal()
    
    print("\n\nSearch for 7:", tree.search(7))
    print("Search for 20:", tree.search(20))
    print("Tree height:", tree.height(tree.root))
    print("Total nodes:", tree.count_nodes(tree.root))
