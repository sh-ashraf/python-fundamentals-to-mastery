"""
================================================================================
PYTHON FUNDAMENTALS - INPUT() FUNCTION
================================================================================
Learning Focus: Getting user input, type conversion, and dynamic vs hard-coded values
"""


# ============================================================================
# 1. BASIC INPUT USAGE
# ============================================================================
# input() displays a prompt and waits for the user to type something

# Example (commented out - uncomment to test):
# input("Enter the Name: ")
# Note: This reads input but doesn't save it anywhere!


# ============================================================================
# 2. STORING USER INPUT IN VARIABLES
# ============================================================================
# To use the input later, we must save it in a variable

name = input("Enter your Name: ")
# User types: Shehab
# name now contains: "Shehab"

# Two ways to display the result:
print("you are", name)
# Output: you are Shehab
# Method 1: Comma separation (auto adds space)

print("you are " + name)
# Output: you are Shehab
# Method 2: String concatenation


# ============================================================================
# 3. TYPE CONVERSION - STRING TO INTEGER
# ============================================================================
# IMPORTANT: input() always returns a STRING, even if the user types numbers
# To perform math operations, we must convert the string to int

age = int(input("Enter your age: "))
# User types: 20
# age now contains: 20 (as integer, not string)

print(age + 5)
# Output: 25
# Now we can do math operations!

# Without int(), this would fail:
# age = input("Enter your age: ")  # User types "20"
# print(age + 5)  # Error! Can't add string + number
# TypeError: can only concatenate str (not "int") to str


# ============================================================================
# 4. HARD-CODED VALUES vs DYNAMIC VALUES
# ============================================================================
"""
Understanding the difference:

┌────────────────┬───────────────────┬────────────────┐
│ Feature        │ Hard-coded Values │ Dynamic Values │
├────────────────┼───────────────────┼────────────────┤
│ Defined where? │ Inside the code   │ During runtime │
│ Flexibility    │ Low               │ High           │
│ User input     │ No                │ Yes            │
│ Example        │ x = 10            │ x = input()    │
└────────────────┴───────────────────┴────────────────┘
"""

# Practical example combining both:
name = input("Enter your Name: ")  # Dynamic - changes each time program runs
country = "Egypt"                  # Hard-coded - always the same value

print(name, "comes from", country)
# If user enters "Ali", Output: Ali comes from Egypt
# If user enters "Sara", Output: Sara comes from Egypt


# ============================================================================
# 5. MULTIPLE TYPE CONVERSIONS
# ============================================================================

# Converting to integer
age = int(input("Enter your age: "))
# User types: 25
# Result: 25 (integer)

# Converting to float (for decimal numbers)
height = float(input("Enter your height in meters: "))
# User types: 1.75
# Result: 1.75 (float)

# No conversion needed (stays as string)
name = input("Enter your name: ")
# User types: Ahmed
# Result: "Ahmed" (string)

print(f"{name} is {age} years old and {height}m tall")
# Output: Ahmed is 25 years old and 1.75m tall


# ============================================================================
# 6. SUMMARY - input() FUNCTION
# ============================================================================
"""
input() Function:
    • Reads user input during runtime
    • Always returns text (string) by default
    • Can be converted to other types using int(), float(), etc.
    • Allows programs to be interactive and flexible

SYNTAX:
    variable = input("prompt message")

TYPE CONVERSION:
    age = int(input("Enter age: "))      # Convert to integer
    price = float(input("Enter price: ")) # Convert to decimal
    name = input("Enter name: ")          # Keep as string

COMMON ERRORS:
    • Forgetting to convert when doing math
    • Trying to convert non-numeric input to int/float
    • Not storing input in a variable

HARD-CODED vs DYNAMIC VALUES:
    • Hard-coded: Fixed values written directly in code
      Example: pi = 3.14
    
    • Dynamic: Values provided by user during execution
      Example: name = input("Name: ")
"""


# ============================================================================
# 7. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use input() to collect values from users
✓ Why input() always returns a string (even for numbers)
✓ How to use int(input()) to convert strings to numbers for math operations
✓ How to use float(input()) for decimal numbers
✓ The critical difference between hard-coded and dynamic values
✓ Why storing input in variables is necessary
✓ Two different ways to combine strings with print() (comma vs +)
✓ Common errors when working with input() and how to avoid them
✓ How to use f-strings to combine different data types in output
"""