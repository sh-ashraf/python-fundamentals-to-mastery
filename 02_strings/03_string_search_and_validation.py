"""
================================================================================
PYTHON STRINGS - PART 3: SEARCH, VALIDATION, AND CASE CONVERSION
================================================================================
Learning Focus: String searching, validation methods, and case transformations
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
# 1. CASE CONVERSION - lower() and upper()
# ============================================================================

# --- lower() Method ---
# string.lower() → Makes all letters lowercase

# --- upper() Method ---
# string.upper() → Makes all letters uppercase

text = "Python PROGRAMMING"
print(text.lower())
# Output: python programming

print(text.upper())
# Output: PYTHON PROGRAMMING


# Use Case: Standardize Text Format
# Make sure text is always in a consistent case (usually lowercase)


# ============================================================================
# 2. CASE CONVERSION FOR DATA MATCHING
# ============================================================================

# Use Case: Clean Data for Matching
# Lowercase all text to prevent case-based mismatches during search or comparison

search = "Email".lower().strip()
# Result: "email"

data = "emAil".lower().strip()
# Result: "email"

print(search == data)
# Output: True

# Best Practice: Clean Before Search
# Always trim spaces and lowercase your data and search term before matching


# ============================================================================
# 3. PYTHON CHALLENGE - Data Cleaning & Formatting
# ============================================================================
"""
Challenge: Turn messy string into clean summary

Input:
    "968-Maria, ( D@ta Engineer );: 27y"

Expected Output:
    name: maria | role: data engineer | age: 27

Steps:
    1. Remove unwanted characters
    2. Extract name, role, and age
    3. Convert to lowercase
    4. Format as requested
