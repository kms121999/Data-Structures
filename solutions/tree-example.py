from tree import BinaryTree

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(8)

    print(tree.contains(3))