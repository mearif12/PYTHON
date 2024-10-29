#OOP

   #In OOP, blueprints are referred to as classes, 
   #In OOP, and the instances are known as objects.
   #Attributes are the properties that define an object's individuality within a class.
   #To add attributes to a class, you must define the __init__ method.
   #__init__ method's first parameter is always self, which represents the instance of the class.
   #This method's first parameter is always self, which represents the instance of the class.
   #you can add custom behaviors to a class by defining functions within it.
   #These functions, known as methods, should include the 'self' parameter to interact with the class instance. 
   #behaviors can call by dot notation.
   #The main difference between functions and methods is that functions are independent and can be called on their own,
   #while methods are associated with a class and can be called only with its instance.
   #Inheritance allows the new class to 'inherit' properties from the existing class while adding or modifying specific features as needed.   
   #This is especially helpful in inheritance, where a child class needs to extend or modify the behavior of its parent class without completely overriding its methods. 
   #super() is especially helpful in inheritance, where a child class needs to extend or modify the behavior of its parent class without completely overriding its methods.
   #Method overriding is a demonstration of another key concept in OOP - polymorphism.
   #If you want to keep the behavior of the parent class and extend it, you can use super() to invoke the parent class method.   

class Model: #creating class

 def __init__(self,name,color):
    self.name = name #assigns value to attributes or properties
    self.color = color
 def start(self):
   print("Successful behavior")
                
my_model = Model("Flag","green")
my_model.start()#calling the function inside the class
print(my_model.name)#Flag


#2
class Car(Model): #inherit from Model class
  def engine(self):
    print("Engine is running")

my_car = Car("BMW","Red")
print(f"My car is {my_car.name} and color is {my_car.color}")
my_car.start()
my_car.engine()
