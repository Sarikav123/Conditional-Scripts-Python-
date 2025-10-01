# Exercise 2 A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old,
# and for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user) Enter your age:
# 63 Your ticket costs £2.00


user_input = int(input('Please enter your age: '))
ticketrate = 6

if user_input < 16:
    print(f"Your ticket costs', £{ticketrate/2:.2f}")
elif user_input >= 60:
    print(f"Your ticket costs', £{ticketrate/3:.2f}")
else:
    print(f"Your ticket costs', £{ticketrate:.2f}")





