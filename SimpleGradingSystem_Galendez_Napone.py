# HI GUYS, THIS IS PRESENTED BY JOBERT NAPONE, AND RONALD FRANCO GALENDEz

Name1 = str(input("Enter Full Name:"))
Name2 = str(input("Enter Id Number:"))
Name3 = str(input("Enter Course:"))
Name4 = str(input("Enter Section:"))

# These next 6 lines of codes demonstrates the calcultaions of the user's average grade
Name5 = eval(input("Enter 1st Quarter Grade:"))
Name6 = eval(input("Enter 2nd Quarter Grade:"))
Name7 = eval(input("Enter 3rd Quarter Grade:"))
Name8 = eval(input("Enter 4th Quarter Grade:"))


average = (Name5 + Name6 + Name7 + Name8) / 4


# Prints the Student's Information and Grade
print("-----------------------------------------")
print("Name:", Name1)
print("Id Number:", Name2)
print("Course:", Name3)
print("Section:", Name4)
print("1st Grade:", Name5)
print("2nd Grade:", Name6)
print("3rd Grade:", Name7)
print("4th Grade:", Name8)
print("The Average of", Name5, Name6, Name7, Name8, "is", average)
