import queue

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


def topview(root):
    if root is None:
        return

    q = queue.Queue()
    q.put([root, 0])

    hdmap = {}

    while not q.empty():
        qobj = q.get()
        obj = qobj[0]
        dis = qobj[1]
        if hdmap.get(dis) is None:
            print(obj.data)
            hdmap[dis] = obj
        if obj.left:
            q.put([obj.left, dis - 1])
        if obj.right:
            q.put([obj.right, dis + 1])


if __name__ == '__main__':
    data = [50, 25, 75, 15, 35, 65, 85, 10, 20, 30, 40, 60, 70, 80, 90]
    rootNode = None
    for key in data:
        rootNode = insert(rootNode, key)
    topview(rootNode)