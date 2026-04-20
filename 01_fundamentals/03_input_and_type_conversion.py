"""
================================================================================
PYTHON INPUT() FUNCTION - STUDY NOTES
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

# Two ways to display the result:
print("you are", name)          # Method 1: Comma separation (auto adds space)
print("you are " + name)         # Method 2: String concatenation


# ============================================================================
# 3. TYPE CONVERSION - STRING TO INTEGER
# ============================================================================
# IMPORTANT: input() always returns a STRING, even if the user types numbers
# To perform math operations, we must convert the string to int

age = int(input("Enter your age: "))
print(age + 5)  # Now we can do math operations!

# Without int(), this would fail:
# age = input("Enter your age: ")  # User types "20"
# print(age + 5)  # Error! Can't add string + number


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


# ============================================================================
# 5. SUMMARY - input() FUNCTION
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

HARD-CODED vs DYNAMIC VALUES:
    • Hard-coded: Fixed values written directly in code
      Example: pi = 3.14
    
    • Dynamic: Values provided by user during execution
      Example: name = input("Name: ")
"""


# ============================================================================
# 6. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use input() to collect values from users
✓ Why input() always returns a string (even for numbers)
✓ How to use int(input()) to convert strings to numbers for math operations
✓ The critical difference between hard-coded and dynamic values
✓ Why storing input in variables is necessary
✓ Two different ways to combine strings with print() (comma vs +)
"""
