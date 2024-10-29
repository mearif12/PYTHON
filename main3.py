#3. User input and type conversion
  # two type of conversion:implicit (int[+-*/]float = float) & explicit (str()).
  # 6/2 = 3.0 .python follows line indentation.
  # input() => by sefault contains string type.
  # type() => is used to check the variable type.
  # str()/int()/float() => used to convert type.

get_input = input()

print(get_input)#'anything you entered'.
print(type(get_input))#'type that you entered'.

num = int(input("Enter a number: ")) ; float_num = float(num) ; string_num = str(num)

print(num)#2
print(float_num)#2.0
print(string_num)#"2"
