"""
================================================================================
PYTHON LOGIC & OPERATORS - PART 2: COMPARISON & LOGICAL OPERATORS
================================================================================
Learning Focus: Comparing values and combining conditions with logical operators
"""


# ============================================================================
# 1. COMPARISON OPERATORS - OVERVIEW
# ============================================================================
"""
Compare two values and return True or False based on the result

┌──────────┬────────────────────────┬────────────────────────────────────┐
│ Operator │ Meaning                │ Purpose                            │
├──────────┼────────────────────────┼────────────────────────────────────┤
│    ==    │ Equal to               │ Checks if two values are equal     │
│    !=    │ Not equal              │ Checks if two values are not equal │
│    <     │ Less than              │ Checks if left value is smaller    │
│    <=    │ Less than or equal     │ Checks if left value is smaller    │
│          │                        │ or equal to right value            │
│    >     │ Greater than           │ Checks if left value is greater    │
│    >=    │ Greater than or equal  │ Checks if left value is greater    │
│          │                        │ or equal to right value            │
└──────────┴────────────────────────┴────────────────────────────────────┘
"""


# ============================================================================
# 2. COMPARISON OPERATORS - Basic Usage
# ============================================================================

print(10 == 10)   # Output: True  (equal to)
print(10 != 10)   # Output: False (not equal to)
print(7 > 3)      # Output: True  (greater than)
print(7 >= 3)     # Output: True  (greater than or equal)
print(3 < 7)      # Output: True  (less than)
print(7 <= 7)     # Output: True  (less than or equal)


# ============================================================================
# 3. COMPARING STRINGS
# ============================================================================

# Strings can be compared alphabetically, not just numbers!
print("a" < "b")
# Output: True (a comes before b alphabetically)

print("a" == "b")
# Output: False


# IMPORTANT: Python is case-sensitive
# "a" and "A" are treated as completely different values
print("a" == "A")
# Output: False


# ⚠️ Common Mistake - Don't confuse = and ==:
# =  → assigns a value:    name = "Alice"
# == → compares values:    name == "Alice"


# ============================================================================
# 4. CHAINED COMPARISONS
# ============================================================================

# You can check multiple conditions in one line, just like in math

print(1 < 4 < 6)
# Output: True (1 is less than 4, AND 4 is less than 6)

print(5 < 4 < 6)
# Output: False (5 is NOT less than 4)


# Use Case: Range Validation (similar to SQL's BETWEEN)
# Check if value is between two bounds

age = 35
print(18 <= age <= 30)
# Output: False (35 is not between 18 and 30)

age = 25
print(18 <= age <= 30)
# Output: True (25 is between 18 and 30)


# ============================================================================
# 5. LOGICAL OPERATORS - OVERVIEW
# ============================================================================
"""
Used to combine multiple boolean expressions

┌──────────┬────────────────────────┬────────────────────────────────────┐
│ Operator │ Meaning                │ Purpose                            │
├──────────┼────────────────────────┼────────────────────────────────────┤
│   and    │ Logical AND            │ Returns True if BOTH expressions   │
│          │                        │ are True                           │
│   or     │ Logical OR             │ Returns True if AT LEAST ONE       │
│          │                        │ expression is True                 │
│   not    │ Logical NOT            │ Inverts the boolean value          │
│          │                        │ (True → False, False → True)       │
└──────────┴────────────────────────┴────────────────────────────────────┘

Truth Tables:

    AND:                          OR:                    NOT:
    T and T → True                T or T → True          not True  → False
    T and F → False               T or F → True          not False → True
    F and T → False               F or T → True
    F and F → False               F or F → False
"""


# ============================================================================
# 6. LOGICAL AND - Both Must Be True
# ============================================================================

print(3 > 1 and 5 < 1)
# Output: False (first is True, second is False → False)

print(3 > 1 and 5 > 1)
# Output: True (both are True → True)


# Use Case: System Health Check
# Flag alert only if BOTH cpu AND memory are overloaded
cpu_usage = 70
memory_usage = 95

print(cpu_usage > 90 and memory_usage > 90)
# Output: False (cpu is fine, only memory is overloaded)

print(cpu_usage > 90 or memory_usage > 90)
# Output: True (at least one is overloaded)


# Use Case: User Login Validation
# Both email AND password must be correct to allow login
email = True
password = False

print(email and password)
# Output: False (password is wrong → access denied)


# ============================================================================
# 7. LOGICAL OR - At Least One Must Be True
# ============================================================================

print(3 > 1 or 5 < 1)
# Output: True (first is True → True, second doesn't matter)

print(3 > 1 or 5 > 1)
# Output: True (both are True → True)

# Use Case: Flexible Access
# Allow if user is logged in OR is a guest
is_logged_in = True
is_guest = False

print(is_logged_in or is_guest)
# Output: True (logged in → access granted)


# ============================================================================
# 8. LOGICAL NOT - Invert the Value
# ============================================================================

print(not 3 > 2)
# Output: False (3 > 2 is True → not True → False)

print(not True)
# Output: False

print(not False)
# Output: True

print(not not False)
# Output: False (double negation = back to original)


# not with truthy/falsy values:
name = ""
print(not name)
# Output: True (empty string is falsy → not False → True)

print(not 0)
# Output: True (0 is falsy → not False → True)


# ============================================================================
# 9. OPERATOR PRECEDENCE - and vs or
# ============================================================================

