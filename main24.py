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
