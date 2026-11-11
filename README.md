
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
