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
