"""
================================================================================
PYTHON CONDITIONAL STATEMENTS - PART 3: INLINE IF AND MATCH CASE
================================================================================
Learning Focus: Ternary (inline if) expressions, match-case statements,
                and applying conditionals to real validation challenges
"""


# ============================================================================
# 1. INLINE IF - Ternary Expression
# ============================================================================

# Standard if/else:
# if condition:
#     do A
# else:
#     do B

# Inline if compresses this into one readable line:
#     do A  if  condition  else  do B

"""
+-------------------------------------------------------+
|                   in-line If Statement                |
|                                                       |
|          do A   if   Condition1   else   do B         |
|                                                       |
|            "Quick, short, simple check"               |
+-------------------------------------------------------+
"""

# --- Simple Inline If (two outcomes) ---
score = 100

# Standard way
if score >= 90:
    print("A")
else:
    print("F")
# Output: A

# Inline way (same logic, one line)
grade = "A" if score >= 90 else "F"
print(grade)
# Output: A


# --- Chained Inline If (three or more outcomes) ---
score = 80

# Standard way
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
# Output: B

# Inline way (chained, use parentheses for readability)
grade = (
    "A" if score >= 90 else
    "B" if score >= 80 else
    "F"
)
print(grade)
# Output: B


# --- When to Use Each ---
# Simple logic   → inline if    (quick one-liner, easy to read)
# Complex logic  → classical if (multiple conditions, nested logic)


# ============================================================================
# 2. MATCH CASE - Pattern Matcher
# ============================================================================

# match/case evaluates a value against multiple exact values.
# Runs the code block of the first matching case.
# Think of it as a "Pattern Matcher":
#     "Match one exact value to multiple options"

"""
+-------------------------------------------------------+
|                     case-match                        |
|                                                       |
|    match  Payment:          "Pattern Matcher"         |
|        case "Cash":                                   |
|        case "Visa":    "Match one exact value         |
|        case _:          to multiple options"          |
|                                                       |
+-------------------------------------------------------+
"""

# --- Syntax ---
# match value:
#     case option_1:
#         do A
#     case option_2:
#         do B
#     case _:            ← wildcard: matches everything else
#         do default

# Task: Convert full country names into 2-letter abbreviations


country = "Egypt"

# Using if/elif/else (flexible logic and multiple conditions)
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown Country")
# Output: EG


# Using match/case (exact value matching, cleaner for fixed options)
match country:
    case "United States" | "USA":   # | matches multiple values in one case
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:                         # wildcard: fallback for anything else
        print("Unknown Country")
# Output: EG


# --- if/elif/else vs match/case ---
"""
┌─────────────────┬──────────────────────────────┬──────────────────────────────┐
│ Feature         │ if / elif / else              │ match / case                 │
├─────────────────┼──────────────────────────────┼──────────────────────────────┤
│ Best for        │ Flexible logic and ranges     │ Matching exact fixed values   │
│ Conditions      │ Any boolean expression        │ Exact value comparison only  │
│ Multiple values │ Use 'or' in condition         │ Use  |  inside a case        │
│ Fallback        │ else                          │ case _                       │
│ Python version  │ All versions                  │ Python 3.10+ only            │
└─────────────────┴──────────────────────────────┴──────────────────────────────┘
"""


# ============================================================================
# 3. CHALLENGE 1 - Email Validator
# ============================================================================
"""
================================================================================
CHALLENGE: Validate the quality and correctness of an email address

Validation Rules:
    - Must not be empty
    - Must contain '.' and '@'
    - Must contain exactly one '@' symbol
    - Must end with '.com', '.org', or '.net'
    - Must not be longer than 254 characters
    - Must start and end with a letter or digit
================================================================================
"""

email = "shehab@gmail.com"
valid = True

# Step 1: Clean the input
email = email.strip()

# Rule 1: Email must not be empty
if email == "":
    print("Email cannot be empty.")
    valid = False

