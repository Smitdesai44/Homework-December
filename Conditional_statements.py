# Simple Conditional Questions

# 1)Check a number
#  Write a program to check if a number is positive, negative, or zero

# n = 4
# if n > 0:
#     print("Number is Positive")
# elif n < 0:
#     print("Number is Negative")
# else:
#     print("Zero")

# 2)Check even or odd
#  Write a program to check if a given number is even or odd.
# n = 5
# if n % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# 3)Grade Checker
#  Write a program to display grades based on a percentage:
# A: 90-100
# B: 70-89
# C: 50-69
# F: Below 50

# percentage = 49
# if 90 <= percentage <= 100:
#     print("Grade 'A'")
# elif 70 <= percentage <= 89:
#     print("Grade 'B'")
# elif 50 <= percentage <= 69:
#     print("Grade 'C'")
# else:
#     print("F")

# 4) Check divisibility
#  Check if a given number is divisible by 3, 5, or both.
# n = 15
# if n % 3 == 0 and n % 5 == 0:
#     print("The number is divisible by both")
# elif n % 3 == 0:
#     print("Number is divisible by 3")
# elif n % 5 == 0:
#     print("Number is divisible by 5")
# else:
#     print("Not Divisible")

# 5) Minimum of two numbers
#  Find the smaller number between two given numbers
# a = 4
# b = 5
# if a > b:
#     print("b is smaller")
# else:
#     print("a is smaller")





# Nested Conditional Questions

# 6) Find the largest of three numbers
#  Given three numbers, find the largest using nested if statements.
# n1 = 8
# n2 = 6
# n3 = 4
# if n1 > n2:
#     if n1 > n3:
#         print("Largest is N1")
#     else:
#         print("Largest is N3")
# else:
#     if n2 > n3:
#         print("Largest is N2")
#     else:
#         print("Largest is N3")
 
# 7)Check leap year
#  Write a program to check if a given year is a leap year or not:

# Divisible by 4 and not 100, or divisible by 400
# is_leap_year = True
# leap_year = 2023

# if is_leap_year:
#     if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
#         print("Leap Year")
#     else:
#         print("Not a leap year")

# 8)Nested temperature check
#  Categorize temperature into:

# Cold: Below 15°C
# Warm: 15°C to 30°C
# Hot: Above 30°C
# 
# is_temperature = True
# temperature = 31

# if is_temperature:
#     if temperature < 15:
#         print("Cold")
#     elif temperature >= 15 and temperature <= 30:
#         print('Warm')
#     else:
#         print("Hot")

# 9)Vowel or consonant
#  Check if a given character is a vowel or consonant.
# is_vowel = True
# vowel = "e"

# if is_vowel:
#     if vowel in "AEIOUaeiou":
#         print("Character is Vowel")
#     else:
#         print("Character is constant")

# 10) Driving eligibility
#  Check if a person is eligible to drive:

# Must be 18 or older.
# Nested check for possessing a valid license.
# is_eligible = True
# age = 33

# if age >= 18:
#     if is_eligible:
#         print("Has valid license and can drive!")
#     else:
#         print("Does not have valid license and cannot drive!")





# Advanced Logical Questions

# 11) Triangle validation
#  Check if three sides can form a triangle:

# The sum of any two sides must be greater than the third side.
# a = 5
# b = 5
# c = 10
# if a+b > c and b+c > a and c+a > b:
#     print("The sum of two sides are greater than third side")
# else:
#     print("The sum of two sides are not greater than third side")

# 12)Calculate tax based on salary
#  Determine the tax rate:

# Salary ≤ 5,00,000: 5%
# 5,00,001 - 10,00,000: 10%
# Above 10,00,000: 20%

# salary = 500000
# if salary <= 500000:
#     tax_rate = 0.05
# elif salary >= 500001 and salary <= 1000000:
#     tax_rate = 0.10
# else:
#     tax_rate = 0.20

# tax = salary * tax_rate
# print(tax)


# 13) Categorize age
#  Categorize a person's age:

# 0-12: Child
# 13-19: Teen
# 20-59: Adult
# 60+: Senior

# age = 70
# if 0 <= age <= 12:
#     print("Child")
# elif 13 <= age <= 19:
#     print("Teen")
# elif 20 <= age <= 59:
#     print("Adult")
# else:
#     print("Senior")

# 14)Logical AND check
#  Check if a number is greater than 10 and divisible by 2.
# num = 12
# if num > 10 and num % 2 == 0:
#     print("Number is greater than 10 and is divisible by 2")
# else:
#     print("Number is not greater than 10 and is not divisible by 2")

# 15)Logical OR check
#  Check if a number is less than 5 or greater than 20.
# num = 4
# if num < 5 or num > 20:
#     print("Number is less than 5 or greater than 20")
# else:
#     print("Number is not less than 5 or not greater than 20")





# Application-Based Scenarios

# 16)Electricity bill
#  Calculate an electricity bill:

# Usage ≤ 100 units: ₹5/unit
# 101-200 units: ₹10/unit
# Above 200 units: ₹15/unit

# usage_units = 250
# if usage_units <= 100:
#     bill_units = 5
# elif usage_units >= 101 and usage_units <= 200:
#     bill_units = 10
# else:
#     bill_units = 15

# bill = usage_units * bill_units
# print(bill)

# 17)Season finder
#  Find the season based on the month:

# December-February: Winter
# March-May: Spring
# June-August: Summer
# September-November: Autumn

# month = "April"
# if month == "December" or month == "January" or month == "February":
#     print("Winter")
# elif month == "March" or month == "April" or month == "May":
#     print("Spring")
# elif month == "June" or month == "July" or month == "August":
#     print("Summer")
# elif month == "September" or month == "October" or month == "November":
#     print("Autumn")
# else:
#     print("Enter valid season")

# 18)Password validation
#  Check if a password meets these conditions:

# At least 8 characters.
# Contains the character '@'.

# password = "smit@"
# if len(password) > 8:
#     print("Your password has 8 or more than 8 characters")
# elif "@" in password:
#     print("Your password contains @")
# else:
#     print("Sorry! your password does not satisfies this conditions")


# 19) Categorize BMI
#  Categorize Body Mass Index (BMI):

# Below 18.5: Underweight
# 18.5 - 24.9: Normal
# 25 - 29.9: Overweight
# 30 or higher: Obese

# BMI = 32
# if BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI <= 24.:9
#     print("Normal") 
# elif 25 <= BMI <= 29.9:
#     print("Overweight")
# else:
#     print("Obese")