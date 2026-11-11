
# ==========================================
# Lesson 04: Python User Input and Output
# Author: Adrian Joseph Bayonon
# Description: Receiving and displaying
#              user information
# ==========================================

# 1. BASIC OUTPUT
print("WELCOME TO PYTHON PROGRAMMING!")
print("This program demonstrates user input and output.")

# 2. BASIC USER INPUT
print("\nPERSONAL INFORMATION")

name = input("Enter your full name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

print("\nPERSONAL DETAILS")
print("Name:", name)
print("Age:", age)
print("Course:", course)

# 3. CONVERTING USER INPUT
print("\nNUMERICAL INPUT")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

total = first_number + second_number

print("First Number:", first_number)
print("Second Number:", second_number)
print("Sum:", total)

# 4. FLOAT INPUT
print("\nGRADE INFORMATION")

grade = float(input("Enter your grade: "))

print("Your grade is:", grade)

# 5. FORMATTED STRINGS (F-STRINGS)
print("\nFORMATTED OUTPUT")

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"You are taking {course}.")
print(f"Your recorded grade is {grade}.")

# 6. SIMPLE CALCULATOR
print("\nSIMPLE CALCULATOR")

num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Division: Cannot divide by zero.")

# End of Lesson 04
