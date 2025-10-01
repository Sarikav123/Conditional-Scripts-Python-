#Exercise 8 Write a program to print the inputted value as it is
# and break the loop if the value is 'done'.
# Example run of the program :hello there hello there :finished finished :done Done


while True:
    userinput = input('Enter the text: ')
    if userinput == 'done':
        break
    print(userinput)
