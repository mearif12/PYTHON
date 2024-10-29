#Class & Static Methods

    #classmethod is a special type of creating class,without handking object.
    #Methods of objects we've looked at so far are called by an instance of a class. However, there are other types methods that a class can have - class and static methods.
    #Class methods are called on the class itself, not on individual instances. This allows their use without needing to create a class instance. 
    #Class methods are highly useful for accessing or managing data and functionality that relate to the class itself, rather than to any specific instance.
    #Static methods are similar to class methods, except they don't receive any additional arguments;
    #Static methods are identical to normal functions that belong to a class.They are marked with the @staticmethod decorator.
    #Static methods don't accept the cls parameter, meaning they can't access or modify the class's state. 

class Book:

 @classmethod
 def books(cls,name,roll):
    print(f"your name is {name} and roll is {roll}")

 @staticmethod
 def hello(name):
   print(f"Hello {name}")

Book.books("Arif",12)

Book.hello("Arif")
