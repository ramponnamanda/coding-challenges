class Node:

    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None


def insert(root, key):
    if root is None :
        return Node(key)

    if root.data < key:
        root.right = insert(root.right, key)
    elif root.data > key:
        root.left = insert(root.left, key)

    return root


class BinarySearchTree:
    @staticmethod
    def init():
        sampledata = [50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90]
        rootnode = None
        for item in sampledata:
            rootnode = insert(rootnode, item)
        return rootnode


if __name__ == '__main__':
    data = [50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90]
    rootNode = None
    for key in data:
        rootNode = insert(rootNode, key)

