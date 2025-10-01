# Exercise 4 Write a Python program to receive 3
# numbers from the user and print the greatest among them.

a, b, c  = map(int,input("Please enter 3 numbers: ").split())
print(a,b,c)

if a>b:
    if a>c:
        print(f"The largest number is  n
        print(f"The largest number is {c}")
elif b>c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")


#another way
a,b,c = map(int, input("Please enter 3 numbers: ").split())
print(f"The largest number is {max(a,b,c)}")
