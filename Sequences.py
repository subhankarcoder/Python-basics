# List is a mutable sequence, means the data can be modified anytime
list_template = [1,2,3,4]
print(type(list_template))

# Tuple is an immutable sequence, means the data can not be modified
tuple = (1,2,3,4)
print(type(tuple))

# Set is a mutabloe sequence, but only allows unique elements
set = {1,2,3,4}
print(type(set))

# Frozen set is a type of set where elements are immutable, so it can be used for hashing
template_set = {1,2,3}
frozenset_temp = frozenset(template_set)
print(type(frozenset_temp))

# Hashing frozenset
frozenset_1 = frozenset({1, 2, 3, 4})
frozenset_2 = frozenset({5,6,7,8})
dictionary = {frozenset_1: 'Set 1', frozenset_2: 'Set 2'}
print(dictionary)

# Mapping and Filtering
my_list = [1,2,3,4]
squared_list = list(map(lambda x: x**2, my_list))
print(my_list,squared_list)

filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)

# Mapping and filtering together
new_list = [1,2,3,4,5,6]
result = [x**2 for x in new_list if x % 2 == 0]
print(result)