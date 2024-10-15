import math

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

def insertion_sort(list): 
        for i in range(1,len(list)):
             key = list[i]
             j= i-1
             while j>=0 and key < list[j]:
               list[j+1]= list[j] 
               j = j-1
             list[j+1] = key
        print(list)
        return list

def bucket_sort(list):
     numbersOfBucket = round(math.sqrt(len(list)))
     maxValue = max(list)
     arr= []
     for i in range(numbersOfBucket):
          arr.append([])
     
     for j in list:
          index_b = math.ceil(j*numbersOfBucket/maxValue)
          arr[index_b-1].append(j)
     for i in range(numbersOfBucket):
          arr[i]=insertion_sort(arr[i])
     
     k = 0
     for i in range(numbersOfBucket):
          for j in range(len(arr[i])):
               list[k]= arr[i][j]
               k+=1
     print(list)

list = [1,2,4,6,3,1,8,9,12,12,14,16,11,20]
bucket_sort(list)