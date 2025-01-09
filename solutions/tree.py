# Credit: This code was created with the assistance of GitHub Copilot.
# Date: 4-10-2024

class BinaryTree:
    """ Binary Tree - implements key operations of the binary tree data structure
    
    Methods
    -------
    insert(value)
        Adds a node to the binary tree with the provided value.
    remove(value)
        Removes a node with the provided value from the binary tree.
    contains(value)
        Returns True if the binary tree contains a node with the provided value. Otherwise, returns False.
    height(node)
        Returns the height of the binary tree with the passed node for a root.
    size()
        Returns the number of nodes in the binary tree.
    empty()
        Returns True if binary tree is empty. Otherwise, returns False.
    __iter__()
        Returns an iterator to traverse the binary tree in order.
    __reversed__()
        Returns an iterator to traverse the binary tree in reverse order.

    Attributes
    ----------
    root : Node
        The root node of the binary tree.
    size : int
        The number of nodes in the binary tree.
    """

    class Node:
        """ Node - represents a node in the binary tree.
        Attributes
        ----------
        value : any
            The value stored in the node.
        left_child : Node
            The left child of the node.
        right_child : Node
            The right child of the node.
        """
        def __init__(self, value):
            self.value = value
            self.left_child = None
            self.right_child = None

    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, value):
        """Adds a node to the binary tree with the provided value.

        Parameters
        ----------
        value : any
            The value to be added to the binary tree
        """
        # Create a new node with the provided value
        new_node = self.Node(value)
        # If the binary tree is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            # Increment the size of the binary tree
            self._size += 1
        else:
            # Otherwise, insert the new node into the binary tree using a helper method
            self._insert(self.root, new_node)
    
    def _insert(self, current_node, new_node):
        # If the value of the new node is less than the value of the current node
        if new_node.value < current_node.value:
            # If the left child of the current node is None, set the new node as the left child
            if current_node.left_child is None:
                current_node.left_child = new_node
                self._size += 1
            # Otherwise, recursively insert the new node into the left subtree
            else:
                self._insert(current_node.left_child, new_node)
        # If the value of the new node is greater than the value of the current node
        elif new_node.value > current_node.value:
            # If the right child of the current node is None, set the new node as the right child
            if current_node.right_child is None:
                current_node.right_child = new_node
                self._size += 1
            # Otherwise, recursively insert the new node into the right subtree
            else:
                self._insert(current_node.right_child, new_node)

        # If the value is equal to the current node, we do nothing
                
    def remove(self, value):
        """Removes a node with the provided value from the binary tree.

        Parameters
        ----------
        value : any
            The value to be removed from the binary tree
        """
        # We call a helper method to remove the node with the provided value
        self.root = self._remove(self.root, value)

        

    def _remove(self, current_node, value):
        # If the current node is None, we return None. The value is not found in the binary tree.
        if current_node is None:
            return None
        
        # If the value is less than the value of the current node, we recursively remove the value from the left subtree
        if value < current_node.value:
            current_node.left_child = self._remove(current_node.left_child, value)
        # If the value is greater than the value of the current node, we recursively remove the value from the right subtree
        elif value > current_node.value:
            current_node.right_child = self._remove(current_node.right_child, value)
        # If the value is equal to the value of the current node, we remove the current node
        else:
            # We adjust the size of the binary tree
            self._size -= 1

            # Then do the actual removal
            # If there is a child missing, we can simply return the other child whether it exists or not
            if current_node.left_child is None:
                return current_node.right_child
            elif current_node.right_child is None:
                return current_node.left_child
            # If both children exist, we shift the right child up and set the left child as the left child of the right child
            else:
                current_node.value = current_node.right_child.value
                current_node.right_child = self._remove(current_node.right_child, current_node.value)
                # We must adjust the size since the remove helper method will decrement the size even though the number of nodes is unchanged
                self._size += 1
            
        # Always return the current node if it is not removed
        return current_node

    def contains(self, value):
        """Returns True if the binary tree contains a node with the provided value. Otherwise, returns False.

        Parameters
        ----------
        value : any
            The value to be checked in the binary tree
        """
        # We call a helper method to check if the binary tree contains the value
        return self._contains(self.root, value)
    
    def _contains(self, current_node, value):
        # If the current node is None, the value is not found in the binary tree
        if current_node is None:
            return False
        # If the value is less than the value of the current node, we recursively search in the left subtree
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        # If the value is greater than the value of the current node, we recursively search in the right subtree
        elif value > current_node.value:
            return self._contains(current_node.right_child, value)
        # If the value is equal to the value of the current node, we have found the value
        else:
            return True
        
    def height(self, node=None):
        """Returns the height of the binary tree with the passed node for a root.

        Parameters
        ----------
        node : Node
            The root node of the binary tree. If not provided, the root of the binary tree is used.
        """
        # If a specific node is not provided, default to the root of the binary tree
        if node is None:
            node = self.root
        # We call a helper method to calculate the height of the binary tree
        return self._height(node)
    
    def _height(self, current_node):
        # If the current node is None, return -1 to offset the height calculation
        if current_node is None:
            return -1
        # Recursively calculate the height of the left and right subtrees
        left_height = self._height(current_node.left_child)
        right_height = self._height(current_node.right_child)
        # Return the maximum height of the left and right subtrees plus 1 for the current node
        return 1 + max(left_height, right_height)
    
    def size(self):
        """Returns the number of nodes in the binary tree."""
        return self._size
                
    def empty(self):
        """Returns True if binary tree is empty. Otherwise, returns False."""
        return self._size == 0
    
    def __iter__(self):
        return self._traverse_in_order(self.root)
    
    def _traverse_in_order(self, current_node):
        if current_node is not None:
            # First yield from the left subtree
            yield from self._traverse_in_order(current_node.left_child)
            # Then yield the value of the current node
            yield current_node.value
            # Finally, yield from the right subtree
            yield from self._traverse_in_order(current_node.right_child)

    def __reversed__(self):
        return self._traverse_reverse_order(self.root)
    
    def _traverse_reverse_order(self, current_node):
        if current_node is not None:
            # First yield from the right subtree
            yield from self._traverse_reverse_order(current_node.right_child)
            # Then yield the value of the current node
            yield current_node.value
            # Finally, yield from the left subtree
            yield from self._traverse_reverse_order(current_node.left_child)


if __name__ == "__main__":
    # Test Cases
    binary_tree = BinaryTree()
    print("Is Binary Tree Empty:", binary_tree.empty())
    # Output: True

    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)
    binary_tree.insert(2)

    print("In Order Traversal:")
    for value in binary_tree:
        print(value)
    # Output: 1, 2, 3, 4, 5, 7, 8, 9
        
    print("Reverse Order Traversal:")
    for value in reversed(binary_tree):
        print(value)
    # Output: 9, 8, 7, 5, 4, 3, 2, 1
    
    print("Height of the Binary Tree:", binary_tree.height())
    # Output: 3

    print("Size of the Binary Tree:", binary_tree.size())
    # Output: 8

    print("Is Binary Tree Empty:", binary_tree.empty())
    # Output: False

    print("Does Binary Tree Contain 7:", binary_tree.contains(7))
    # Output: True

    print("Does Binary Tree Contain 6:", binary_tree.contains(6))
    # Output: False

    binary_tree.remove(7)
    binary_tree.remove(3)

    print("In Order Traversal:")
    for value in binary_tree:
        print(value)
    # Output: 1, 2, 4, 5, 8, 9
        
    print("Size of the Binary Tree:", binary_tree.size())
    # Output: 6

