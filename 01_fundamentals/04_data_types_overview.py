"""
================================================================================
PYTHON DATA TYPES - STUDY NOTES
================================================================================
Learning Focus: Understanding Python's type system and working with different data types
"""


# ============================================================================
# 1. DATA TYPES OVERVIEW - THE BIG PICTURE
# ============================================================================
"""
Python Data Types Hierarchy:

                            DATA TYPES
                                |
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
    NO VALUE              SINGLE VALUE            MULTI VALUES
   (NoneType)             (Primitives)            (Collections)
        │                       │                       │
      None          ┌───────────┼───────────┐      ┌────┴────┐
                    │           │           │      │         │
                   int       float       str      list      dict
                               │          bool    set       tuple
                            complex


Category Breakdown:
    
    NO VALUE:
        • None → Represents absence of value
    
    SINGLE VALUE (Primitives):
        • int     → Whole numbers (1, 42, -5)
        • float   → Decimal numbers (3.14, -0.5)
        • str     → Text ("Hello", 'Python')
        • bool    → True or False
        • complex → Complex numbers (3+4j)
    
    MULTI VALUES (Collections):
        • list    → Ordered, mutable [1, 2, 3]
        • tuple   → Ordered, immutable (1, 2, 3)
        • set     → Unordered, unique {1, 2, 3}
        • dict    → Key-value pairs {"name": "Shehab"}
"""


# ============================================================================
# 2. CHECKING DATA TYPES WITH type()
# ============================================================================
# Use type() to identify what data type a value has

# --- INTEGER (int) ---
# Whole numbers without decimal points
a = 10
print(type(a))  # Output: <class 'int'>


# --- FLOAT (float) ---
# Numbers with decimal points
b = 3.15
print(type(b))  # Output: <class 'float'>


# --- STRING (str) ---
# Text values enclosed in quotes (single or double)
c = "Hello"
print(type(c))  # Output: <class 'str'>

d = 'Hi'
print(type(d))  # Output: <class 'str'>

# Important: Numbers in quotes are strings, not integers!
e = "1234"
print(type(e))  # Output: <class 'str'> (NOT int)


# --- BOOLEAN (bool) ---
# Only two values: True or False (must be capitalized!)
f = True
print(type(f))  # Output: <class 'bool'>

g = False
print(type(g))  # Output: <class 'bool'>


# --- NONETYPE (None) ---
# Represents "no value" or "not set yet"
h = None
print(type(h))  # Output: <class 'NoneType'>


# ============================================================================
# 3. COMMON BEGINNER CONFUSION - None vs Empty String
# ============================================================================

# None = no value at all
h = None
print(type(h))  # Output: <class 'NoneType'>

# Empty string = still a string, just with zero characters
i = ""
print(type(i))  # Output: <class 'str'>

# Whitespace string = still a string, contains spaces
j = "  "
print(type(j))  # Output: <class 'str'>

# Key Insight:
# None means "nothing exists here"
# "" means "text exists here, but it's empty"


# ============================================================================
# 4. DYNAMIC TYPING IN PYTHON
# ============================================================================
"""
Python automatically detects and assigns data types.
You don't need to declare types explicitly (unlike C++ or Java).

Data types can change during runtime:
"""

x = 10          # x is int
print(type(x))  # <class 'int'>

x = "Python"    # Now x is str
print(type(x))  # <class 'str'>

x = 3.14        # Now x is float
print(type(x))  # <class 'float'>

# This is called DYNAMIC TYPING - types can change!


# ============================================================================
# 5. PRACTICAL CHALLENGE - USING MULTIPLE DATA TYPES
# ============================================================================

# 1. Your age (int)
age = 21

# 2. Your height in cm (float)
height = 175.5

# 3. Your name (str)
name = "Shehab"

# 4. Are you a student? (bool)
is_student = True

# 5. Something with no value yet (NoneType)
future_job = None


# Display all values
print("\n" + "="*50)
print("VALUES:")
print("="*50)
print(age, height, name, is_student, future_job)


# Display all data types
print("\n" + "="*50)
print("DATA TYPES:")
print("="*50)
print(type(age), type(height), type(name), type(is_student), type(future_job))


# Bonus: Working with lengths
print("\n" + "="*50)
print("LENGTH EXAMPLES:")
print("="*50)
print("Length of name (character count):", len(name))
print("Bit length of age:", age.bit_length())  # Number of bits needed to represent the int


# ============================================================================
# 6. KEY CONCEPTS SUMMARY
# ============================================================================
"""
DATA TYPES - ESSENTIAL FACTS

What are data types?
    • Every value in Python has a data type
    • Data types tell Python how to handle and store values
    • They determine what operations you can perform

How does Python handle types?
    • Automatic detection (type inference)
    • Dynamic typing (types can change at runtime)
    • Type checking with type() function

Three main categories:
    1. No Value     → NoneType
    2. Single Value → int, str, bool, float, complex
    3. Multi Values → list, tuple, set, dict

Important notes:
    • Values are objects of a data type class
    • "1234" is a string, not an integer
    • None ≠ "" (empty string)
    • bool values must be capitalized: True, False
"""


# ============================================================================
# 7. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ The three main categories of Python data types
✓ How to use type() to identify variable types
✓ The critical difference between None, empty string (""), and whitespace string ("  ")
✓ How Python uses dynamic typing (types can change)
✓ How to define and work with int, float, str, bool, and NoneType
✓ That numbers in quotes ("123") are strings, not integers
✓ Boolean values must be capitalized (True/False)
✓ How to check string length with len()
✓ How to check integer bit length with .bit_length()
"""