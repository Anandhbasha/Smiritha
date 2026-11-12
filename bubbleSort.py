# # 30,40,50,10,20,15
# # a=30
# # b=40
# # 30,40
# # 40 & 50
# # 30,40,10,50,20,15
# # 30,40,10,20,50,15
# # 30,40,10,15,20,50
# # 30,10,40,15,20,50
# # 30,10,15,40,20,50
# # 30,10,15,20,40,50
# # 10,30,15,20,40,50
# # 10,15,20,30,40,50


# def bubbleSort(arr):
#     n= len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return arr

# # work upto last index
# # 5
# # 5->0
# # 4


# arr = [5,3,8,2,1]
# print("Before Bubble short:",arr)
# res = bubbleSort(arr)
# print("After Bubble short:",res)
        


def bubbleSort(arr):
    n= len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            if not swapped:
                break
    return arr

arr = [1,2,3,4,5]
print("Before Bubble short:",arr)
res = bubbleSort(arr)
print("After Bubble short:",res)

# Best case O(n)
# Worst case O(n^2)
# Space complexity O(1)