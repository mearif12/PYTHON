#Functions with lists

   #You can create a custom function that takes a list as an argument.
   #The in operator allows you to easily check if an item is in a particular list.
   #It returns True if the item occurs one or more times in the list, and False if it doesn’t.
   #The sum() function takes a list as an argument and adds up all the elements in a list.
   #The sum function can work only with lists with numerical values.
   #The max() function returns the maximum value in a list.
   #The sorted() function takes an iterable as input and returns a list with the items sorted.
   #The sorted() function can handle both numerical and textual values. For textual values, it sorts them alphabetically.
   #You can specify ascending or descending order using the reverse argument. When reverse = True, the values are sorted in descending order.
#1
lists = ["Py","Cpp","C","R"]

def show(something):
    print(something)
show(lists)# "Py" "Cpp" "C" "R"   

#2
sub = []
def fun(num="Your number is: "):
    inp = int(input("Enter a number: "))
    sub.append(inp)
    print(num , sub)    
fun()    

#3
def play(score):
    if score >= 70:
        return True
print(play(65))#None    

#4
courses = ["OOP","ML","AI","DEEP"]
course = "Python"
def display(courses,course):
    return course in courses
print(display(courses,course))#False

#5
nums = [1,4,3,2,5]
maximum = max(nums)
minimum = min(nums)
sort = sorted(nums)
descend = sorted(nums,reverse=True)
total = sum(nums)
print(maximum)#5
print(minimum)#4
print(sort)# 1 2 3 4 5
print(descend)# 5 4 3 2 1
print(total)#15
