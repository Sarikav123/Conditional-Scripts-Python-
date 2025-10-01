#Exercise 6 Reverse a number using while loop

num = int(input('Enter a number which is min 2 digit :'))

rvrsd = 0

while num>0:
    digit = num % 10
    num = num//10
    rvrsd = (rvrsd * 10) + digit
print(f'The reversed number is {rvrsd}')
