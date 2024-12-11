print("Hello")

# codacy_error_example.py

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


# Using `exec` and `eval` (security issues)
dangerous_code = "print('Hello World')"
exec(dangerous_code)  # Codacy should flag this as dangerous


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

# codacy_error_demo.py

# Unused import
import os
import sys

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

# Using `exec` and `eval` (security issues)
dangerous_code = "print('Hello World')"
exec(dangerous_code)  # Codacy should flag this as dangerous
eval(dangerous_code)  # Codacy should flag this as dangerous too

# Function with no docstring and complexity
def calculate(a, b):  # Function redefined intentionally
    if a == b:
        return a * b
    return a + b


# Hardcoded credentials (example for security checks)
def connect_to_database():
    username = "admin"  # Hardcoded username
    password = "12345"  # Hardcoded password (insecure)
    return username, password

connect_to_database

# Unreachable code
def unreachable_code_example():
    return "This function returns immediately."
    print("This line will never be executed.")  # Unreachable code

unreachable_code_example

# Inconsistent indentation (style issue)
def inconsistent_indentation():
    x = 10
      y = 20  # Indentation error
    return x + y

inconsistent_indentation

# Using bare `except` (bad practice)
def risky_try_except():
    try:
        risky_operation()
    except:  # Bare except, Codacy should flag this
        print("An error occurred.")

risky_try_except

# Very long line exceeding 120 characters
long_line_example = "This is an intentionally long line that exceeds the character limit to trigger a line length error from Codacy."


error

# Syntax error
def syntax_error_function():
    print("Missing closing parenthesis"  # Syntax error: missing closing parenthesis
          
