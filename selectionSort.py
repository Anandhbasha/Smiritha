def selctionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1,n):
            # 1,5
            # 2<1
            if arr[j]<arr[minIndex]:
                # arr[2]
                # 64<25
                minIndex = j
                # 2
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
        # 64->2
        # 11->0
        # 11,25,64,12,22
        # 11,25,12,64,22
    return arr


nums = [64,25,11,12,22]

# 64
# 25

print("BeforeSelection:",nums)

showRes = selctionSort(nums)

print("After Selection",showRes)