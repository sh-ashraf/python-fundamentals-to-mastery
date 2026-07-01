"""
================================================================================
PYTHON FUNDAMENTALS - VARIABLES
================================================================================
Learning Focus: Creating, storing, and reusing values with variables
"""


# ============================================================================
# 1. BASIC VARIABLE USAGE
# ============================================================================
# Variables store data that can be reused throughout your program

name = "Shehab"
language = "Python"

# Using variables in print statements:
print("My name is", name)
# Output: My name is Shehab

print(name, "is learning", language)
# Output: Shehab is learning Python

print(name, "wants to become", language, "expert")
# Output: Shehab wants to become Python expert

# Benefits of using variables:
# - Write "Shehab" once, use it multiple times
# - Change the value in one place, it updates everywhere
# - Makes code cleaner and easier to maintain


# ============================================================================
# 2. PRACTICAL CHALLENGE - EMAIL GENERATOR
# ============================================================================
# Using variables to build dynamic email addresses and links

email_domain = "@datawithbaraa.com"
link = "www.datawithbaraa.com"

# Generate different email addresses using the same domain:
print("info" + email_domain)
# Output: info@datawithbaraa.com

print("support" + email_domain)
# Output: support@datawithbaraa.com

print(link)
# Output: www.datawithbaraa.com

# Real-world use case:
# If the domain changes, you only update it once in the variable!


# ============================================================================
# 3. UNDERSTANDING VARIABLES
# ============================================================================
"""
What is a Variable?
    A named container that stores a value in computer memory

Why Use Variables?
    • Makes programs dynamic and flexible
    • Allows reusing values without retyping them
    • Enables updating values throughout the program
    • Improves code readability and maintenance

Key Characteristics:
    ✓ Stored in memory during program execution
    ✓ Reusable anywhere in your code
    ✓ Updatable - you can change the value anytime
    ✓ Named meaningfully to describe what they store

SYNTAX:
    variable_name = value

EXAMPLES:
    name = "Shehab"          # String (text)
    age = 25                 # Integer (whole number)
    price = 19.99            # Float (decimal)
    is_student = True        # Boolean (True/False)
"""


# ============================================================================
# 4. VARIABLE NAMING BEST PRACTICES
# ============================================================================
"""
Good variable names:
    ✓ user_name, email_domain, total_price
    ✓ Descriptive and meaningful
    ✓ Use lowercase with underscores (snake_case)

Bad variable names:
    ✗ x, y, data, temp
    ✗ Too short and unclear
    ✗ Don't describe what they store

Python Naming Rules:
    • Must start with a letter or underscore
    • Can contain letters, numbers, and underscores
    • Cannot start with a number
    • Case-sensitive (name ≠ Name)
    • Cannot use Python keywords (if, for, while, etc.)
"""


# ============================================================================
# 5. UPDATING VARIABLES
# ============================================================================
# Variables can be reassigned new values at any time

language = "Python"
print(language)
# Output: Python

language = "SQL"  # Update the value
print(language)
# Output: SQL

# The old value ("Python") is replaced with the new value ("SQL")


# ============================================================================
# 6. VARIABLE OPERATIONS
# ============================================================================

# You can perform operations with variables
age = 25
print(age + 5)
# Output: 30

# Combine variables
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
# Output: John Doe


# ============================================================================
# 7. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to create and use variables in Python
✓ How variables make programs reusable and maintainable
✓ How to print variable values combined with text
✓ How to build dynamic content using string concatenation
✓ The difference between using comma (,) and plus (+) in print
✓ Real-world application: building email addresses with variables
✓ Best practices for naming variables clearly
✓ That variables can be updated/reassigned anytime
✓ Python naming rules and conventions (snake_case)
"""