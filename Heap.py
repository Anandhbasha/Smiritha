#      5
#   3     4
# 1   2   3.5

#           100 
#        50     80
#      20  30  60

#           10 
#        20     15
#      40  30  25


arr = [100,50,80,20,30,60]

# root - >i-1//2
# left child-> (2*i)+1
# right child->(2*1)+2


#       100
#   50      80
# 20   30

i= 1
print("Parent",arr[(i-1)//2])
# arr[(1-1)//2]->0//2->0
print("Left",arr[(2*i)+1])
print("Right",arr[(2*i)+2])


# 50->30->10->60
# 40
# 60

# 60->50->10->30
# 40


lst = [40,10,30,50,20]
lstorder = [10,20,30,40,50]


#       40
#   10      30
# 50   20



#       50
#   40      30
# 10   20


def heaps(arr,n,i):
    largets = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largets]:
        largets = left
    if right < n and arr[right] > arr[largets]:
            largets = right
    if largets!=i:
         arr[i],arr[largets] = arr[largets],arr[i]
         heaps(arr,n,largets)


def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
         heaps(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heaps(arr,i,0)

lst = [40,10,30,50,20]

heapSort(arr)