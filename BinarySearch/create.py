import math
def binary_search(array,value):
    start = 0
    end = len(array) - 1
    middle =math.floor((start+end)/2)
    
    while value != array[middle] and start <= end:
        if value > array[middle]:
            start = middle +1
        else:
            end = middle - 1
        middle = math.floor((start+end)/2)
    if array[middle] == value:
        return middle
    else:
        return -1

newList = [1,2,4,5,6,7,8,9,12,14,16,17,20]

index = binary_search(newList,12)

print(index)