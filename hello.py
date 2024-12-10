print("Hello")

# codacy_error_example.py

import math  # Unused import

def some_function():
    a = 10  # Unused variable
    b = 20
    c = 30
    result = b + c
    print(result)

def another_function():
    long_variable_name_example_that_exceeds_line_limit = "This string is too long and will break the line length rule because it's over 80 characters long, and this is not acceptable."
    
    # Some code
    if True:
        print("This is a simple line.")
    return "Done"

def a_very_long_function_name_that_exceeds_the_maximum_length_of_function_names():
    x = 5
    y = 10
    z = 15
    print(x + y + z)

some_function()  # Function too long if it's more than a few lines
# Example Python file with deliberate Codacy errors

# Unused import
import os

# Function with no docstring and complexity
def calculate(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        if a == 0:
            return "Zero"
        else:
            return a + b

# Line too long (Codacy often flags lines >80 or 120 characters)
very_long_variable_name = "This line is intentionally made very long to exceed the line length limit and trigger an error."

# Using `exec` and `eval` (security issues)
dangerous_code = "print('Hello World')"
exec(dangerous_code)  # Codacy or Bandit should flag this as dangerous

# Unused variable
unused_var = 1234

# Using print statements (depending on Codacy rules, print can be flagged in production code)
print("Debugging is fun!")  # Could be flagged as a bad practice

# Example Python file with deliberate Codacy errors

# Unused import
import os

# Function with no docstring and complexity
def calculate(a, b):
    if a > b:
        return a - b
    elif a < b:
        return b - a
    else:
        if a == 0:
            return "Zero"
        else:
            return a + b

# Line too long (Codacy often flags lines >80 or 120 characters)
very_long_variable_name = "This line is intentionally made very long to exceed the line length limit and trigger an error."

# Using `exec` and `eval` (security issues)
dangerous_code = "print('Hello World')"
exec(dangerous_code)  # Codacy or Bandit should flag this as dangerous

# Unused variable
unused_var = 1234

# Using print statements (depending on Codacy rules, print can be flagged in production code)
print("Debugging is fun!")  # Could be flagged as a bad practice
