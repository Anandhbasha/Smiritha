class Node:
    def __init__(self,data):
        self.data = data
        self.next=None

class CircularList:
    def __init__(self):
        self.head=None
    def insertData(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next=self.head
            return
        temp = self.head
        while temp.next !=self.head:
            temp = temp.next
        temp.next =newNode
        newNode.next = self.head
    def display(self):
        if self.head is None:
            return
        temp = self.head
        while True:
            print(temp.data,end="->")
            temp=temp.next

            if temp==self.head:
                break
        print("Back to Front")


ll = CircularList()
ll.insertData(60)
ll.insertData(70)
ll.insertData(80)

ll.display()