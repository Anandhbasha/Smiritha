#       50
#   empty   20
# empty     30

#       50->2
#    20    60->1
#   10 40 55  70->0

# height =-1 for empty tree
# balance factor 

# Bf = Height(left)-Height(Right)

# 1-1 = 0
# 0-0=0

#   50
#   30
#   20

# left balance = 2
# right balance = -2


#   50
#  e    60  
#  e    70

# -1-1 = -2


# +1,-1

# LL->Single rotate concept

# 1->2->3 ->
# 3 =0
# 2=-1
# 1=-2
#   2-
# 1   3
# RR
# 1 ->2
# 2->1
# 3->0
#   2



# LR
#   7
# 3
#   5

#   7
#   5
#   3

#   5
# 3    7



# RL

#   3
#      7
#   5


# 3
# 5
# 7

#   5
# 3   7


class Node:
    def __init__(self,data):
        self.data = data
        self.left =None
        self.right = None
        self.height = 1

def height(node):
    if node is None:
        return 0
    return node.height

def bfactor(node):
    if node is None:
        return 0
    return height(node.left)-height(node.right)

def rotateRight(y):
    x = y.left
    temp = x.right
    x.right = y
    y.left = temp

    y.height = 1+max(height(y.left)),height(y.right)
    # 30.height = 1+max(0,0) = 1
    x.height = 1+max(height(x.left)),height(x.right)

    return x

def rotateLeft(x):
    y = x.left
    temp = y.right
    y.right = x
    x.left = temp

    x.height = 1+max(height(x.left)),height(x.right)
    y.height = 1+max(height(y.left)),height(y.right)

    return y

def insert(root,value):
    if root is None:
        return Node(value)
    if value< root.data:
        root.left = insert(root.left,value)
    elif value> root.data:
        root.right = insert(root.right,value)
    else:
        return root
    root.height = 1+max(height(root.left),height(root.right))
    bf = bfactor(root)

    # LL
    if bf > 1 and value < root.left.data:
        return rotateRight(root)
    if bf < -1 and value < root.right.data:
        return rotateLeft(root)
    if bf > 1 and value < root.left.data:
        root.left = rotateLeft(root.left)
        return rotateRight(root)
    if bf <-1 and value < root.right.data:
        root.right = rotateLeft(root.right)
        return rotateLeft(root)
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
# 30->y
# 20->x
# 10

#   20
# 10   30->y
