# arr = [10,20,30,40,50,60,70,80,90,100]

# step 1:
# Low = 0
# High = 9
# mid = (0+9)//2 = 4
# mid = 50

# 60>50
# low = 5
# high = 9
# (5+9)//2=7


def binarySearch(arr,tar):
    low =0
    high = len(arr-1)

    while low<=high:
        mid = (low+high)//2
        if mid==tar:
            return mid
        elif tar>arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1


arr = [10,20,30,40,50,60,70,80,90,100]
target = 60
res = binarySearch(arr,target)

if res!=-1:
    print("Element found index:",res)
else:
    print("Element not found")