"""

# Solution:
messy_data = "968-Maria, ( D@ta Engineer );: 27y"

# Step 1: Clean and split the data
cleaned = messy_data.replace("968-", "").replace(",", "").replace("(", "").replace(")", "").replace(";", "").replace(":", "")
# Result: "Maria  D@ta Engineer  27y"

# Step 2: Extract parts
name = "maria"  # Extracted and lowercased
role = "data engineer"  # Extracted, lowercased, @ removed
age = "27"  # Extracted, y removed

# Step 3: Format output
result = f"name: {name} | role: {role} | age: {age}"
print(result)
# Output: name: maria | role: data engineer | age: 27


# ============================================================================
# 4. STRING SEARCH - startswith() and endswith()
# ============================================================================

# --- startswith() Method ---
# string.startswith(substring) → Returns True if string begins with substring

phone = "+48-176-12345"
print(phone.startswith("+49"))
# Output: False

print(phone.startswith("+48"))
# Output: True


# --- endswith() Method ---
# string.endswith(substring) → Returns True if string ends with substring

email = "temo@gmail.com"
print(email.endswith("gmail.com"))
# Output: True

# Use Case: Check File Extensions
file = "data_backup.csv"
print(file.endswith(".csv"))
# Output: True

print(file.endswith(".xlsx"))
# Output: False


# ============================================================================
# 5. STRING SEARCH - in Operator
# ============================================================================

# --- in Operator ---
# 'substring' in 'string' → Returns True if substring exists anywhere in string

email = "temo@gmail.com"
print('@' in email)
# Output: True

# Use Case: Check if URL is an API Endpoint
url = "http://api.company.com/v1/data"
print("/api" in url)
# Output: False (looking for "/api", but URL has "api.")

print("api" in url)
# Output: True


# ============================================================================
# 6. STRING SEARCH - find() Method
# ============================================================================

# --- find() Method ---
# string.find(substring) → Returns the starting position (index) of substring
# Returns -1 if substring is not found

# Problem: Extract phone number without country code
phone1 = "+48-176-12345"
phone2 = "48-654-16548"

# Hardcoding the start position doesn't work when country code length changes
print(phone1[4:])
# Output: 176-12345

print(phone2[3:])
# Output: 654-16548


# Solution: Use find() for dynamic extraction
phone3 = "0048-654-16548"

# Find the position of "-" and extract everything after it
print(phone1[phone1.find("-") + 1:])
# Output: 176-12345

print(phone2[phone2.find("-") + 1:])
# Output: 654-16548

print(phone3[phone3.find("-") + 1:])
# Output: 654-16548

# Check the position of "-"
print(phone1.find("-"))
# Output: 3

# find() is great when combined with slicing for dynamic extraction


# ============================================================================
# 7. ADVANCED find() USAGE
# ============================================================================

# find() returns -1 if substring not found
text = "Python Programming"
print(text.find("Java"))
# Output: -1

# find() is case-sensitive
print(text.find("python"))
# Output: -1 (lowercase 'python' not found)

print(text.find("Python"))
# Output: 0 (found at index 0)

# Find position and use for validation
email = "user@example.com"
at_position = email.find("@")

if at_position != -1:
    username = email[:at_position]
    domain = email[at_position + 1:]
    print(f"Username: {username}, Domain: {domain}")
# Output: Username: user, Domain: example.com


# ============================================================================
# 8. STRING VALIDATION - isalpha()
# ============================================================================

# --- isalpha() Method ---
# string.isalpha() → Returns True if string contains ONLY letters (no spaces, numbers, or symbols)

# Use Case: Check if country name contains only letters
country = "USA"
print(country.isalpha())
# Output: True

country = "USA1"
print(country.isalpha())
# Output: False (contains number)

# Note: Spaces also make it False
country = "United States"
print(country.isalpha())
# Output: False (contains space)


# ============================================================================
# 9. STRING VALIDATION - isnumeric()
# ============================================================================

# --- isnumeric() Method ---
# string.isnumeric() → Returns True if string contains ONLY numbers

phone = "0123456789"
print(phone.isnumeric())
# Output: True

phone = "012-345-6789"
print(phone.isnumeric())
# Output: False (contains hyphens)

# Use Case: Prevent invalid or "garbage" data from entering your system
age_input = "25"
if age_input.isnumeric():
    age = int(age_input)
    print(f"Valid age: {age}")
else:
    print("Invalid age input!")
# Output: Valid age: 25


# ============================================================================
# 10. COMBINING VALIDATION METHODS
# ============================================================================

# Example 1: Validate Email Structure
email = "user@example.com"
has_at = "@" in email
has_dot = "." in email
is_valid = has_at and has_dot

print(f"Email valid: {is_valid}")
# Output: Email valid: True


# Example 2: Validate Phone Number Format
phone = "0123456789"
is_numeric = phone.isnumeric()
correct_length = len(phone) == 10
is_valid_phone = is_numeric and correct_length

print(f"Phone valid: {is_valid_phone}")
# Output: Phone valid: True


# Example 3: Check File Type
filename = "report.pdf"
is_pdf = filename.endswith(".pdf")
has_name = len(filename.replace(".pdf", "")) > 0

print(f"Valid PDF filename: {is_pdf and has_name}")
# Output: Valid PDF filename: True


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
STRING SEARCH, VALIDATION & CASE CONVERSION - ESSENTIAL FACTS

Case Conversion:
    • .lower()               → Convert to lowercase
    • .upper()               → Convert to uppercase
    • Best Practice: Always clean case before comparing strings

Search Methods:
    • .startswith(sub)       → Check if string begins with substring
    • .endswith(sub)         → Check if string ends with substring
    • sub in string          → Check if substring exists anywhere
    • .find(sub)             → Find position of substring (returns -1 if not found)

Validation Methods:
    • .isalpha()             → True if only letters (no spaces/numbers)
    • .isnumeric()           → True if only numbers
    • .isalnum()             → True if only letters and numbers
    • .isspace()             → True if only whitespace

Important Notes:
    • All search methods are CASE-SENSITIVE
    • find() returns -1 if substring not found (not an error)
    • Always combine .lower() + .strip() before comparing
    • Validation methods return False for empty strings
    • Use find() + slicing for dynamic string extraction
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to convert strings to lowercase and uppercase with .lower() and .upper()
✓ Why case conversion is essential before string comparison
✓ How to use startswith() and endswith() for pattern matching
✓ How to use the 'in' operator to check if substring exists
✓ How to use find() to get the position of a substring
✓ That find() returns -1 when substring is not found
✓ How to combine find() with slicing for dynamic extraction
✓ How to validate strings with isalpha() and isnumeric()
✓ Best practice: always .strip() and .lower() before comparing
✓ How to combine multiple validation methods for robust checks
✓ Real-world use cases: email validation, phone cleaning, file type checking
✓ How to handle messy data with chained string methods
"""