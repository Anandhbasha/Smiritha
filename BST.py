#           50
#      30       70
#   20    40  60   80

# 50->30,20,40
# 50->70,60,80

class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None

def insert(root,value):
    if root is None:
        return Node(value)
    if value< root.data:
        root.left = insert(root.left,value)
    elif value> root.data:
        root.right = insert(root.right,value)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end="-")
    inorder(root.right)

root = None

values = [50,30,70,20,40,60,80]

for i in values:
    root = insert(root,i)

inorder(root)

#       50  
#    30     60
# 20  40  70    80