"""
================================================================================
PYTHON LOGIC & OPERATORS - PART 1: BOOLEAN FUNCTIONS
================================================================================
Learning Focus: Understanding boolean values, conversion, and validation functions
"""


# ============================================================================
# CONTROL FLOW OVERVIEW - THE BIG PICTURE
# ============================================================================
"""
Python Control Flow - Complete Reference Table

┌──────────────────────┬───────────────────────┬────────────────────────────────────┐
│ Category             │ Keywords / Operators  │ Purpose                            │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Conditional          │ if                    │ Execute code if condition is True  │
│ Statements           │ elif                  │ Check another condition            │
│                      │ else                  │ Execute fallback code              │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Loop Types           │ for                   │ Iterate over sequence/range        │
│                      │ while                 │ Repeat while condition is True     │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Loop Control         │ break                 │ Exit loop completely               │
│                      │ continue              │ Skip current iteration             │
│                      │ pass                  │ Placeholder / do nothing           │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Boolean Values       │ True                  │ Boolean true value                 │
│                      │ False                 │ Boolean false value                │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Boolean Functions    │ bool()                │ Convert to boolean                 │
│                      │ any()                 │ True if any item is True           │
│                      │ all()                 │ True if all items are True         │
│                      │ isinstance()          │ Check object type                  │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Comparison           │ ==                    │ Equal to                           │
│ Operators            │ !=                    │ Not equal to                       │
│                      │ <  >                  │ Less / Greater than                │
│                      │ <= >=                 │ Less / Greater or equal            │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Logical Operators    │ and                   │ Both conditions must be True       │
│                      │ or                    │ One condition must be True         │
│                      │ not                   │ Reverse boolean value              │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Membership           │ in                    │ Value exists in collection         │
│ Operators            │ not in                │ Value does not exist               │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Identity Operators   │ is                    │ Same object in memory              │
│                      │ is not                │ Different objects                  │
└──────────────────────┴───────────────────────┴────────────────────────────────────┘

Note: This chapter focuses on Boolean Values and Functions.
      Later chapters will cover Conditionals and Loops.
"""


# ============================================================================
# 1. BOOLEAN BASICS - True and False
# ============================================================================

# Python has two boolean values: True and False
# IMPORTANT: Must be capitalized (not true/false)

print(True)
# Output: True

print(False)
# Output: False

# Check the type of boolean values
print(type(True))
# Output: <class 'bool'>

print(type(False))
# Output: <class 'bool'>


# ============================================================================
# 2. BOOLEAN CONVERSION - bool() Function
# ============================================================================

# --- bool() Function ---
# bool(value) → Converts any value to boolean

# Rule 1: Non-empty and non-zero values = True
# Rule 2: Empty or zero values = False


# --- Values that are True (Truthy) ---

print(bool(123))
# Output: True (non-zero number)

print(bool(-5))
# Output: True (non-zero, even negative)

print(bool("Hi"))
# Output: True (non-empty string)

print(bool([1, 2, 3]))
# Output: True (non-empty list)


# --- Values that are False (Falsy) ---

print(bool())
# Output: False (no argument = default False)

print(bool(0))
# Output: False (zero)

print(bool(0.0))
# Output: False (zero float)

print(bool(""))
# Output: False (empty string)

print(bool([]))
# Output: False (empty list)

print(bool({}))
# Output: False (empty dictionary)

print(bool(None))
# Output: False (None represents "no value")


# ============================================================================
# 3. IMPORTANT DISTINCTION - None vs Empty String
# ============================================================================
"""
Understanding None vs Empty String:

None:
    • Means "no value exists" or "value is missing"
    • Used when something hasn't been set yet
    • Different from empty

Empty String (""):
    • The value exists, but it's an empty string
    • Has a value (empty), not missing

Example:
    name = None      → No name assigned yet
    name = ""        → Name is assigned but empty
"""

print(bool(None))
# Output: False

print(bool(""))
# Output: False

# Both are False, but they mean different things!
print(None == "")
# Output: False (they are NOT the same)


# ============================================================================
# 4. PRACTICAL EXAMPLES - Truthy and Falsy
# ============================================================================

# Example 1: Check if user provided input
user_input = input("Enter your name (or press Enter): ")

if bool(user_input):
    print(f"Hello, {user_input}!")
else:
    print("No name provided")
# If user presses Enter, user_input = "" (Falsy)


# Example 2: Check if list has items
shopping_cart = []

if bool(shopping_cart):
    print("You have items in cart")
else:
    print("Cart is empty")
# Output: Cart is empty


# ============================================================================
# 5. ANY() FUNCTION - At Least One True
# ============================================================================

# --- any() Function ---
# any(iterable) → Returns True if AT LEAST ONE value is True

# Use Case: Flexible Registration
# Allow registration if ANY field is filled

email = ""
phone = "0176-123456"
username = ""

# Check if any contact method exists
has_contact = any([email, phone, username])
print(has_contact)
# Output: True (phone is filled)

# Practical example
if any([email, phone, username]):
    print("Registration allowed - at least one contact method provided")
else:
    print("Registration failed - no contact information")
# Output: Registration allowed - at least one contact method provided


# More any() examples:
print(any([False, False, True]))
# Output: True (one True is enough)

print(any([0, "", None, "Hi"]))
# Output: True ("Hi" is truthy)

print(any([False, 0, "", None]))
# Output: False (all are falsy)


# ============================================================================
# 6. ALL() FUNCTION - All Must Be True
# ============================================================================

# --- all() Function ---
# all(iterable) → Returns True if ALL values are True

