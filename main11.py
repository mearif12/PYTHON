#Nested loops

   #A loop can have another loop nested within it. 
   #This means that for each iteration of the outer (main) loop, the inner loop will run entirely.
   #Each iteration of the outer loop runs the inner loop entirely, with corresponding iterator values.
   #(f"something:{some}") is knwon as formatted string,where {some} prints the value of variable some.
   #use "\n" to print new line

outer_loop = [1,2,3]
inner_loop = ["a","b","c"]

for outer in outer_loop:
    for inner in inner_loop: #loop continues(outer_loop * inner_loop) times
        print(f"Outer: {outer}, Inner: {inner}")#Ex: Outer: 1, Inner: a,b,c 


#printing types of items

vehicles = ["car","bike"]
colors = ["red","blue","black"]

for i in vehicles:
    print(i +": ")
    for j in colors:
        print(j) #car:red blue black ; bike:red blue black

    print("\n")#prints new line    

#nested in range(a,b).but counts from a to b-1
for i in range(1,3):
    for j in range(2,4):
        print(i,j) # 12 13 22 23    

#mixed nesting : by range() and list
items = ["A","B","C"]
for i in items:
    for j in range(3):
        print(i) # A A A B B B C C C
