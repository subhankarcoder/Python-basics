import numpy as np
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])

arr_res = arr_1 + arr_2 # Adding to Arrays (Element wise operation)
print(arr_res)
# Note: For element wise operation both the arrays should be of same dimension and shape
# Same elementary operations can be don for substrsction, multiplication and division


#BROADCASTING
# Broadcasting is a powerful process to add two arrays of any shapes and dimension in numpy
# Deep diving into example
arr_3 = np.array([1,2,3,4])
arr_4 = np.array([5,6,7])
# Broadcasting the addition
result = arr_3[:,np.newaxis] + arr_4
print("Result after broadcasting: ")
print(result)

# Using Universal functions (ufuncs)
arr_5 = np.array([1,2,3,4])
sqrt_arr = np.sqrt(arr_5)
print(sqrt_arr)