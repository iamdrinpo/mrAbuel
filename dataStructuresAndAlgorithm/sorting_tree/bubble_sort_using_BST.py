# node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# insertion of values
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# placing of values (left or right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

values = list(map(int, input("Enter numbers to insert into the tree: ").split()))

root = None
for v in values:
    root = insert(root, v)

print("Sorted values from the tree: ", end="")
inorder(root)
