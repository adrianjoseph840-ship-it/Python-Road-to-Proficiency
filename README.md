
# Lesson 01: Introduction to Python

## Overview

This lesson introduces Python programming and demonstrates
how to create and execute a basic Python program.

## Learning Objectives

- Understand what Python is.
- Understand the purpose of Python.
- Learn how to create a Python file.
- Use the print() function.
- Write comments in Python.

## What is Python?

Python is a high-level, general-purpose programming
language known for its simple and readable syntax.

It is commonly used in:

- Web Development
- Automation
- Data Science
- Artificial Intelligence
- Machine Learning
- Software Development

## Python File Extension

Python source code files use the `.py` extension.

Example:

`main.py`

## Python print() Function

The print() function displays information in the terminal.

Example:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

## Python Comments

Comments are notes written inside the source code.
Python ignores comments during program execution.

Example:

```python
# This is a Python comment
print("Learning Python")
```

## Program Output

```text
Hello, World!
Name: Adrian Joseph Bayonon
University: NWSSU
Course: BS Computer Science
I am learning Python from scratch.
My goal is to become a skilled programmer.
I want to develop applications and software.
```

## Key Takeaways

- Python is a beginner-friendly programming language.
- Python programs use the `.py` extension.
- The print() function displays output.
- Comments begin with the `#` symbol.

## Status

Completed



# Lesson 02: Variables and Data Storage

## Overview

This lesson introduces variables in Python and explains
how they are used to store and manage information.

## Learning Objectives

- Understand Python variables.
- Learn how to declare and assign variables.
- Identify common Python data types.
- Understand variable reassignment.
- Display variable values using print().

## What are Variables?

Variables are named references used to store and access
data in a Python program.

Example:

```python
name = "Adrian"
age = 21
```

In this example:

- `name` stores a string.
- `age` stores an integer.

## Variable Naming Rules

1. Variable names can contain letters, numbers, and underscores.
2. Variable names cannot start with a number.
3. Variable names are case-sensitive.
4. Python keywords cannot be used as variable names.
5. Use descriptive names for readability.

## Common Python Data Types

| Data Type | Description | Example |
|---|---|---|
| str | Text | "Python" |
| int | Whole numbers | 21 |
| float | Decimal numbers | 95.5 |
| bool | True or False | True |

## Variable Assignment

Variables are assigned using the equals sign (`=`).

Example:

```python
age = 21
```

## Variable Reassignment

The value of a variable can be changed.

Example:

```python
age = 21
age = 22

print(age)
```

Output:

```text
22
```

## Program Output

The program displays personal information, academic
information, different data types, and updated values.

## Key Takeaways

- Variables store and reference data.
- Python supports different data types.
- Variables can be reassigned.
- Descriptive variable names improve readability.

## Status

Completed



# Lesson 03: Python Data Types, Type Conversion, and Type Checking

## Overview

This lesson explores the built-in data types available in
Python and demonstrates how to identify and convert data
between different types.

## Learning Objectives

- Understand Python's built-in data types.
- Identify strings, integers, floats, and booleans.
- Understand lists, tuples, sets, and dictionaries.
- Learn about the None data type.
- Use the type() function to identify data types.
- Perform basic type conversion.

## 1. String (str)

Strings represent text enclosed in quotation marks.

Example:

```python
name = "Adrian"
course = "BS Computer Science"
```

## 2. Integer (int)

Integers represent whole numbers without decimal points.

Example:

```python
age = 21
year_level = 3
```

## 3. Float (float)

Floats represent numbers containing decimal points.

Example:

```python
grade = 95.5
height = 1.70
```

## 4. Boolean (bool)

Boolean values represent logical states.

Python has two Boolean values:

- True
- False

Example:

```python
is_student = True
is_graduated = False
```

## 5. List

A list stores multiple values in an ordered collection.
Lists are mutable, meaning their contents can be changed.

Example:

```python
subjects = ["Programming", "Mathematics", "Science"]
```

## 6. Tuple

A tuple stores multiple values in an ordered collection.
Unlike lists, tuples are immutable.

Example:

```python
coordinates = (10, 20)
```

## 7. Set

A set stores unique elements and does not maintain
a guaranteed ordering.

Example:

```python
numbers = {1, 2, 3, 4, 4, 5}
```

Duplicate values are automatically removed.

## 8. Dictionary

A dictionary stores information using key-value pairs.

Example:

```python
student = {
    "name": "Adrian",
    "course": "BS Computer Science",
    "year": 3
}
```

## 9. None

None represents the absence of a value.

Example:

```python
middle_name = None
```

## 10. Type Checking

Python provides the type() function to identify
the data type of a value.

Example:

```python
age = 21
print(type(age))
```

Output:

```text
<class 'int'>
```

## 11. Type Conversion

Type conversion changes a value from one data type
to another.

Common conversion functions:

| Function | Purpose |
|---|---|
| int() | Converts to integer |
| float() | Converts to float |
| str() | Converts to string |
| bool() | Converts to boolean |
| list() | Converts to list |
| tuple() | Converts to tuple |
| set() | Converts to set |

Example:

```python
number = "100"

integer_number = int(number)
float_number = float(number)

print(integer_number)
print(float_number)
```

Output:

```text
100
100.0
```

## Key Takeaways

