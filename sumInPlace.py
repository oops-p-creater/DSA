class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def convert(root):
    if(not root):
        return 0
    else:
        sumleft=convert(root.left)
        sumright=convert(root.right)
        old=root.data
        root.data=sumright+sumleft
    return root.data+old

def preorder(root):
 
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
convert(root)
preorder(root)