# ⚠️ IMPORTANT: 'and' has HIGHER priority than 'or'
# Just like multiplication (*) has higher priority than addition (+)

"""
ANALYSIS OF LOGICAL OPERATOR PRECEDENCE

Variables:
    X = 5, Y = 8, Z = 6
    Expression: X == 5 or Y > 5 and Z < 4

Without Parentheses (default precedence):
    Step 1: Evaluate 'and' FIRST  → (8 > 5 and 6 < 4) → (True and False) → False
    Step 2: Evaluate 'or'  SECOND → (5 == 5 or False)  → (True or False)  → True
    Final Output: True

With Parentheses (override precedence):
    Expression: (5 == 5 or 8 > 5) and 6 < 4
    Step 1: Evaluate Parentheses  → (True or True)     → True
    Step 2: Evaluate 'and'        → (True and 6 < 4)   → (True and False) → False
    Final Output: False
"""

X = 5
Y = 8
Z = 6

result_without_parentheses = X == 5 or Y > 5 and Z < 4
print(f"Without parentheses: {result_without_parentheses}")
# Output: Without parentheses: True

result_with_parentheses = (X == 5 or Y > 5) and Z < 4
print(f"With parentheses: {result_with_parentheses}")
# Output: With parentheses: False


# ============================================================================
# 10. PRACTICAL TASK - Access Control System
# ============================================================================

# Allow access ONLY if:
# User is logged in OR is a guest
# BUT they must NOT be banned

is_logged_in = True
is_guest = False
is_banned = True

# Without parentheses (wrong logic - 'and' evaluated first)
print(is_logged_in or is_guest and not is_banned)
# Output: True (incorrect - banned user gets access!)

# With parentheses (correct logic - groups or conditions first)
print((is_logged_in or is_guest) and not is_banned)
# Output: False (correct - banned user is blocked!)

# Lesson: Always use parentheses to make logic clear and correct!


# ============================================================================
# 11. PYTHON CHALLENGES
# ============================================================================

# --- Challenge 1: User Validation ---
# Check if name is not empty AND age is at least 18

name = "Alice"
age = 20

is_valid_user = name != "" and age >= 18
print(f"Challenge 1 - Valid user: {is_valid_user}")
# Output: Challenge 1 - Valid user: True


# --- Challenge 2: Password Strength ---
# Check if password is at least 8 characters AND has no spaces

password = "SecurePassword123"

is_valid_password = len(password) >= 8 and " " not in password
print(f"Challenge 2 - Valid password: {is_valid_password}")
# Output: Challenge 2 - Valid password: True


# --- Challenge 3: Email Validation ---
# Check if email is not empty, contains '@', and ends with '.com'

email = "user@example.com"

is_valid_email = email != "" and "@" in email and email.endswith(".com")
print(f"Challenge 3 - Valid email: {is_valid_email}")
# Output: Challenge 3 - Valid email: True


# --- Challenge 4: Username Validation ---
# Check if username is a string, is not None, and is longer than 5 characters

username = "coder_pro"

is_valid_username = isinstance(
    username, str) and username is not None and len(username) > 5
print(f"Challenge 4 - Valid username: {is_valid_username}")
# Output: Challenge 4 - Valid username: True


# --- Challenge 5: Authorization System ---
# Check if user is admin OR moderator
# AND either not banned OR has verified email

is_admin = True
is_moderator = False
is_banned = False
has_verified_email = True

# Parentheses group 'or' conditions before checking 'and' relationship
is_authorized = (is_admin or is_moderator) and (
    not is_banned or has_verified_email)
print(f"Challenge 5 - Is authorized: {is_authorized}")
# Output: Challenge 5 - Is authorized: True


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
COMPARISON & LOGICAL OPERATORS - ESSENTIAL FACTS

Comparison Operators (return True/False):
    • ==    → Equal to
    • !=    → Not equal to
    • >     → Greater than
    • <     → Less than
    • >=    → Greater than or equal
    • <=    → Less than or equal

Logical Operators:
    • and   → BOTH must be True
    • or    → AT LEAST ONE must be True
    • not   → INVERTS the boolean value

Operator Precedence (High to Low):
    1. not     (evaluated first)
    2. and     (evaluated second)
    3. or      (evaluated last)

Important Notes:
    • = assigns, == compares (don't mix them up!)
    • Strings are compared alphabetically
    • Python string comparison is CASE-SENSITIVE ("a" ≠ "A")
    • 'and' has higher priority than 'or' (use parentheses to be safe)
    • Chained comparisons work like SQL BETWEEN: 18 <= age <= 30
    • Always use parentheses for complex logic to avoid bugs
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ All six comparison operators: ==, !=, >, <, >=, <=
✓ That strings can be compared alphabetically
✓ That Python string comparison is case-sensitive
✓ The difference between = (assignment) and == (comparison)
✓ Chained comparisons: 18 <= age <= 30 (similar to SQL BETWEEN)
✓ The three logical operators: and, or, not
✓ Truth tables for and, or, and not
✓ That 'and' has higher precedence than 'or'
✓ How operator precedence can change the result unexpectedly
✓ Why parentheses are important for complex conditions
✓ How to combine comparison and logical operators for:
  ✓ User validation (name + age)
  ✓ Password strength checking
  ✓ Email format validation
  ✓ Authorization systems (admin/moderator + banned status)
✓ That double not (not not) returns the original value
✓ How not works with truthy/falsy values
"""
