#!/bin/python3
#--------------------------------------------------------
# Program by Bruce Wayne
#
#
# Version   Date    Info
# 1.0       2023    Initial Version
# 1.1       2024    Bug fix
#--------------------------------------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value) if root_value is not None else None
    
    def insert(self, value):
        """Insert a value into the binary tree using level-order insertion"""
        if self.root is None:
            self.root = TreeNode(value)
            return
        
        from collections import deque
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            
            if current.left is None:
                current.left = TreeNode(value)
                return
            queue.append(current.left)
            
            if current.right is None:
                current.right = TreeNode(value)
                return
            queue.append(current.right)
    
    def search(self, value):
        """Search for a value in the tree using BFS"""
        if self.root is None:
            return False
            
        from collections import deque
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            if current.value == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False
    
    def traverse(self, mode='inorder'):
        """Perform tree traversal with different modes"""
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.value
                yield from _inorder(node.right)
        
        def _preorder(node):
            if node:
                yield node.value
                yield from _preorder(node.left)
                yield from _preorder(node.right)
        
        def _postorder(node):
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.value
        
        def _levelorder():
            if self.root is None:
                return
            from collections import deque
            queue = deque([self.root])
            while queue:
                current = queue.popleft()
                yield current.value
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        
        traversals = {
            'inorder': _inorder,
            'preorder': _preorder,
            'postorder': _postorder,
            'levelorder': _levelorder
        }
        
        if mode not in traversals:
            raise ValueError(f"Invalid traversal mode. Choose from {list(traversals.keys())}")
        
        return list(traversals[mode](self.root)) if mode != 'levelorder' else list(_levelorder())
    
    def height(self):
        """Calculate height of the tree"""
        def _height(node):
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
    
    def size(self):
        """Count all nodes in the tree"""
        def _size(node):
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)
    
    def __str__(self):
        """String representation of the tree (level order)"""
        return ' '.join(map(str, self.traverse('levelorder')))

if __name__ == "__main__":
    # Create and populate the tree
    tree = BinaryTree(10)
    for value in [5, 15, 3, 7, 12, 18]:
        tree.insert(value)
    
    # Demonstrate functionality
    print("Inorder Traversal:", tree.traverse('inorder'))
    print("Preorder Traversal:", tree.traverse('preorder'))
    print("Postorder Traversal:", tree.traverse('postorder'))
    print("Level Order Traversal:", tree.traverse('levelorder'))
    print("\nSearch for 7:", tree.search(7))
    print("Search for 20:", tree.search(20))
    print("Tree height:", tree.height())
    print("Total nodes:", tree.size())
    print("\nString representation (level order):", tree)
