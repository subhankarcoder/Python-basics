import numpy as np
# Reshaping Arrays(From 1D to 2D)
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = arr_1d.reshape((2,3)) 
print(arr_2d)

# Flattening Array from 2D to 1D
arr_1d_again = arr_2d.flatten()
print(arr_1d_again)

# Concatenating 2 Arrays
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])
arr_concat = np.concatenate([arr_1,arr_2])
print(arr_concat)

# Stacking two arrays
arr_vertical_stack = np.vstack([arr_1,arr_2])
print("Vertically stacked: \n",arr_vertical_stack) # Output: [[1 2 3 4]
                                                        #    [5 6 7 8]]

arr_horizontal_stack = np.hstack([arr_1,arr_2])
print("Horizontally stacked: \n",arr_horizontal_stack) # Output: [1 2 3 4 5 6 7 8]

# Array Splitting
split_arr = np.split(arr_1,4) # Splitted the array into 4 equal parts
print(split_arr)

# Appending and deleting elements
arr_3 = np.append(arr_1,[9,10,11])
print(arr_3)

arr_4 = np.delete(arr_1,[1,2,3]) # Here it is deleting the index, not the element
print(arr_4)

# Inserting element in a specific position
arr_5 = np.insert(arr_1,1,[5]) # Inserting the value '5' at index 1 of arr_1
print(arr_5)