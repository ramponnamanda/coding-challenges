from io.pyprojects.all.BST import BinarySearchTree

if __name__ == '__main__':
    node = BinarySearchTree.init()
    print(node)


def inorderwithoutrecursion(root):
    if root is None:
        return
    stack = []

    while True:
        print(root.data)
        stack.add(root)
        while root.right != None:
            stack.add(root.right)
        # if len(stack)


def checkBST(root):
    result = True
    if root:
        if root.left:
            result &= (root.left.data < root.data) & checkBST(root.left)
        if root.right:
            result &= (root.right.data > root.data) & checkBST(root.right)
    return result
