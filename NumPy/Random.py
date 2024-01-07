import numpy as np
# Creating Random Numbers
rand_num = np.random.rand(5) # Creates 5 random numbers between 0 and 1
print(rand_num)

rand_num_n = np.random.randn(5) # This is using Gaussian Distribution (Bell curve) 
print(rand_num_n)

# Generating Integer between a range
rand_int = np.random.randint(1,10,5) # => [1,10) 5 random integers
print(rand_int)

# Sampling from an Array
arr = np.array([1,2,3,4,5,6])
np.random.shuffle(arr)
print(arr) # Shuffled the array

# Choice of sample
choiced_arr = np.random.choice(arr,size=3,replace=False)
print(choiced_arr)