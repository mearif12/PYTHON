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
