def greet_name(name):
    print(f"Hello {name}!")
greet_name("Subhankar")

# Default parameters of a function
def greet_default_name(name="USER"):
    """
        This is a docstring of a function 
        parameters: name taken from the user
        return statement: printing greetings
    """
    print(f"Hello {name}!")
greet_default_name(); # Prints greeting with default name (USER)
greet_default_name("Jhon")

def multiplication(a,b):
    return a*b
result = multiplication(3,4)
print(result)

# Lambda function (are used to simplify usage of short and simple functions)

add = lambda x,y : x+y
result = add (3,4)
print(f"Sumof the numbers are: {result}")