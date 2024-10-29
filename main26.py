#Decorators

   #In Python, functions can be nested.
   #Decorators modify a function's behavior without altering its original code.
   #You can apply a decorator to a function using the @ sign.   

#1
def outer():
    print("Hello from outer function")

    def inner():
        print("Hello from inner function")
    inner()
outer()        

#2
def external(fun): #decorator function
    def internal():
        print("External runs")
        fun()
        print("Internal runs")
    return internal    

@external   #decorator
def hello():
    print("Hello there")
hello()
