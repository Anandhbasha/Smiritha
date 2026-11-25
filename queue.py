# # # from collections import deque
# # # queue = deque()

# # # queue.append(100)
# # # queue.append(200)
# # # queue.append(300)
# # # queue.append(400)
# # # queue.append(500)
# # # queue.append(600)

# # # print(queue)
# # # print(queue[0])
# # # # print(queue.pop(0))
# # # remove = queue.popleft()
# # # print(remove)
# # # print(queue)

# # class Node:
# #     def __init__(self,data):
# #         self.data = data
# #         self.next = None

# # class Queue:
# #     def __init__(self):
# #         self.front = None
# #         self.rear = None
# #     def enQueue(self,data):
# #         newNode = Node(data)
# #         if self.rear is None:
# #             self.front= self.rear = newNode
# #             return
# #         self.rear.next = newNode
# #         self.rear = newNode

# #     def dequeue(self):
# #         if self.front is None:
# #             print("Queue is emppty")
# #             return None
# #         value = self.front.data
# #         self.front.data = self.front.next
# #         if self.front is None:
# #             self.rear=None
# #         return value
# #     def peek(self):
# #         if self.front is Node:
# #             return None
# #         return self.front.data
# #     def display(self):
# #         curr = self.front
# #         while curr:
# #             print(curr.data,end="->")
# #             curr = curr.next
# #         print("None")


# # q = Queue()
# # q.enQueue(10)
# # q.enQueue(20)
# # q.enQueue(30)
# # q.enQueue(40)

# # q.display()

# # print(q.peek())
# # print(q.dequeue())


# # q.display()



# # Circular queue
# class CircularQueue:
#     def __init__(self,size):
#         self.size = size
#         # list size =5
#         self.front = -1
#         self.rear = -1
#         self.queue = [None]*size
#         # 5*[None,None,None,None,None]



#     def enqueue(self,value):
#         if (self.rear+1)%self.size==self.front:
#             print("Queue is full")
#             return
#         if self.front==-1:
#             self.front=0
#         self.rear =(self.rear+1)%self.size
        
#         self.queue[self.rear] = value

#         # self.queue[0] = 10
#     def dequeue(self):
#         if self.front ==-1:
#             print("Queue is empty")
#             return None
#         value = self.queue[self.front]
#         # [10,20,30,40,50]
#         self.queue[self.front] = None
#         # [None,20,30,40,50]
#         if self.front==self.rear:
#             # [10]
#             self.front=self.rear=-1
#         else:
#             self.front = (self.front+1)%self.size
#             # (0+1)%5->1
#             # (1+1)%5->2
#             # 4+1->0
#         return value
#     def display(self):
#         if self.front==-1:
#             print("Queue is empty")
#             return
#         x = self.front
#         while True:
#             print(self.queue[x],end="->")
#             if x==self.rear:
#                 break
#             x = (x+1)%self.size
#         print()

# cq = CircularQueue(5)
# cq.enqueue(10)
# cq.enqueue(20)
# cq.enqueue(30)
# cq.enqueue(40)
# cq.enqueue(50)

# cq.display()


# cq.dequeue()
# cq.dequeue()

# cq.display()

# cq.enqueue(70)
# cq.enqueue(80)
# cq.display()


# Priority
import heapq

patients = []

heapq.heappush(patients,(3,"Patient1"))
heapq.heappush(patients,(1,"Patient2"))
heapq.heappush(patients,(2,"Patient3"))

print(patients)

while patients:
    priority,name = heapq.heappop(patients)
    print(name,priority)
