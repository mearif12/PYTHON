#break and continue

   #The break statement is used to stop the loop when some condition is met.
   #The break statement, stops a loop when a condition is meet.
   #The continue statement allows you to skip the current iteration of a loop when a certain condition is true.

nums = [1,2,3,4,5,6,7,0]
for i in nums:
    if i == 5:
       break #also break 0
    print(i)#1 2 3 4  

while True:
    text = input("Enter a text: ")
    print(text)
    if text == "Stop":
        break #loop will break when user input "Stop".otherwise,it continues 
    
#continue
animals = ["cat", "giraffe", "lion", "leopard", "mouse"]
for animal in animals:
  if animal[0] == "l":
    continue
  print(animal)#'cat' 'giraffe' 'mouse' 

hour = 1
while hour <= 10:
  if hour == 5:
    hour += 1
    continue
  print("Making coffee:", hour)#Only skips the "Making coffee: 5"
  hour +=1     
