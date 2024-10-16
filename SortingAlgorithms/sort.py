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

def merge(list, left, middle,right ):
     n1= middle-left+1
     n2= right-middle

     L=[0]*(n1)
     R=[0]*(n2)
     for i in range(0,n1):
          L[i]=list[left+i]
     for j  in range(0,n2):
          R[j]=list[middle+1+j]
     i =0 
     j = 0 
     k = left
     while i < n1 and j < n2:
         if L[i] <= R[j]:
              list[k]= L[i]
              i+=1
         else:
              list[k]=R[j]
              j+=1
         k+=1

     while i < n1:
      list[k] = L[i]
      i+=1
      k+=1

     while j < n1 and j < n2:
      list[k] = R[j]
      j+=1
      k+=1

def merge_sort(list,l,r):
     if l < r:
          m=(l+(r-1))//2 
          merge_sort(list, l,m)
          merge_sort(list, m+1,r)
          merge(list,l,m,r)
     return list

list = [1,2,4,6,3,1,8,9,12,12,14,16,11,20]
print(merge_sort(list,0,13)) 