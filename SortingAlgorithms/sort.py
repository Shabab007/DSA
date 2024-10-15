def buble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1]=array[j+1], array[j]
    print (array)

    
def selection_sort(list): 
        for i in range(len(list)):
             min_index = i
             for j in range(i+1, len(list)):
                  if list[min_index] > list[j]:
                       min_index=j
             list[i],list[min_index] = list[min_index], list[i] 
        print(list)

list = [1,2,4,5,6,7,8,9,12,12,14,16,17,20]
selection_sort(list)