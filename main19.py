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
