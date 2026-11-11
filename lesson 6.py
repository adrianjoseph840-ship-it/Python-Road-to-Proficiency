
# ==========================================
# Lesson 06: Python Conditional Statements
# Author: Adrian Joseph Bayonon
# Description: Understanding decision-making
#              using conditional statements
# ==========================================

# 1. BASIC IF STATEMENT

print("BASIC IF STATEMENT")

age = 21

if age >= 18:
    print("You are an adult.")


# 2. IF-ELSE STATEMENT

print("\nIF-ELSE STATEMENT")

number = 10

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")


# 3. IF-ELIF-ELSE STATEMENT

print("\nIF-ELIF-ELSE STATEMENT")

grade = 88

if grade >= 90:
    print("Grade Classification: Excellent")
elif grade >= 85:
    print("Grade Classification: Very Good")
elif grade >= 80:
    print("Grade Classification: Good")
elif grade >= 75:
    print("Grade Classification: Passed")
else:
    print("Grade Classification: Failed")


# 4. NESTED IF STATEMENTS

print("\nNESTED IF STATEMENTS")

age = 21
has_valid_id = True

if age >= 18:
    if has_valid_id:
        print("You are eligible for verification.")
    else:
        print("Please provide a valid ID.")
else:
    print("You are not eligible.")


# 5. MULTIPLE CONDITIONS

print("\nMULTIPLE CONDITIONS")

attendance = 90
exam_score = 85

if attendance >= 75 and exam_score >= 75:
    print("Student passed the requirements.")
else:
    print("Student did not meet the requirements.")


# 6. TERNARY OPERATOR

print("\nTERNARY OPERATOR")

temperature = 30

weather = "Hot" if temperature >= 30 else "Cold"

print("Weather Condition:", weather)


# 7. PRACTICAL PROGRAM: VOTING ELIGIBILITY

print("\nVOTING ELIGIBILITY CHECKER")

voter_age = 20

if voter_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# 8. PRACTICAL PROGRAM: POSITIVE, NEGATIVE, OR ZERO

print("\nNUMBER CLASSIFIER")

number = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# 9. PRACTICAL PROGRAM: LOGIN AUTHENTICATION

print("\nLOGIN AUTHENTICATION SIMULATION")

correct_username = "admin"
correct_password = "python123"

username = "admin"
password = "python123"

if username == correct_username and password == correct_password:
    print("Login successful. Welcome!")
else:
    print("Invalid username or password.")


# End of Lesson 06
