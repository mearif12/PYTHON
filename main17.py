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
