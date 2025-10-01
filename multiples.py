#Exercise 7 Finding the multiples of a number using loop


num = int(input("Enter a number: "))

val = 1
n = 1

while n<=10:
    val = num * n
    print( f'{num} * {n} = {val}' )
    n = n + 1
