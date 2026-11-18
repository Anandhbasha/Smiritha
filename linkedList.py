lst = [10,20,30,40,50]
# 10
# 

# 0-> Node->10->1->node


# Create a Node
class Node:
    def __init__(self,data):
        # to store the value
        self.data = data
        # it store next node reference
        self.next = None

class LinkedList:
    def __init__(self):
        # first node
        self.head = None
    def insertData(self,data):
        # Add new node at end
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next = newNode
    def display(self):
        # Travese all node
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insertData(60)
ll.insertData(70)
ll.insertData(80)

ll.display()