import numpy as np
# Array indexing and slicing
# Array indexing means determining the position of elements in an array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("The indexed element is: ",arr_2d[1,2]) # 2nd row 3rd coloumn output: 6

# Slicing means cutting particular elements of an Array
arr_1d = np.array([1,2,3,4])
print("Sliced element from index 1 to 3 is",arr_1d[1:4])

# Boolean indexing
mask = arr_1d > 2
print("Elements in arr_1d which is greater than 2 is: ",arr_1d[mask])

print("Shape of arr_2d is: ",arr_2d.shape)
print("Number of dimension in arr_2d is: ",arr_2d.ndim)

# Slicing of 2D Array
sliced_row = arr_2d[1:4,:]
print(sliced_row)
sliced_coloumn = arr_2d[:,1:4]
print("Sliced coloumns are: ",sliced_coloumn)