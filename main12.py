#Iterations and Selections

    #You can combine if statements with list iterations.

nums = [34,45,56,67,78,86,99]
for i in nums:
    if i >= 60:
        print(i) #67 78 86 99 


#Counting same items in list and string
items = ["TV","PC","TV","TAB","PHONE","TV","PC","PHONE"]
counter = 0

for i in items:
    if i == "TV":
        counter += 1
        print(counter)#1 2 3  
print("Number of TV's :" , counter)#3    


bio = "Hey,This is M E Arif"
count = 0
for i in bio:
    if i == "s":
       count += 1
print("s in the string: " , count)        


num = [1,2,3,4,5]
sum = 0
for i in num:
    sum += i 
print(f"The summation is: {sum}")

#Checking something in list
lists = ["apple","banana","Orange","Berry","Jack-fruit"]
for i in lists:
    if "e" in i:
        print(i) #apple Orange Jack-fruit 
