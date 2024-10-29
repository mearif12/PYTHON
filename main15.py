#Custom function

    #To use your own functions, you need to define them first. 
    #Once a function has been defined, you can call it as many times as you need.
    #Arguments are put inside the parentheses () following the function name.
    #The result of a function can be sent back with the return statement.
    #Python allows function arguments to have default values.
    #If the function is called without the argument, the argument gets its default value.

def greet(name): #creating function
    print("Hello There")
    print("This is",name)
    print(f"{name} roll 12")
greet("M E Arif")  #calling the function  

#paramaterized function returns value
def triangle(b,h):
    area = 0.5*b*h
    height = h
    return area,height
print(triangle(2,3))#3.0  3

def hello(name="Guest"):
    print("Hello",name)
hello() # Hello Guest
hello("Ashton") # Hello Ashton
