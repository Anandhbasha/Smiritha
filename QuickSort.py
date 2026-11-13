# arr = [150,120,180,130,160,140]

# pivot = 140
# 120,130,140
# 150,160,180

def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left = []
    right =[]

    for i in arr[:-1]:
        if i<=pivot:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left)+[pivot]+quickSort(right)


arr = [150,120,180,130,160,140]
res = quickSort(arr)
print("Sorted array :",res)