import numpy as np

arr_1d = np.array([1,2,3,4])
print(arr_1d)

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 3x3 Matrix (every array is a row)
print(arr_2d)

arr_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3d)

# Creating Arrays with Function
zeros_arry = np.zeros((3,3)) # Creating Null matrix
print(zeros_arry)

ones_array = np.ones((3,3)) # Creating array with every elements being 1
print(ones_array)

identity_array = np.eye(3) # Creating Identity matrix
print(identity_array)

range_arr = np.arange(0,10,2) # Creating an Array from 0 to 10 [0,10) with an interval of 2
print(range_arr)

linespace_arr = np.linspace(0,1,5) # Evenly distributed 5 elements from 0 to 1 [0.0,0.25,0.50,0.75,1.0]
print(linespace_arr)