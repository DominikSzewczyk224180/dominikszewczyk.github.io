# codacy_error_demo.py

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

# Using `exec` (security issue)
dangerous_code = "print('Hello World')"
exec(dangerous_code)  # Codacy should flag this as dangerous

# Redefining a function
def calculate(a, b):  # Function redefined intentionally
    return a * b

# Syntax error
def syntax_error_function():
    print("Missing closing parenthesis"  # Syntax error: missing closing parenthesis

# Hardcoded credentials (example for security checks)
def connect_to_database():
    username = "admin"  # Hardcoded username
    password = "12345"  # Hardcoded password (insecure)
    return username, password