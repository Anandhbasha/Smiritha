# 5,3,1,2,4
# 3,5,1,2,4
# 3,1,5,2,4
# 1,3,5,2,4
# 1,2,3,4,5

arr = [5,3,1,2,4]
for i in range(1,len(arr)):
    # 1,5
    key = arr[i]
    j = i-1
    # 3
    while j>=0 and arr[j]>key:
    # arr[j] = 5
    # key = 3
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key

print("Sorted array:",arr)

