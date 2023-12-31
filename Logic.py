print("Let's understand if-else, while, for loop")
check_number = int(input("Enter an integer: "))

# # Start of if-else statement
if (check_number > 5):
    print("Hello!")
elif (check_number == 5):
    print("I will not greet you!")
else:
    print("Bye")
# # End of if-else statement
    
# # Start Of While loop
while (check_number < 5):
    check_number += 1

print(check_number)
# # End of while loop

fruits = ["Apple","Bannana","Mango","Guava"]

# # Format: for {variable} in {iterable}
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)
    # Output: 0,1,2,3,4

# Printing arrays with values and positions
for index,fruit in enumerate(fruits):
    print(f"Index: {index+1}, Fruit: {fruit}")

# Break statement in for loop
for i in range(10):
    if i==5 :
        break;
    print(i)

#iterating through a dictionary (key,value pairs)
my_dictionary = {'a': 1,'b': 2,'c': 3}
for key,value in my_dictionary.items():
    print(f"{key}: {value}")

names = ["Alice","Bob","Jhon"]
ages = [25,30,35]
# Zipping two arrays together to show the combined result
for name,age in zip(names,ages):
    print(f"{name}: {age}")

# range(1,10,2) means the for loop will start from 1, go upto 10 and difference between each element will be 2
for i in range(1,10,2):
    print(i)

# Output: 4,3,2,1,0
for i in reversed(range(5)):
    print(i)