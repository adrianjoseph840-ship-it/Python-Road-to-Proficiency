
# ==========================================
# Lesson 03: Python Data Types
# Author: Adrian Joseph Bayonon
# Description: Data types, type checking,
#              and type conversion
# ==========================================

# 1. STRING (str)
name = "Adrian Joseph Bayonon"
course = "BS Computer Science"

print("STRING DATA TYPE")
print("Name:", name)
print("Course:", course)
print("Type of name:", type(name))

# 2. INTEGER (int)
age = 21
year_level = 3

print("\nINTEGER DATA TYPE")
print("Age:", age)
print("Year Level:", year_level)
print("Type of age:", type(age))

# 3. FLOAT (float)
grade = 95.5
height = 1.70

print("\nFLOAT DATA TYPE")
print("Grade:", grade)
print("Height:", height)
print("Type of grade:", type(grade))

# 4. BOOLEAN (bool)
is_student = True
is_graduated = False

print("\nBOOLEAN DATA TYPE")
print("Currently a student:", is_student)
print("Graduated:", is_graduated)
print("Type of is_student:", type(is_student))

# 5. LIST
subjects = ["Programming", "Mathematics", "Software Engineering"]

print("\nLIST DATA TYPE")
print("Subjects:", subjects)
print("Type of subjects:", type(subjects))

# 6. TUPLE
coordinates = (10, 20)

print("\nTUPLE DATA TYPE")
print("Coordinates:", coordinates)
print("Type of coordinates:", type(coordinates))

# 7. SET
unique_numbers = {1, 2, 3, 4, 4, 5}

print("\nSET DATA TYPE")
print("Unique Numbers:", unique_numbers)
print("Type of unique_numbers:", type(unique_numbers))

# 8. DICTIONARY
student = {
    "name": "Adrian",
    "course": "BS Computer Science",
    "year": 3
}

print("\nDICTIONARY DATA TYPE")
print("Student Information:", student)
print("Type of student:", type(student))

# 9. NONE TYPE
middle_name = None

print("\nNONE DATA TYPE")
print("Middle Name:", middle_name)
print("Type of middle_name:", type(middle_name))

# 10. TYPE CONVERSION
print("\nTYPE CONVERSION")

number = "100"

converted_integer = int(number)
converted_float = float(number)
converted_string = str(converted_integer)

print("Original Value:", number)
print("Converted to Integer:", converted_integer)
print("Converted to Float:", converted_float)
print("Converted to String:", converted_string)

print("Original Type:", type(number))
print("Integer Type:", type(converted_integer))
print("Float Type:", type(converted_float))
print("String Type:", type(converted_string))

# 11. BOOLEAN CONVERSION
print("\nBOOLEAN CONVERSION")

value1 = bool(1)
value2 = bool(0)

print("bool(1):", value1)
print("bool(0):", value2)

# End of Lesson 03
