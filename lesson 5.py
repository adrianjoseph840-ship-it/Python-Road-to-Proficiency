
# ==========================================
# Lesson 05: Python Operators and Expressions
# Author: Adrian Joseph Bayonon
# Description: Understanding Python operators
# ==========================================

# 1. ARITHMETIC OPERATORS

print("ARITHMETIC OPERATORS")

a = 20
b = 6

print("First Number:", a)
print("Second Number:", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# 2. ASSIGNMENT OPERATORS

print("\nASSIGNMENT OPERATORS")

number = 10
print("Initial Value:", number)

number += 5
print("After += 5:", number)

number -= 3
print("After -= 3:", number)

number *= 2
print("After *= 2:", number)

number /= 4
print("After /= 4:", number)


# 3. COMPARISON OPERATORS

print("\nCOMPARISON OPERATORS")

x = 15
y = 10

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)


# 4. LOGICAL OPERATORS

print("\nLOGICAL OPERATORS")

age = 21
has_valid_id = True

print("AND:", age >= 18 and has_valid_id)
print("OR:", age >= 18 or has_valid_id)
print("NOT:", not has_valid_id)


# 5. OPERATOR PRECEDENCE

print("\nOPERATOR PRECEDENCE")

result1 = 10 + 5 * 2
result2 = (10 + 5) * 2
result3 = 20 / 5 + 3

print("10 + 5 * 2 =", result1)
print("(10 + 5) * 2 =", result2)
print("20 / 5 + 3 =", result3)


# 6. PRACTICAL PROGRAM: STUDENT GRADE CALCULATION

print("\nSTUDENT GRADE CALCULATION")

prelim = 90
midterm = 85
final = 95

average = (prelim + midterm + final) / 3

print("Preliminary Grade:", prelim)
print("Midterm Grade:", midterm)
print("Final Grade:", final)
print("Average Grade:", average)

print("Passed:", average >= 75)


# 7. PRACTICAL PROGRAM: EVEN OR ODD

print("\nEVEN OR ODD CHECKER")

number = 24

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")


# End of Lesson 05
