# from collections import deque
# queue = deque()

# queue.append(100)
# queue.append(200)
# queue.append(300)
# queue.append(400)
# queue.append(500)
# queue.append(600)

# print(queue)
# print(queue[0])
# # print(queue.pop(0))
# remove = queue.popleft()
# print(remove)
# print(queue)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enQueue(self,data):
        newNode = Node(data)
        if self.rear is None:
            self.front= self.rear = newNode
            return
        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        if self.front is None:
            print("Queue is emppty")
            return None
        value = self.front.data
        self.front.data = self.front.next
        if self.front is None:
            self.rear=None
        return value
    def peek(self):
        if self.front is Node:
            return None
        return self.front.data
    def display(self):
        curr = self.front
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")


q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)

q.display()

print(q.peek())
print(q.dequeue())


q.display()