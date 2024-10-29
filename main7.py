#if...else statement

cgpa = float(input("Enter your CGPA: "))

if cgpa>=3.00 or cgpa == "B":
    if cgpa>=3.75:
        print("Superb")#nested if...else
    print("Good")        
elif cgpa<3.00 or cgpa>2.00:
    print("Try more")   
else:
    print("Bad")   