# Use Case: Strict Registration
# Allow registration ONLY if ALL fields are filled

email = "baraa@gmail.com"
phone = "0176-123456"
username = "baraa123"

# Check if all required fields exist
all_filled = all([email, phone, username])
print(all_filled)
# Output: True (all fields have values)

# Practical example
if all([email, phone, username]):
    print("Registration complete - all fields provided")
else:
    print("Registration incomplete - fill all fields")
# Output: Registration complete - all fields provided


# More all() examples:
print(all([True, True, True]))
# Output: True (all are True)

print(all([True, False, True]))
# Output: False (one False breaks it)

print(all([1, 2, 3, "Hi"]))
# Output: True (all are truthy)

print(all([1, 2, 0, "Hi"]))
# Output: False (0 is falsy)


# ============================================================================
# 7. ANY() VS ALL() - COMPARISON
# ============================================================================
"""
Quick Comparison:

any():
    • Returns True if AT LEAST ONE item is True
    • Use when: "Is there anything valid?"
    • Example: Has user provided any contact method?

all():
    • Returns True if ALL items are True
    • Use when: "Is everything valid?"
    • Example: Has user filled all required fields?

┌────────────────┬──────────┬──────────┐
│ Values         │ any()    │ all()    │
├────────────────┼──────────┼──────────┤
│ [T, T, T]      │ True     │ True     │
│ [T, T, F]      │ True     │ False    │
│ [T, F, F]      │ True     │ False    │
│ [F, F, F]      │ False    │ False    │
└────────────────┴──────────┴──────────┘
"""


# ============================================================================
# 8. ISINSTANCE() FUNCTION - Type Checking
# ============================================================================

# --- isinstance() Function ---
# isinstance(value, type) → Checks if value belongs to a data type

print(isinstance(123, int))
# Output: True (123 is an integer)

print(isinstance(123, str))
# Output: False (123 is not a string)

print(isinstance(True, bool))
# Output: True (True is a boolean)

print(isinstance(True, int))
# Output: True (bool is a subclass of int!)

# Interesting fact: In Python, bool is a subclass of int
# True = 1, False = 0
print(True == 1)
# Output: True

print(False == 0)
# Output: True


# Use Case: Validate function argument
def calculate_discount(price):
    if isinstance(price, (int, float)):
        return price * 0.9
    else:
        return "Invalid price - must be a number"


print(calculate_discount(100))
# Output: 90.0

print(calculate_discount("100"))
# Output: Invalid price - must be a number


# ============================================================================
# 9. STRING METHOD - endswith()
# ============================================================================

# --- endswith() Method ---
# string.endswith(substring) → Checks if string ends with substring
# Returns: bool (True/False)

print("Hello".endswith("o"))
# Output: True

print("Hello".endswith("O"))
# Output: False (case-sensitive!)

# Use Case: File type validation
filename = "report.pdf"

if filename.endswith(".pdf"):
    print("Valid PDF file")
else:
    print("Not a PDF file")
# Output: Valid PDF file

# Check multiple extensions
allowed_extensions = (".jpg", ".png", ".gif")
image_file = "photo.png"

if image_file.endswith(allowed_extensions):
    print("Valid image file")
# Output: Valid image file


# ============================================================================
# 10. COMBINING BOOLEAN FUNCTIONS
# ============================================================================

# Example 1: Form validation with any()
username = "john_doe"
email = ""
phone = ""

has_identifier = any([username, email, phone])
print(f"Can proceed with registration: {has_identifier}")
# Output: Can proceed with registration: True


# Example 2: Complete profile check with all()
name = "John"
age = 25
city = "Cairo"
bio = "Python developer"

profile_complete = all([name, age, city, bio])
print(f"Profile is complete: {profile_complete}")
# Output: Profile is complete: True


# Example 3: Type checking with isinstance()
values = [123, "text", 45.6, True]

numbers = [v for v in values if isinstance(
    v, (int, float)) and not isinstance(v, bool)]
print(f"Numbers only: {numbers}")
# Output: Numbers only: [123, 45.6]


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
BOOLEAN FUNCTIONS - ESSENTIAL FACTS

Boolean Values:
    • True, False (must be capitalized)
    • Type: <class 'bool'>

bool() Function:
    • Converts any value to boolean
    • Truthy: non-zero, non-empty values
    • Falsy: 0, 0.0, "", [], {}, None, False

Falsy Values (all return False):
    • False
    • None
    • 0, 0.0
    • "" (empty string)
    • [] (empty list)
    • {} (empty dict)
    • () (empty tuple)

Boolean Functions:
    • any(iterable)      → True if ANY item is True
    • all(iterable)      → True if ALL items are True
    • isinstance(v, t)   → True if v is type t
    • endswith(suffix)   → True if string ends with suffix

Important Notes:
    • None ≠ "" (None is missing, "" is empty)
    • bool is a subclass of int (True=1, False=0)
    • isinstance() can check multiple types: isinstance(x, (int, float))
    • String methods like endswith() are case-sensitive
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ The two boolean values: True and False (must be capitalized)
✓ How to convert values to boolean with bool()
✓ The difference between truthy and falsy values
✓ Complete list of falsy values in Python
✓ Critical difference between None (missing) and "" (empty)
✓ How to use any() to check if at least one value is True
✓ How to use all() to check if all values are True
✓ When to use any() vs all() for validation
✓ How to check data types with isinstance()
✓ That bool is a subclass of int (True=1, False=0)
✓ How to use endswith() for string suffix checking
✓ Real-world use cases: form validation, file type checking, profile completion
"""
