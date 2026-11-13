# [38,27,43,3,9,82,10]

# [38,27,43] [3,9,82,10]
# [38,27][43] [3,9][82,10]
# [38][27][43][3][9][82][10]
# [38][27] = [27,38,43]
# [3][9] = [3,9]
# [82][10] = [10,82]
# [3,9,10,82]
# [3,9,10,27,38,43,82]

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    print(left)
    return merge(left,right)
def merge(left,right):
    print(left)
    res = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            # 2<5
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
        
    res.extend(left[i:])
    res.extend(right[j:])
    return res
arr = [38,27,43,3,9,82,10]

res = mergeSort(arr)
print("Sorted array:",res)


arr.sort(reverse=True)
print(arr)

