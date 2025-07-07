# PYTHON DOCUMENTATION

## Table of Contents :

1. [Python](#python-documentation)


   [1.1 Output](#1output--data-types)

   [1.2 Operators](#2operators)

   [1.3 Type Conversion](#3type-conversion)

   [1.4 More on Operators](#4comparison-and-logical-operator)

   [1.5 Looping](#5looping)

   [1.6 Password Checker](#6password-checker)

   [1.7 Control Statement](#7ifelse-statement)

   [1.8 List](#8list)

   [1.9 List Methods](#9list-slicing-methods)

   [1.10 List Iteration](#10list-iteration)

   [1.11 Nested for](#11nested-for-loop)

   [1.12 Iteration and Selection](#12iterations--selections)

   [1.13 Break and Continue](#13break--continue)

   [1.14 Built in Functions](#14built-in-functions)

   [1.15 User defined Functions](#15user-defined-functions)

   [1.16 Functions with Lists](#16functions-with-lists)

   [1.17 Tuple](#17tuple)

   [1.18 Set](#18set)

   [1.19 Dictionaries](#19dictionaries)

   [1.20 List Comprehensions](#20list-comprehensions)

   [1.21 Exception Handling](#21exception-handling)

   [1.22 Functional Programming](#22functional-programming)

   [1.23 Lambda Expressions](#23lambda-expressions)

   [1.24 Map and Filter](#24map--filter)

   [1.25 *args and **kwargs](#25args--kwargs)

   [1.26 Decorators](#26decorators)

   [1.27 OOP ~ Inheritance](#27oop--inheritance)

   [1.28 OOP ~ Data-Hiding](#28oop--data-hiding)

   [1.29 OOP ~ Class and Static Methods](#29oop--class--static-methods)

   [1.30 File Handling](#30file-handling)

2. [PHP](#php-documentation)   


#### 1.Output & data types:

```
#1.Printing and concatenating different data-types 

name = "Arif " ; roll = 12 ; bool = True
  
  #for same type use "+",use "," for differnet

print("Hello " + name , roll , bool)#Hello Arif 12 True 

```

#### 2.Opeartors:

```
 #Updating and Performing simple (+,-,*,/)

 #The execution of code happens line by line.so after getting 1st error it terminates execution.

 #python is a case-sensitive language.use snake casing to declare variables:(my_name)

x = 5 ; 
x = 7 ; #update to 7 
y = 3 

print("Addition: ", x+y) #10
print("Subtraction: ", x-y) #4
print("Multiplication: ", x*y) #21
print("Division: ",x/y) #2.3333


```

#### 3.Type conversion:

```
  # User input and type conversion
  # two type of conversion:implicit (int[+-*/]float = float) & explicit (str()).
  # 6/2 = 3.0 .python follows line indentation.
  # input() => by sefault contains string type.
  # type() => is used to check the variable type.
  # str()/int()/float() => used to convert type.

get_input = input()

print(get_input)#'anything you entered'.
print(type(get_input))#'type that you entered'.

num = int(input("Enter a number: ")) ; float_num = float(num) ; string_num = str(num)

print(num)#2
print(float_num)#2.0
print(string_num)#"2"

```

#### 4.comparison and logical operator:

```
   #Comparison Operator (>,<,>=,<=) and Logical Operator (and,or)

   #comparison & logical operator has only Boolean output: True/False.
   #Iteration is about executing an instruction repeatedly. 
   #Iteration is commonly represented as a loop.

a = 5 ; b = 7

print(60 > 30)#True
print (True and False)#False
print(a > 10 or b > 3)#True


```

#### 5.looping

```
  #Looping (for,while)

  #Iteration is about executing an instruction repeatedly. 
  #Iteration is commonly represented as a loop.
  #The code that gets repeated in the for loop must be indented. 
  #Indentation is the spaces at the beginning of lines.
  #Python doesn't mind whether you use 1 spaces or any other number of spaces.
  #while loop has 3 part: initialize,condition,updating
  #Loops usually include counters. 
  #A counter is a variable that keeps track of the number of iterations.
  #more operators for comparing: (==,!=,>=,<=)

for i in range(10):
    print("Student",i)#Student 0........Student9 

start = 5
while start > 0:
    print(start) #print infinitly 5 by default
    start = start - 1 #5 4 3 2 1    
print("Goodbye") #Goodbye

```

#### 6.Password checker:

```
 #Password checker

password = "Arif12"
guess = input("Enter your password: ")
while guess != password:
    print("Not Correct")
    guess = input("Try again: ")
    print("Successfully logged in")#loop is continuing untill the password matched

```

#### 7.if...else statement:

```
#if...else statement

cgpa = float(input("Enter your CGPA: "))

if cgpa>=3.00 or cgpa == "B":
    if cgpa>=3.75:
        print("Superb")#nested if...else
    print("Good")        
elif cgpa<3.00 or cgpa>2.00:
    print("Try more")   
else:
    print("Bad")   

```

#### 8.List:

```
#Lists

  #Lists allow you to store a collection of multiple values in a single variable.
  #Add square brackets [ ] around the values to create a list.
  #Lists are ordered collections of items. 
  #You can access an item in a list using its position or index number.
  #index starts from:0 to n-1 [n is total number of items in list]
  #Lists are ordered collections of items. 
  #You can access an item in a list using its position or index number.

city = ["Dhaka","Delhi","London","New-York"]

Bangla = city[0] # copying an item from list to another variable.

city[1]="Islamabad" # updating the value of an item in list. 

print(city)#'Dhaka','Delhi','London',New-York
print(city[0])#Dhaka
print(Bangla)
print(city[1])#Islamabad
print(city[0] + city[1])#DhakaIslamabad

currency = "Taka" #indexing also allwoed in string but immutable [not updateable]

print(currency[0])#T

Base = [
  
  "Binary",2,
  "Decimal",10.0,
  "Octal",8
] # List can store different data types

print(Base)

```

#### 9.List slicing methods:

```
#list methods

  #Indexing allows you to access individual values from a sequence. 
  #slicing:extract, modify and replace a specific range of elements from sequences.
  #Slicing allows you to extract a portion of a list.
  #Starting and stopping indexes are separated by a colon ":"
  #The starting index is inclusive. The stopping index is exclusive.
  #omit the starting index means that you'll be slicing from the very first element.  
  #[:n] means slicing from "0" index to "n".
  #[n:] means slicing from "n" index to "last".
  #[:] means slicing from "0" index to "last".
  #Python supports "indexing from the end", called negative indexing.EX=>-4"BD"-3"PAK"-2"NZ"-1"AUS"
  #always use less negative index then : then upper negative index.EX=>[-4:-2]. 

Country = ["BD","PAK","NZ","AUS"] #for slicing applied:0"BD"1"PAK"2"NZ"3"AUS"4   

pak = Country[1]

print(Country[0:2])#'BD','PAK'
print(Country[2:4])#'NZ','AUS'
print(Country[1:-2])#'PAK'
print(pak[1:3])#AK
print(pak[:2])#PA
print(Country[:3]) #'BD','PAK','NZ' .omit the starting index. 

Country[:3] = ["Wales","USA","UK"]#Updating country using slicing
print(Country) #['Wales', 'USA', 'UK', 'AUS']

```

#### 10.List iteration:

```
#List Iteration

    #You can check if an item is in a particular list by using the in operator.
    #It returns True if the item occurs one or more times in the list, and False if it doesn’t.
    #The iterator variable i stands for each item in the list. As the loop goes on, it changes to the next item.
    #The shorthand operator += provides an easy way to increment a variable’s value.

sub = ["EEE","ICE","CSE","ME"]
mine = "ICE"

print("EEE" in sub)#True 
print("PME" in sub)#False
print("C" in mine)#True

team = ["A","B","C","D"]
for i in team:
    print("letter" + i)# A B C D

price = 80 ; price += 10 # price = price + 10 , (-=,*=,/=)   
print(price)#90

num = [10,20,30,40]
for i in num:
    i *= 2 #doubling by i = i * 2 
    print(i)#20 40 60 80 

```

#### 11.Nested for loop:

```
#Nested loops

   #A loop can have another loop nested within it. 
   #This means that for each iteration of the outer (main) loop, the inner loop will run entirely.
   #Each iteration of the outer loop runs the inner loop entirely, with corresponding iterator values.
   #(f"something:{some}") is knwon as formatted string,where {some} prints the value of variable some.
   #use "\n" to print new line

outer_loop = [1,2,3]
inner_loop = ["a","b","c"]

for outer in outer_loop:
    for inner in inner_loop: #loop continues(outer_loop * inner_loop) times
        print(f"Outer: {outer}, Inner: {inner}")#Ex: Outer: 1, Inner: a,b,c 


#printing types of items

vehicles = ["car","bike"]
colors = ["red","blue","black"]

for i in vehicles:
    print(i +": ")
    for j in colors:
        print(j) #car:red blue black ; bike:red blue black

    print("\n")#prints new line    

#nested in range(a,b).but counts from a to b-1
for i in range(1,3):
    for j in range(2,4):
        print(i,j) # 12 13 22 23    

#mixed nesting : by range() and list
items = ["A","B","C"]
for i in items:
    for j in range(3):
        print(i) # A A A B B B C C C

```

#### 12.Iterations & selections:

```
#Iterations and Selections

    #You can combine if statements with list iterations.

nums = [34,45,56,67,78,86,99]
for i in nums:
    if i >= 60:
        print(i) #67 78 86 99 


#Counting same items in list and string
items = ["TV","PC","TV","TAB","PHONE","TV","PC","PHONE"]
counter = 0

for i in items:
    if i == "TV":
        counter += 1
        print(counter)#1 2 3  
print("Number of TV's :" , counter)#3    


bio = "Hey,This is M E Arif"
count = 0
for i in bio:
    if i == "s":
       count += 1
print("s in the string: " , count)        


num = [1,2,3,4,5]
sum = 0
for i in num:
    sum += i 
print(f"The summation is: {sum}")

#Checking something in list
lists = ["apple","banana","Orange","Berry","Jack-fruit"]
for i in lists:
    if "e" in i:
        print(i) #apple Orange Jack-fruit 

```

#### 13.Break & continue:

```
#break and continue

   #The break statement is used to stop the loop when some condition is met.
   #The break statement, stops a loop when a condition is meet.
   #The continue statement allows you to skip the current iteration of a loop when a certain condition is true.

nums = [1,2,3,4,5,6,7,0]
for i in nums:
    if i == 5:
       break #also break 0
    print(i)#1 2 3 4  

while True:
    text = input("Enter a text: ")
    print(text)
    if text == "Stop":
        break #loop will break when user input "Stop".otherwise,it continues 
    
#continue
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)#'cat' 'giraffe' 'mouse' 

hour = 1
while hour <= 10:
  if hour == 5:
    hour += 1
    continue
  print("Making coffee:", hour)#Only skips the "Making coffee: 5"
  hour +=1

```

#### 14.Built in functions:

```
#Functions 
  
   #Functions are reusable blocks of code for specific tasks.
   #They help keep your code as short and easy to work with as possible, saving you from repeating code.
   #Every function has a name. The code within a function is only executed when the function is "called".
   #The functions upper() and lower() and capitalize() allow you to quickly change the case of a string to all in uppercase or lowercase, respectively.
   #upper() and lower() functions can only be used on strings. 
   #Functions that only work on certain objects (strings, lists, etc.) are called using dot (.)notation.
   #The find() function checks if a character (or a pattern of characters) is present in a string. The function returns the index (position) of the given value. 
   #find() will return -1 if the value can't be found in the string.
   #upper(),lower(),find(),append(),insert(index,"item"),pops(index) are dot notation.
   #len() is a built in function, stands for length .
   #The append() function adds a new item to the end of a list.The append() function is for lists. If you try to use append() on a string you’ll get an error. 
   #The pop() function removes an element from a list.
   
print(type(range(2)))#built in functions
print(range(3))#range(0,3)

text = "BANgladesh"
print(text.upper())#BANGLADESH
print(text.lower())#bangladesh

ai = "robot"
print(ai.find("o"))#gives the first "o" index number (1).
print(ai.find("o",2))#gives the second "o" index number (3).
print(ai.find("A"))#-1
print(len(ai))#5

lists = ["ML","AI","C","R"]
print(len(lists))#4
lists.append("Ruby")
print(lists)#'ML' 'AI' 'C' 'R' 'Ruby'
lists.insert(2,"PYTHON")
print(lists)#'ML' 'AI' 'PYTHON' 'C' 'R' 'Ruby'
lists.pop(3)
print(lists)#'ML' 'AI' 'PYTHON' 'R' 'Ruby'
print(lists[3])#'R'

```

#### 15.User defined functions:

```
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

```

#### 16.Functions with lists:

```
#Functions with lists

   #You can create a custom function that takes a list as an argument.
   #The in operator allows you to easily check if an item is in a particular list.
   #It returns True if the item occurs one or more times in the list, and False if it doesn’t.
   #The sum() function takes a list as an argument and adds up all the elements in a list.
   #The sum function can work only with lists with numerical values.
   #The max() function returns the maximum value in a list.
   #The sorted() function takes an iterable as input and returns a list with the items sorted.
   #The sorted() function can handle both numerical and textual values. For textual values, it sorts them alphabetically.
   #You can specify ascending or descending order using the reverse argument. When reverse = True, the values are sorted in descending order.
#1
lists = ["Py","Cpp","C","R"]

def show(something):
    print(something)
show(lists)# "Py" "Cpp" "C" "R"   

#2
sub = []
def fun(num="Your number is: "):
    inp = int(input("Enter a number: "))
    sub.append(inp)
    print(num , sub)    
fun()    

#3
def play(score):
    if score >= 70:
        return True
print(play(65))#None    

#4
courses = ["OOP","ML","AI","DEEP"]
course = "Python"
def display(courses,course):
    return course in courses
print(display(courses,course))#False

#5
nums = [1,4,3,2,5]
maximum = max(nums)
minimum = min(nums)
sort = sorted(nums)
descend = sorted(nums,reverse=True)
total = sum(nums)
print(maximum)#5
print(minimum)#4
print(sort)# 1 2 3 4 5
print(descend)# 5 4 3 2 1
print(total)#15

```

#### 17.Tuple:

```
#Tuple

   #Tuples, like lists, are ordered collections of items created with parentheses.
   #The items in tuples also have their indexes, starting from 0. 
   #You can access the items in tuples just like you do with lists.
   #difference between tuples and lists is Tuples are immutable.
   #You can use the count() function to calculate the number of occurrences of an item in a tuple.
   #While unpacking, the number of variables should match the number of items in the tuple.Otherwise,the program will result in an error.
   #The * operator in tuple unpacking is used to gather multiple elements from the tuple into a list.
   #[*] operattor holds lists from the tuple.

#1
points = (12,14,9,10,9)
print(points.count(9)) #2

#2
time = (2001,"Sept",11)
year,month,date = time
print(f"USA destroyed by: {date} : {month} : {year}")#USA destroyed by: 11:Sept:2001

#3
nums = (200,300,400,500)
init,*rest = nums
print(init) #200
print(rest) #[300,400,500]

```

#### 18.Set:

```
#Tuple

   #Tuples, like lists, are ordered collections of items created with parentheses.
   #The items in tuples also have their indexes, starting from 0. 
   #You can access the items in tuples just like you do with lists.
   #difference between tuples and lists is Tuples are immutable.
   #You can use the count() function to calculate the number of occurrences of an item in a tuple.
   #While unpacking, the number of variables should match the number of items in the tuple.Otherwise,the program will result in an error.
   #The * operator in tuple unpacking is used to gather multiple elements from the tuple into a list.
   #[*] operattor holds lists from the tuple.

#1
points = (12,14,9,10,9)
print(points.count(9)) #2

#2
time = (2001,"Sept",11)
year,month,date = time
print(f"USA destroyed by: {date} : {month} : {year}")#USA destroyed by: 11:Sept:2001

#3
nums = (200,300,400,500)
init,*rest = nums
print(init) #200
print(rest) #[300,400,500]

```

#### 19.Dictionaries:

```
#Dictionaries

   #Dictionaries are collection types used to store data in key:value pairs, which are considered as items.
   #Dictionaries are created using curly brackets { }.it's almost like json format.
   #Key:value pairs in a dictionary are separated by commas, and they can be written on new lines for a better readability.
   #Dictionaries can have duplicate values, but not duplicate keys.Values with duplicate keys will overwrite existing values.
   #To access values in dictionaries, you need to use the keys.
   #Another way to access values in a dictionary is through the get() function.
   #You can get all the values and keys of a dictionary using the values() and keys() functions, respectively.
   #The items() function returns all the key:value pairs in a dictionary.
   #The update() function updates the dictionary with the items from the given argument.The argument must be a dictionary with the item you want to update.
   #The pop() function removes the item with the specified key name.

#1
dict_name = {
    
    "key":"value",
    "name":"Arif",
    "roll":10,
    "list":["ML","AI"]
}
dict_name.update({"roll":12,"reg":1065459})#updating and adding value of keys 

print(dict_name)#{'key': 'value', 'name': 'Arif', 'roll': 12, 'list': ['ML', 'AI']}
print(dict_name["roll"])#12

#2
key = dict_name.keys()
value = dict_name.values()
item = dict_name.items()
print(item)#dict_items([('key', 'value'), ('name', 'Arif'), ('roll', 12), ('list', ['ML', 'AI'])])
print(f"{key} : {value}")#dict_keys(['key', 'name', 'roll', 'list']) : dict_values(['value', 'Arif', 12, ['ML', 'AI']])

#3
dict_name.pop("key")
print(dict_name)#deleting "key"
print("key" in dict_name)#False

#4
for i in dict_name.values():
    print(i)#Showing all values

```

#### 20.List comprehensions:

```
#List Comprehensions

    #List comprehensions are useful shorthands for such operations.
    #They offer a shorter and more readable way to create lists with various settings using just a single line of code.
    #List comprehensions:> var_name = [expression for i in iteration]
    #expression = x/x*x/etc | iteration = range(10),list,tuple etc

#1
num = []

for i in range(1,10):
    num.append(i)
print(num)#1 2 3 4 5 6 7 8 9

#2-Using list comprehensions

nums = [x*2 for x in range(1,6)]
print(nums)#2 4 6 8 10

#3-list comprehensions with lists
city = ["NY","YK"]
lists = [x.lower() for x in city]
print(lists)#'ny' 'yk'

#4-Extra if...else condition
names = ["Anik","labib"]
group = [x for x in names if x[0] != "A"]
print(group)

```

#### 21.Exception handling:

```
#Exception

   #Exceptions are specific errors that occur during a program's execution and interrupt its normal flow when first encountered.
   #To handle them and prevent program failure, you can use a try/except statement.
   #The try block holds code that might cause an exception.
   #If an exception occurs, execution of the try block stops, and the except block is executed, allowing the program to continue running.
   #type of error: NameError,TypeError,IndexError,SyntaxError.
   #You can have multiple except blocks to handle each possible exception specifically.
   #You can use the finally statement to perform an operation after the try/except block, no matter if an exception occurred or not.
   #The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.   
   #You can trigger your own exceptions based on specific conditions using the raise statement. 
   #This will immediately stop the program's execution and indicate an error has occurred.   

#1
nums = [2,4,6,'8',9]

try:
    total = sum(nums)
    print(total)

except IndexError:
    print("Index is not correct")#this won't happen

except TypeError:
    print("Invalid types occurs")#this will happen

finally:
    print("Code runs successfully")        

#2
letter = ['A','B','C','D','E']
try:
    omit = letter[2]
except IndexError:
    print("Index is not correct")
else:
    print(omit + " is the letter")#if try: block is successfully execute the else: works    


#3-raise
price = 995
if price > 900:
    raise ValueError("Value is error")

```

#### 22.Functional programming:

```
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

```

#### 23.Lambda expressions:

```
#Lambda Expressions

   #Lambda expressions are functions without a name that are quick to create and use.
   #They are written in just one line using the lambda keyword and are often used for small, simple tasks.
   #Lambda expressions are called anonymous functions.
   #You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function.    

greet = (lambda name:"Welcome :"+name) ("Arif")
print(greet)#Welcome Arif

tri = lambda height,width: "Area :" + str(0.5*height*width)
print(tri(2,2))#Area :2.0

```

#### 24.Map & filter:

```
#Map & Filter
 
   #The map() function applies a specified function to every element in an iterable, like lists or tuples.
   #It produces a result that can be transformed into a list using the list() function for easy viewing or further use.
   #The map function takes two arguments - an iterable and function.:>map(function,iterable)
   #map function. This eliminates the need to define a regular function explicitly of lambda.   
   #The filter() function, just like the map() function, takes in a function and an iterable as arguments. 
   #The key purpose of filter() is to apply a condition specified in the provided function to each item in the iterable
   #and return only those for which the function evaluates to True.
   #filter() is just give extra condition where map() apllies for all.   

names = ["kiAs","riFa","Shifa"]

def capital(name):
    return name.capitalize()

#1
capitalized = map(capital,names)#applying capital() to names list

capitalized = list(capitalized)#converting into list

print(capitalized)#'Kias' 'Rifa' 'Shifa'

#2
print(list(map(capital,names)))#Short form
print(list(filter(lambda name: len(name) == 4,names)))#'kiAs' 'riFa'

#3
nums = [1,2,3]
double = list(map(lambda x:x*2,nums))
print(double)#[2,4,6]


```

#### 25.*args & **kwargs:

```
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

```

#### 26.Decorators:

```
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

```

#### 27.OOP ~ inheritance

```
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


#3
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calls the speak method from Animal class
        print("Dog barks")

dog = Dog()
dog.speak()

```

#### 28.OOP ~ data hiding:

```
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

```

#### 29.OOP ~ class & static methods:

```
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


```

#### 30.File handling:

```
#File Handling

    #Python has several functions for creating, reading, updating, and deleting files.
    #The open() function takes two parameters; filename, and mode.
    #There are four different methods (modes) for opening a file:
    #"r","a","w","x"->read,append,write,Create - Creates the specified file, returns an error if the file exists.
    #In addition you can specify if the file should be handled as binary or text mode
    #"t" - Text - Default value. Text mode."b" - Binary - Binary mode (e.g. images)
    #read(x)->used to read part of the file.
    #"a" - Append - will append to the end of the file
    #"w" - Write - will overwrite any existing content
    #To delete a file, you must import the OS module, and run its os.remove() function.
    #To delete an entire folder, use the os.rmdir() method.
    #By calling readline() two times, you can read the two first lines.

file = open("demo.txt","wt") #write text
file.write("This is ME ARIF")
file.close()

file = open("demo.txt","r")
print(file.read(2)) #Th
print(file.read())

import os
os.remove(file.txt)
os.rmdir(folder)


#Check if file exists, then delete it:

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

```

## - - - - - - - - - - - - - - - - - - - - - - - - - - -THE END- - - - - - - - - - - - - - - - - - - - - - - - - - - - 
