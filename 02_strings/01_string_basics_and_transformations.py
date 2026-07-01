"""
================================================================================
PYTHON STRINGS - PART 1: BASICS AND METHODS
================================================================================
Learning Focus: String types, math operations, and transformation methods
"""


# ============================================================================
# STRING OPERATIONS OVERVIEW
# ============================================================================
"""
Quick Reference Table:

┌─────────────┬────────────┬──────────────────┬─────────────────┬──────────────┬─────────────┐
│ Types       │ Math       │ Transformations  │ Cleaning        │ Search       │ Validation  │
├─────────────┼────────────┼──────────────────┼─────────────────┼──────────────┼─────────────┤
│ type()      │ len()      │ replace()        │ strip()         │ startswith() │ isalpha()   │
│ str()       │ count()    │ 'H' + 'i'        │ lstrip()        │ endswith()   │ isnumeric() │
│             │            │ f"{}"            │ rstrip()        │ find()       │             │
│             │            │ split()          │                 │ in operator  │             │
│             │            │ 'ha' * 2         │ Case Cleaning:  │              │             │
│             │            │                  │ lower()         │              │             │
│             │            │ Extraction:      │ upper()         │              │             │
│             │            │ 'cat'[0]         │                 │              │             │
│             │            │ 'cat'[1:3]       │                 │              │             │
└─────────────┴────────────┴──────────────────┴─────────────────┴──────────────┴─────────────┘
"""


# ============================================================================
# 1. STRING TYPES - type() and str()
# ============================================================================

# --- type() Function ---
# type(value) → Returns the data type of a value

name = "Shehab"
print(type(name))  # Output: <class 'str'>


# --- str() Function ---
# str(value) → Converts any value into a string

age = 24
print(type(age))  # Output: <class 'int'>

# IMPORTANT: Can't combine string with integer using + operator
# Solution: Convert the integer to string first
print("Your age is: " + str(age))  # Output: Your age is: 24

# Testing that the original variable remains unchanged
age = age + 5
print(age)  # Output: 29 (still an integer)


# ============================================================================
# 2. STRING MATH OPERATIONS
# ============================================================================

# --- len() Function ---
# len(value) → Returns the number of characters in a string (including spaces)

# Use Case 1: Check Password Quality
password = "123a123"
print(len(password))  # Output: 7

if len(password) < 8:
    print("Your Password is too short!")
else:
    print("Password ✅✅")

# NOTE: len() counts EVERYTHING, including spaces and special characters


# --- count() Method ---
# string.count(substring) → Returns how many times substring appears

# Use Case 1: Word Frequency Check
text = """
Python is easy to learn.
Python is powerful$.
many people love python.
"""

# IMPORTANT: Python is case-sensitive!
print(text.count("Python"))  # Output: 2 (doesn't count "python")

# Use Case 2: Detect Quality Issues
# Count unwanted characters in your data
print(text.count("$"))  # Output: 1


# ============================================================================
# 3. DATA TRANSFORMATIONS - replace()
# ============================================================================

# --- replace() Method ---
# string.replace(old, new) → Swaps part of the text with something new

# Use Case 1: Clean Numeric Formats
# Replace commas with dots in European-style decimal numbers
price = "1234,56"
print(price.replace(",", "."))  # Output: 1234.56

# Use Case 2: Change Phone Number Format
phone = "176-1234-56"
print(phone.replace("-", "/"))  # Output: 176/1234/56

# Use Case 3: Remove Unwanted Parts
# Replace with empty string ("") to remove characters
print(phone.replace("-", ""))  # Output: 176123456

# Use Case 4: Chain Multiple replacements (Left-to-Right)
price = "$1,299.99"
clean_price = price.replace("$", "").replace(",", "")
print(clean_price)  # Output: 1299.99


# --- Python Challenge: Clean Phone Number ---
# Convert messy phone number into clean digit-only format

phone_num = "+49 (176) 123-4567"
clean_phone = (phone_num.replace("+", "00").replace(" ",
               "").replace("(", "").replace(")", "").replace("-", ""))
print(clean_phone)  # Output: 0049176123456


# ============================================================================
# 4. DATA TRANSFORMATIONS - Concatenation
# ============================================================================

# --- String Concatenation with + Operator ---
# 'string' + 'string' → Joins two strings into one

first_name = "Michael"
last_name = "Scott"
full_name = first_name + " " + last_name
print(full_name)  # Output: Michael Scott

# Use Case: Build File Paths Dynamically
folder = "C:/Users/Baraa/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)  # Output: C:/Users/Baraa/report.csv


# ============================================================================
# 5. DATA TRANSFORMATIONS - f-strings (Formatted Strings)
# ============================================================================

# --- f-string Syntax ---
# f"text {variable}" → Inserts variables directly inside strings

name = "sam"
age = 34
is_student = False

# Old Way (Hard to read):
print("my name is " + name + ", I am " + str(age) +
      " years old, and student status is " + str(is_student) + ".")

# Modern Way with f-strings (Clean and readable):
print(
    f"my name is {name}, I am {age} years old, and student status is {is_student}.")

# f-strings can contain expressions, not just variables:
print(f"2 + 3 = {2 + 3}")  # Output: 2 + 3 = 5

# Printing literal braces: Use double braces {{ }}
print(f"{{this is me}}")  # Output: {this is me}


# ============================================================================
# 6. DATA TRANSFORMATIONS - split()
# ============================================================================

# --- split() Method ---
# string.split(separator) → Breaks a string into a list of smaller parts

# Use Case 1: Break a date into components
timestamp = "2026-09-20"
print(timestamp.split("-"))  # Output: ['2026', '09', '20']

# Use Case 2: Parse CSV data
csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # Output: ['1234', 'Max', 'USA', '1970-10-05', 'M']


# ============================================================================
# 7. DATA TRANSFORMATIONS - Repetition
# ============================================================================

# --- String Repetition with * Operator ---
# string * number → Repeats the string multiple times

print("ha" * 3)  # Output: hahaha

# Use Case: Style Your Logs
# Create visual separators in console output
print("#" * 30)  # Output: ##############################


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
STRING OPERATIONS - ESSENTIAL FACTS

Type Functions:
    • type(value)     → Check data type
    • str(value)      → Convert to string

Math Operations:
    • len(string)     → Count characters (including spaces)
    • string.count(x) → Count occurrences (case-sensitive)

Transformations:
    • string.replace(old, new)  → Swap or remove text
    • string1 + string2         → Concatenate strings
    • f"{variable}"             → Format strings (modern way)
    • string.split(separator)   → Break into list
    • string * n                → Repeat string n times

Important Notes:
    • Strings are CASE-SENSITIVE in Python
    • Can't use + to combine string and number (use str() or f-string)
    • replace() can be chained for multiple replacements
    • f-strings are cleaner than + concatenation
    • Use {{ }} to print literal braces in f-strings
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to check and convert data types with type() and str()
✓ How to count string length with len() and substring occurrences with count()
✓ How to clean and transform strings with replace()
✓ The difference between + concatenation and f-strings
✓ How to split strings into lists for data processing
✓ How to repeat strings with the * operator
✓ That Python string operations are case-sensitive
✓ How to chain multiple replace() methods for complex cleaning
✓ Real-world use cases: password validation, phone formatting, CSV parsing
"""
