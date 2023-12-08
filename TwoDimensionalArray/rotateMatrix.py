import numpy as np

myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])
def rotateMatrix(matrix):
   for layer in range(len(matrix//2)):
        first= layer
        last= len(matrix) - 1 - layer
        for i in range(first,last):
            top = matrix[layer][i]
            matrix[layer][i]= matrix[-i-1][layer]
            matrix[-i-1][layer]=matrix[-layer-1][-i-1]
            matrix[-layer-1][-i-1]= matrix[i][-layer-1]
            matrix[i][-layer-1] = top
   return matrix     

print(rotateMatrix(myArray))
