# Stack 
# array Operation
# push
# pop
# peek
# isEmpty
# size

# append->push
# lst[-1]->Peek
# pop-> remove last 

stacks = []

stacks.append(10)
stacks.append(20)
stacks.append(30)
stacks.append(40)
stacks.append(50)
stacks.append(60)
stacks.append(70)

print("Stack List:",stacks)

print("Peek Element",stacks[-1])



removedValue = stacks.pop()
print("PopsElement",removedValue)

print("After Pop",stacks)


print("size",len(stacks))
print("is Empty:",len(stacks)==0)