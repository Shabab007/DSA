import numpy as np

twoDimArray= np.array([[1,2,3],[2,5,6], [8,9,6]])

def searchTDArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] ==value:
                return (f"value is located in row {i} and column {j}")
    return "the element not found"

print(searchTDArray(twoDimArray,8))