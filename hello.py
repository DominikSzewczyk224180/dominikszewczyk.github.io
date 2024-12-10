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
