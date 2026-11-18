class Node:
    def __init__(self,data):
        self.data = data
        self.prev=None
        self.next=None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insertEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head=newNode
            return
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next = newNode
        temp.prev = temp
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print("None")

dl = DoubleLinkedList()
dl.insertEnd(100)
dl.insertEnd(200)
dl.insertEnd(300)
dl.insertEnd(400)

dl.display()