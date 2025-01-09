from tree import BinaryTree

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(8)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)
    
    for value in reversed(tree):
        print(value)