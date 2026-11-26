from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def search(root,target):
    if root is None:
        return False
    if root.data ==target:
        return True
    return search(root.left,target) or search(root.right,target)

def counts(root):
    if root is None:
        return 0
    return 1 + counts(root.left) or counts(root.right)


def deletionNode(root,target):
    if root is None:
        return None
    queue = deque([root])
    targetNode = None
    deepestNode = None
    deepestParent = None

    while queue:
        curr = queue.popleft()
        if curr.data ==target and targetNode is None:
            targetNode = curr
        if curr.left:
            deepestParent = curr
            deepestNode =curr.left
            queue.append(curr.left)
        if curr.right:
            deepestParent = curr
            deepestNode =curr.right
            queue.append(curr.right)
    if targetNode is None:
        print("Element Not found")
        return root
    if deepestNode is None:
        return None
    targetNode.data = deepestNode.data

    if deepestParent.left==deepestNode:
        deepestNode.left = None
    else:
        deepestParent.right =None
    return root

#           10
#   90              30
# 60    70      80    90  

# 

root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(50)
root.left.right =Node(60)


root.right.left = Node(80)

target = 90
if search(root,target):
    print("Match found")
else:
    print("No match found")

print(counts(root))

root = deletionNode(root,100)