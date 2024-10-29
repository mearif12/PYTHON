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
