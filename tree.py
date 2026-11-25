# Node ->An element in th tree
# root ->Top most in the tree
# parent ->Node has the child
# children ->connect below the parenty
# siblings->Node has a same parent
# leaf -> Node without child
# height ->Longest path leaf to root
# subtree -> a node form a node and its descendant
# Edge ->connect b/w two nodes
# ancestor->Node above another node
# descendant ->Node below the another node
# depth - >no of edges from root to node



# Binary Tree
# Binary tree travesal
# DFS Travesal method
    # InOrder
    # preorder
    # postorder


    #       10
    # 20          #30
#50      60     70    80
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inoreder(root):
    if root is None:
        return
    inoreder(root.left)
    print(root.data,end=" ")
    inoreder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
    

root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(50)
root.left.right =Node(60)


root.right.left = Node(80)
root.right.right =Node(90)

print("InOrder Travesel")
inoreder(root)

print("\nPreOrder Travesel")
preorder(root)

print("\nPostOrder Travesel")
postorder(root)

# Inorder
# Left root right
# preOreder
# Root Left Right
# post
# Left Right Root
