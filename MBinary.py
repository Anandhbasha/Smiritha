class Node:
    def __init__(self):
        self.keys = []
        self.children = []

class MwayTree:
    def __init__(self,m):
        self.m = m
        self.root = None
    def insert(self,value):
        if self.root is None:
            self.root = Node()
            self.root.keys.append(value)
            return
        curr = self.root

        while True:
            if value in curr.keys:
                return
            if len(curr.keys) < self.m -1:
                curr.keys.append(value)
                curr.keys.sort()
                return
            index = 0
            while index <len(curr.keys) and value > curr.keys[index]:
                # 2 
                index+=1
            while len(curr.children) <= index:
                curr.children.append(Node())
            curr = curr.children[index]
    def search(self,value):
        curr = self.root
        while curr is not Node:
            if value in curr.keys:
                return True
            index = 0
            while index <len(curr.keys) and value > curr.keys[index]:
                index+=1
            if index >= len(curr.children):
                return False
            curr = curr.children[index]
        return False

tr = MwayTree(3)
values = [40,20,60,10,30,50,70]
for i in values:
    tr.insert(i)

print("Tree",tr.search(50))
print("Tree",tr.search(100))
            
# 

#   if len(curr.keys) < self.m -1:
# M=4
# Mx= 3

#       20      40          60
#    10   30  35   80     55    70


# 10,20,30,35,40,80,55,60,70

# 10 is called as root


# 2 < 3-1 = False