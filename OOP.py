# Initializing Class (Blueprint of an object)
class Dog:
    # Initializing constructor
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    # Initializing Methods
    def bark(self):
        print(f"{self.name} said Hello!")

# Creating a new Object
# my_dog = Dog("Bob",4)
# Invoking a method
# my_dog.bark()

# Let's try another class
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self) :
        return 3.14 * (self.radius ** 2)
    
my_circle = Circle(2)
print(my_circle.area())

# Let's understand Inheritance
class Animal:
    def __init__(self,species):
        self.species = species
    def speak(self):
        print(f"Message from {self.species}")

# Inheriting Animal class into a new class
class Dog(Animal):
    def __init__(self, species):
        # Super function bascially calls the inherited code from the parent class
        super().__init__(species)

    def bark(self):
        print("Woof!")
class Cat(Animal):
    def meow(self):
        print("Meow!")       

# Calling classes
my_dog = Dog("Bob")
my_cat = Cat("Oggy")
my_dog.speak()
my_cat.speak()

my_dog.bark()
my_cat.meow()

# Method Overriding: Here the derived class can override the quality of the parent class
class Bird(Animal):
    # Overridding the self method
    def speak(self):
        print(f"I'm Overriding the parent class, {self.species}")

my_bird = Bird("SuperBird")
my_bird.speak()

# Calling super function (The logic part from the parent class)
class Fish(Animal):
    def speak(self):
        super().speak()
        print("Another piece of line with speak!!!")

my_fish = Fish("Allice")
my_fish.speak()


# Let's understand Encapsulation
# It is the method of protecting data or methods in a class
# self.var => public specifier
# self._var => protected specifier
# self.__var => private specifier

class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    def Deposite(self,amount):
        self._balance += amount
        print(f"Amount deposited: ${amount}, total bank balance: ${self._balance}")

    def Withdraw(self,amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            print(f"Amount withdrawn: ${amount}, total bank balance: ${self._balance}")
        else:
            print("Invalid amount to withdraw")
    
    def Balance(self):
        return self._balance

my_account = BankAccount(5000)
my_account.Deposite(500)
my_account.Withdraw(200)

# Accessing a protected variable
# Not recommended
print(my_account._balance)

# Recommended: Using Getter Method
print(my_account.Balance())


# Now it's time for polymorphism. Polymorphism is the multiple behaviour of a method according to condition
# It is of two types:
#   1) Compile-time polymorphism
#   2) Run-time polymorphism

# Compile-time polymorphism:
class Function:
    def __init__(self):
        pass
    def add(self,*args):
        return sum(args)

my_function = Function()
add_1 = my_function.add(1,2)
add_2 = my_function.add(1,2,3)
print(f"Results got by polymorphic effect for different number of inputs: {add_1},{add_2}") 