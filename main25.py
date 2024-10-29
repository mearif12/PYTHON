# *args & **kwargs

   #*args allows you to provide any number of arguments without the need to create a list before calling the function each time.
   #*args receives arguments as a tuple, which can be used inside the function.
   #* operator informs Python that the argument is an iterable and should be unpacked to receive its values as individual arguments.
   #When defining a function with both regular arguments and *args, the regular arguments must come before *args in the function definition.
   #The first line of the function definition, which includes the function name and its parameters, is called function signature.
   #Python also allows you to pass keyword arguments using **kwargs. 
   # **kwargs receives arguments in the form of a dictionary, consisting of key:value pairs.
   #The ** operator in Python is used to unpack dictionaries into arguments.
   #** enables a function to accept an arbitrary number of keyword arguments, converting these arguments into a dictionary of key:value pairs.
   #to write a function:> def func_name(name,*args,**kwargs) 

def sum(*args):
    total = 0
    for i in args:
        total += i
    return total
print(sum(1,2,3,4))#10
print(sum(1,2,3,4,5))#15
print(sum(1,2,3,4,5,6))#21   

#2
def show(name,*args): #tuple type
    print("Name: " + name)
    for i in args:
        print(i)
show("TV","PC")#Name : TV PC

#3
def greet(**kwargs):  #dictionary type
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25, city="New York")
