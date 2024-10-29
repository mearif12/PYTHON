#5.Looping (for,while)
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
