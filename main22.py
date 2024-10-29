#Functional Programming
        
       #Functions that take another function as an argument or return a function -  are called Higher-Order Functions.

#1
def welcome(name):
    return "Welcome " + name
greet = welcome
print(greet("Arif")) 

#2
def home(name):
    return "Welcome " + name
def show(name,fun):
    print(fun(name))
show("Arif",home) 