# Rule 2: Email must contain both '.' and '@'
if not ('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False

# Rule 3: Email must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False

# Rule 4: Email must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")
    valid = False

# Rule 5: Email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
    valid = False

# Rule 6: Email must start and end with a letter or digit
if email != "" and not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False

# Final Result
if valid:
    print("Email is valid ✅")
else:
    print("Email is invalid ❌")
# Output: Email is valid ✅


# ============================================================================
# 4. CHALLENGE 2 - Password Validator
# ============================================================================
"""
================================================================================
CHALLENGE: Validate the quality and correctness of a password

Validation Rules:
    - Password must not be empty
    - Password must be at least 8 characters
    - Password must include at least 1 uppercase letter
    - Password must include at least 1 lowercase letter
    - Password must not be the same as the email
    - Password must not contain any spaces
    - Password must start and end with a letter or digit
================================================================================
"""

email    = "shehab@gmail.com"
password = "Shehab123"
valid    = True

# Step 1: Clean the input
password = password.strip()

# Rule 1: Password must not be empty
if password == "":
    print("Password cannot be empty.")
    valid = False

# Rule 2: Password must be at least 8 characters
if len(password) < 8:
    print("Password must be at least 8 characters.")
    valid = False

# Rule 3: Password must include at least 1 uppercase letter
if not any(char.isupper() for char in password):
    print("Password must include at least 1 uppercase letter.")
    valid = False

# Rule 4: Password must include at least 1 lowercase letter
if not any(char.islower() for char in password):
    print("Password must include at least 1 lowercase letter.")
    valid = False

# Rule 5: Password must not be the same as the email
if password == email:
    print("Password must not be the same as the email.")
    valid = False

# Rule 6: Password must not contain any spaces
if " " in password:
    print("Password must not contain any spaces.")
    valid = False

# Rule 7: Password must start and end with a letter or digit
if password != "" and not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit.")
    valid = False

# Final Result
if valid:
    print("Password is valid ✅")
else:
    print("Password is invalid ❌")
# Output: Password is valid ✅


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
CONDITIONAL STATEMENTS - COMPLETE PICTURE

────────────────────────────────────────────────────────────────────────────

  if                               elif                          else
  Starts the 1st condition         Adds a follow-up condition    "fallback"
                                   if the previous is false      if none of
                                                                 the conditions
                                                                 are met

────────────────────────────────────────────────────────────────────────────

Four Forms of Conditional Statements:

    1. Standalone if      → "Just Checking"
                            "If this is true, do this — otherwise, do nothing"

    2. if / else          → "This or That"
                            Two outcomes: True path or False path

    3. if / elif / else   → "Branching"
                            "Choose one from many" — stops at first True

    4. Independent ifs    → "Checklist Mode"
                            "Test all conditions" — every if always runs

────────────────────────────────────────────────────────────────────────────

Two Special Forms:

    Inline if (Ternary):
        do A  if  condition  else  do B
        • "Quick, short, simple check"
        • Use for simple two-outcome logic only

    Match / Case:
        match value:
            case option_1: ...
            case option_2: ...
            case _:        ...  (wildcard fallback)
        • "Pattern Matcher"
        • "Match one exact value to multiple options"
        • Requires Python 3.10+

────────────────────────────────────────────────────────────────────────────

When to Use What:

    ┌──────────────────────┬────────────────────────────────────────────┐
    │ Situation            │ Best Choice                                │
    ├──────────────────────┼────────────────────────────────────────────┤
    │ One optional action  │ Standalone if                              │
    │ Two outcomes         │ if / else  or  inline if                   │
    │ Many outcomes        │ if / elif / else                           │
    │ Exact value matching │ match / case                               │
    │ Unrelated checks     │ Independent if blocks                      │
    │ Quick one-liner      │ Inline if (ternary)                        │
    └──────────────────────┴────────────────────────────────────────────┘

Applying Conditionals - Real Validation Pattern:
    1. Strip the input
    2. Use independent ifs to check each rule separately
    3. Track validity with a bool flag (valid = True / False)
    4. Print specific messages for each failed rule
    5. Show a final verdict at the end
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How inline if (ternary) compresses if/else into one readable line
✓ How to chain inline ifs for three or more outcomes
✓ When to use inline if (simple) vs classical if (complex)
✓ How match/case works as a pattern matcher for exact values
✓ How to match multiple values in one case using the | operator
✓ The wildcard case _ as a fallback (equivalent to else)
✓ The difference between if/elif/else and match/case
✓ That match/case requires Python 3.10+
✓ How to build a real email validator using independent if checks
✓ How to build a real password validator with multiple rule checks
✓ The validation pattern: strip → check rules → track flag → report result
✓ How to use any() with a generator to check characters in a string
"""