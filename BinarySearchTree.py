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


def insertwithoutrec(root, key):
    if root is None:
        return Node(key)

    temp = root
    while temp:
        if temp.data > key:
            if temp.left :
                temp = temp.left
            else:
                temp.left = Node(key)
                break

        elif temp.data < key:
            if temp.right:
                temp = temp.right
            else:
                temp.right = Node(key)
                break
        else:
            break;
    return root


def inorderwithoutrecursion(root):
    stack = []
    stack.push(root)
    while stack:



def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


def delete(root, key):
    if root is None:
        return root

    if root.data < key:
        root.right = delete(root.right, key)
    elif root.data > key:
        root.left = delete(root.left, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = inorderSuccessor(root)
        root.right = delete(root.right, successor.data)
        successor.right = root.right
        successor.left = root.left
        return successor
    return root


def inorderSuccessor(root):
    temp = root.right
    while temp.left is not None:
        temp = temp.left
    return temp


if __name__ == '__main__':
    data = [50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90]
    rootNode = None
    for key in data:
        rootNode = insertwithoutrec(rootNode, key)

    inorder(rootNode)

    delete(rootNode, 70)
    delete(rootNode, 75)
    print("updated tree")

    inorder(rootNode)
