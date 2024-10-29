#List Comprehensions

    #List comprehensions are useful shorthands for such operations.
    #They offer a shorter and more readable way to create lists with various settings using just a single line of code.
    #List comprehensions:> var_name = [expression for i in iteration]
    #expression = x/x*x/etc | iteration = range(10),list,tuple etc

#1
num = []

for i in range(1,10):
    num.append(i)
print(num)#1 2 3 4 5 6 7 8 9

#2-Using list comprehensions

nums = [x*2 for x in range(1,6)]
print(nums)#2 4 6 8 10

#3-list comprehensions with lists
city = ["NY","YK"]
lists = [x.lower() for x in city]
print(lists)#'ny' 'yk'

#4-Extra if...else condition
names = ["Anik","labib"]
group = [x for x in names if x[0] != "A"]
print(group)
