# Exercise 1 Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user
# and prints output the corresponding month of the year.
# An example run of the program
# (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March

user_input = int(input("Enter an integer from 1 to 12"))

months = ['January','February','March','April','May','June','July','August','september','october','november','december']
if 1 <= user_input <=12:
    print("Month is ", months[user_input - 1])
else:
    print("Invalid input")


