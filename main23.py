#Lambda Expressions

   #Lambda expressions are functions without a name that are quick to create and use.
   #They are written in just one line using the lambda keyword and are often used for small, simple tasks.
   #Lambda expressions are called anonymous functions.
   #You can provide arguments to lambda expressions on-the-fly by adding them in parentheses immediately after the lambda function.    

greet = (lambda name:"Welcome :"+name) ("Arif")
print(greet)#Welcome Arif

tri = lambda height,width: "Area :" + str(0.5*height*width)
print(tri(2,2))#Area :2.0
