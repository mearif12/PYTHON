#List Iteration

    #You can check if an item is in a particular list by using the in operator.
    #It returns True if the item occurs one or more times in the list, and False if it doesn’t.
    #The iterator variable i stands for each item in the list. As the loop goes on, it changes to the next item.
    #The shorthand operator += provides an easy way to increment a variable’s value.

sub = ["EEE","ICE","CSE","ME"]
mine = "ICE"

print("EEE" in sub)#True 
print("PME" in sub)#False
print("C" in mine)#True

team = ["A","B","C","D"]
for i in team:
    print("letter" + i)# A B C D

price = 80 ; price += 10 # price = price + 10 , (-=,*=,/=)   
print(price)#90

num = [10,20,30,40]
for i in num:
    i *= 2 #doubling by i = i * 2 
    print(i)#20 40 60 80 
