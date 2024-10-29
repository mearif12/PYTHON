#Set

   #Sets, unlike lists and tuples, are unordered collections. 
   #Sets are created with curly brackets { }.
   #Sets are unordered and don't support indexing or slicing.
   #Sets can't have duplicates, which is very helpful 
   #when developers need to ensure that each item in a collection is unique.
   #Adding duplicate items to a set doesn't cause an error; instead, it's ignored.
   #Like lists and tuples, sets can have values with different data types.
   #Sets are mutuable,Use the add() and remove() functions, each with a value as an argument, to add or remove it from a set.
   #append() function works only with ordered collection types,Sets are unordered, that's why you can't use it on them.
   #The clear() function doesn't accept an argument and removes all the items from a set.
   #The union() function called returns a new set with all elements from both sets, omitting duplicates.
   #The difference() function returns a set containing elements that are only in the first set and not in the second.

#1
students = {"Rafi","kafi","Nafi"}
students.clear()#clearing the set
print(students)#set()
students.add("Shafi")
print(students)#{'Shafi'}

#2
book_1 = {"OOP","DM","DE","AC"}
book_2 = {"DC","NM","AE","ML"}

books = book_1.union(book_2)#Union of 2 sets
print(books)#{'AE', 'DM', 'DE', 'OOP', 'DC', 'ML', 'AC', 'NM'}

bookes = book_1.difference(book_2)#A-B of 2 sets
print(bookes)#{'DE','OOP','DM','AC'}
