#6.Password checker

password = "Arif12"
guess = input("Enter your password: ")
while guess != password:
    print("Not Correct")
    guess = input("Try again: ")
    print("Successfully logged in")#loop is continuing untill the password matched
