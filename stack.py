# # Stack 
# # array Operation
# # push
# # pop
# # peek
# # isEmpty
# # size

# # append->push
# # lst[-1]->Peek
# # pop-> remove last 

# stacks = []

# stacks.append(10)
# stacks.append(20)
# stacks.append(30)
# stacks.append(40)
# stacks.append(50)
# stacks.append(60)
# stacks.append(70)

# print("Stack List:",stacks)

# print("Peek Element",stacks[-1])



# removedValue = stacks.pop()
# print("PopsElement",removedValue)

# print("After Pop",stacks)


# print("size",len(stacks))
# print("is Empty:",len(stacks)==0)



# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None
#     def push(self,data):
#         newNode = Node(data)
#         newNode.next =self.top
#         self.top = newNode
#     def pop(self):
#         if self.top is None:
#             print("Stack is empty")
#             return None
#         value = self.top.data
#         self.top = self.top.next
#         return value
#     def peek(self):
#         if self.top is None:
#             print("Stack is empty")
#             return None
#         return self.top.data
#     def display(self):
#         curr = self.top
#         while curr:
#             print(curr.data,end="->")
#             curr = curr.next
#         print("None")



# S = Stack()
# S.push(10)
# S.push(20)
# S.push(30)
# S.display()

# print("Top:",S.peek())
# print("Remove:",S.pop())

# S.display()


# def RevString(text):
#     stack=[]
#     for s in text:
#         stack.append(s)
#     res = ""
#     while stack:
#         res+=stack.pop()

#     return res

# result = RevString("Python")
# print(result)



# 10
# rem->0
# co->5->2->
# 1010


# def decimalToBinary(num):
#     if num==0:
#         return "0"
#     stack = []
#     while num>0:
#         rem = num%2
#         # append
#         stack.append(rem)
#         # [0,1,0,1]
#         num = num//2
#     binary=""
#     while stack:
#         # 1010
#         binary+=str(stack.pop())
#         # 1010
#     return binary

# value = decimalToBinary(10)
# print(value)



infix = "A+B*C"

stack = []
postfix = ""
for ch in infix:
    if ch.isalpha():
        postfix+=ch
        # ABC
    else:
        stack.append(ch)
while stack:
    postfix+=stack.pop()

print(postfix)


# ABC*+


# BODMAS
# Bracket
# of
# Division
# Multiplication
# Addtion
# Subs