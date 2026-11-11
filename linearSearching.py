def linSerach(array,finds):
    for i in range(len(array)):
        if array[i]==finds:
            # 10==45
            return i
    return 2

lst = [10,25,30,45,50,60]

target = int(input("Enter the number to find this input:"))

res = linSerach(lst,target)

if res==2:
    print("Element not found")
else:
    print("Element found at index:",res)


# o(1)
# O(n)

# small collections
# unsorted list
# simple


# 3,3