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
