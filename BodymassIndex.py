    # Exercise 3 Name your file: BodyMassIndex.py Write a program to calculate your BMI and
    # give weight status. Body Mass Index (BMI) is an internationally used measurement to check
    # if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms
    # and height in meters: BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI
    # range - kg/m2 Category Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese
    # An example run of the program (numbers in bold are typed in by the user) Enter your weight in (kg):
    # 75 Enter your height in (m): 1.70 Your BMI is: 25.95 You are in the “overweight” range.

weight = float(input("Enter weight in Kg: "))
height_cm = float(input("Enter height in cm: "))
height_m = height_cm/100
BMI = weight / (height_m ** 2)

if BMI < 18.5:
    print(f"Your BMI is: {BMI:.2f} You are in the “Underweight” range")
elif  18.5 <=BMI<= 24.9:
    print(f"Your BMI is: {BMI:.2f} You are in the “Normal” range")
elif   25 <=BMI< 30:
    print(f"Your BMI is: {BMI:.2f} You are in the “Overweight” range")
else:
    print(f"Your BMI is: {BMI:.2f} You are in the “Obese” range")