- Python supports several built-in data types.
- Strings store text.
- Integers and floats store numerical values.
- Booleans represent True or False.
- Lists, tuples, sets, and dictionaries store collections.
- The type() function identifies data types.
- Type conversion changes values between compatible types.

## Project Files

- main.py - Python implementation and demonstrations.

## Status

Completed


# Lesson 04: Python User Input and Output

## Overview

This lesson introduces user input and output in Python.
It demonstrates how programs receive information from
users and display processed results.

## Learning Objectives

- Understand the input() function.
- Understand the print() function.
- Receive information from users.
- Convert input values into numerical data types.
- Use formatted strings (f-strings).
- Build a simple interactive calculator.

## 1. Output Using print()

The print() function displays information in the terminal.

Example:

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

## 2. Receiving Input Using input()

The input() function allows users to enter information.

Example:

```python
name = input("Enter your name: ")
print("Hello,", name)
```

The program waits for the user to enter a value.

## 3. Understanding Input Data Types

The input() function returns a string by default,
even when the user enters a number.

Example:

```python
age = input("Enter your age: ")

print(type(age))
```

Output:

```text
<class 'str'>
```

## 4. Converting User Input

Python provides conversion functions for transforming
input values into other data types.

Example:

```python
age = int(input("Enter your age: "))
grade = float(input("Enter your grade: "))
```

Common conversion functions:

| Function | Description |
|---|---|
| int() | Converts to integer |
| float() | Converts to decimal number |
| str() | Converts to string |
| bool() | Converts to boolean |

## 5. Formatted Strings (F-Strings)

F-strings allow variables and expressions to be placed
directly inside strings.

Example:

```python
name = "Adrian"
age = 21

print(f"My name is {name}.")
print(f"I am {age} years old.")
```

Output:

```text
My name is Adrian.
I am 21 years old.
```

## 6. Basic Arithmetic with User Input

Python can process numerical input using arithmetic
operators.

Example:

```python
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

total = first_number + second_number

print(f"Total: {total}")
```

## 7. Simple Calculator

The lesson also demonstrates a basic calculator
that performs:

- Addition
- Subtraction
- Multiplication
- Division

The program checks whether the second number is zero
before performing division.

## Key Takeaways

- print() displays information.
- input() receives information from users.
- input() returns a string by default.
- int() and float() convert numerical input.
- F-strings format output using variables.
- Python can process user input through calculations.

## Project Files

- main.py - Interactive Python input and output program.

## Status

Completed


# Lesson 05: Python Operators and Expressions

## Overview

This lesson explores the different operators available
in Python. Operators are symbols or keywords used to
perform operations on variables and values.

## Learning Objectives

- Understand arithmetic operators.
- Use assignment operators.
- Perform comparisons using comparison operators.
- Understand logical operators.
- Learn operator precedence.
- Apply operators in practical programs.

## 1. Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Description | Example |
|---|---|---|
| + | Addition | 10 + 5 = 15 |
| - | Subtraction | 10 - 5 = 5 |
| * | Multiplication | 10 * 5 = 50 |
| / | Division | 10 / 5 = 2.0 |
| // | Floor Division | 10 // 3 = 3 |
| % | Modulus | 10 % 3 = 1 |
| ** | Exponentiation | 2 ** 3 = 8 |

## 2. Assignment Operators

Assignment operators assign or update variable values.

| Operator | Example | Equivalent |
|---|---|---|
| = | x = 10 | Assign 10 |
| += | x += 5 | x = x + 5 |
| -= | x -= 5 | x = x - 5 |
| *= | x *= 2 | x = x * 2 |
| /= | x /= 2 | x = x / 2 |
| //= | x //= 2 | x = x // 2 |
| %= | x %= 3 | x = x % 3 |
| **= | x **= 2 | x = x ** 2 |

## 3. Comparison Operators

Comparison operators compare two values and return
a Boolean result: True or False.

| Operator | Description |
|---|---|
| == | Equal to |
| != | Not equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal to |
| <= | Less than or equal to |

Example:

```python
age = 21

print(age >= 18)
```

Output:

```text
True
```

## 4. Logical Operators

Logical operators combine or reverse conditions.

| Operator | Description |
|---|---|
| and | True when both conditions are true |
| or | True when at least one condition is true |
| not | Reverses a Boolean result |

Example:

```python
age = 21
has_valid_id = True

print(age >= 18 and has_valid_id)
```

Output:

```text
True
```

## 5. Operator Precedence

Operator precedence determines the order in which
Python evaluates expressions.

Example:

```python
result = 10 + 5 * 2

print(result)
```

Output:

```text
20
```

Multiplication is evaluated before addition.

Parentheses can change the evaluation order.

```python
result = (10 + 5) * 2

print(result)
```

Output:

```text
30
```

## 6. Practical Applications

This lesson includes three practical demonstrations:

### Student Grade Calculation

Calculates the average of three examination grades
and checks whether the student passed.

### Even or Odd Checker

Uses the modulus operator to determine whether
a number is even or odd.

### Logical Condition Checking

Combines multiple conditions using logical operators.

## Key Takeaways

- Arithmetic operators perform calculations.
- Assignment operators update variable values.
- Comparison operators return Boolean results.
- Logical operators combine conditions.
- Operator precedence determines evaluation order.
- Operators are essential in programming logic.

## Project Files

- main.py - Demonstration of Python operators.

## Status

Completed
