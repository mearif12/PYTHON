#Data Hiding

   #Data hiding is a key idea in making code with objects (like in games or apps) safer and cleaner.
   #sometimes it's crucial to 'protect' certain class attributes and methods from being accessed outside the class. This is called data hiding.
   #data hiding has two levels. The first involves prefixing an attribute with a single underscore _, 
   #signaling it's meant for internal use and should be viewed as 'protected'.
   #Use _ for variables that are intended to be "protected" and accessed within the class or subclasses, but you’re okay with direct access if needed.
   #Use __ for variables that are truly "private" and should not be accessed or modified outside of the class.
   #__ it limits its access outside the class through name mangling, enhancing data protection and encapsulation.
   #Accessing a private attribute with double underscores from outside the class causes an error, but it's accessible within class methods.
   #Python employs name mangling for private attributes, which means you can access them using a specific naming convention from outside the class if necessary.

class Person:
    def __init__(self, name, age, salary):
        self.name = name         # Public variable
        self._age = age          # Protected variable (by convention)
        self.__salary = salary   # Private variable (name mangling)

    def get_salary(self):
        return self.__salary     # Public method to access the private variable

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

# Example usage
person = Person("John", 30, 50000)

# Access public variable
print(person.name)               # Output: John

# Access protected variable (discouraged, but allowed)
print(person._age)               # Output: 30

# Access private variable (will fail)
# print(person.__salary)         # Raises AttributeError

# Access private variable through a method
print(person.get_salary())        # Output: 50000

# Access private variable using name mangling (not recommended)
print(person._Person__salary)     # Output: 50000
