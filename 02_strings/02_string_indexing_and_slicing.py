"""
================================================================================
PYTHON STRINGS - PART 2: INDEXING, SLICING, AND CLEANING
================================================================================
Learning Focus: String extraction, indexing, slicing, and whitespace cleaning
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
# 1. STRING INDEXING - Accessing Individual Characters
# ============================================================================

# --- Indexing Syntax ---
# string[index] → Extracts one character by position

text = "python"

# Positive Indexing (starts from 0)
#   p  y  t  h  o  n
#   0  1  2  3  4  5

# Negative Indexing (starts from -1 at the end)
#   p   y   t   h   o   n
#  -6  -5  -4  -3  -2  -1


# --- Extract First Character ---
print(text[0])
# Output: p

print(text[-6])
# Output: p


# --- Extract Last Character ---
print(text[5])
# Output: n

print(text[-1])
# Output: n


# --- Extract Middle Character (h) ---
print(text[3])
# Output: h

print(text[-3])
# Output: h


# ============================================================================
# 2. STRING SLICING - Extracting Substrings
# ============================================================================

# --- Slicing Syntax ---
# string[start:end:step] → Extracts a portion of the string
#
# Parameters:
#   start - Starting index (inclusive)
#   end   - Ending index (exclusive)
#   step  - Step/increment (default: 1)

date = "2026-09-20"
#       0123456789  (index positions)


# --- Extract the Year (2026) ---
print(date[0:4])
# Output: 2026
# Starts at index 0, stops before index 4

# If you leave start empty, Python starts from index 0
print(date[:4])
# Output: 2026


# --- Extract the Month (09) ---
print(date[5:7])
# Output: 09
# Starts at index 5, stops before index 7


# --- Extract the Day (20) ---
print(date[8:11])
# Output: 20

# If you leave end empty, Python goes to the end
print(date[8:])
# Output: 20


# ============================================================================
# 3. ADVANCED SLICING PATTERNS
# ============================================================================

text = "Python Programming"

# Extract first 6 characters
print(text[:6])
# Output: Python

# Extract last 11 characters
print(text[-11:])
# Output: Programming

# Extract middle portion
print(text[7:18])
# Output: Programming

# Reverse a string using negative step
print(text[::-1])
# Output: gnimmargorP nohtyP

# Extract every second character
print(text[::2])
# Output: Pto rgamn


# ============================================================================
# 4. DATA CLEANING - Remove Whitespace
# ============================================================================

# --- lstrip() Method ---
# string.lstrip() → Removes spaces from the LEFT side

text = "     Engineering"
cleaned = text.lstrip()
print(cleaned)
# Output: Engineering


# --- rstrip() Method ---
# string.rstrip() → Removes spaces from the RIGHT side

text = "Engineering     "
cleaned = text.rstrip()
print(cleaned)
# Output: Engineering


# --- strip() Method ---
# string.strip() → Removes spaces from BOTH ends

text = "     Engineering     "
cleaned = text.strip()
print(cleaned)
# Output: Engineering


# ============================================================================
# 5. IMPORTANT NOTES ABOUT strip()
# ============================================================================

# Best Practice: Always strip user input
# Use .strip() to remove unexpected extra spaces from both ends

# NOTE 1: Only removes spaces at start/end, NOT in the middle
text = "Data    Engineering"
cleaned = text.strip()
print(cleaned)
# Output: Data    Engineering
# (spaces in the middle are preserved)


# NOTE 2: Can remove specific characters, not just spaces
text = "###ABC####"
cleaned = text.strip("#")
print(cleaned)
# Output: ABC


# ============================================================================
# 6. USE CASE - Detect and Count Extra Spaces
# ============================================================================

# Check length before and after strip() to find unwanted spaces

text = "    Engineering"

# Check original length
print(len(text))
# Output: 15

# Check cleaned length
print(len(text.strip()))
# Output: 11

# Calculate number of extra spaces
nr_of_spaces = len(text) - len(text.strip())
print("Nr of Spaces:", nr_of_spaces)
# Output: Nr of Spaces: 4

# Check if data is clean (no extra spaces)
is_clean = len(text) == len(text.strip())
print("Is my data clean?", is_clean)
# Output: Is my data clean? False


# ============================================================================
# 7. PRACTICAL EXAMPLES - Combining Indexing & Cleaning
# ============================================================================

# Example 1: Clean and extract from user input
user_input = "  john.doe@email.com  "
cleaned_email = user_input.strip()
username = cleaned_email[:8]  # Extract "john.doe"
print(username)
# Output: john.doe


# Example 2: Extract and validate phone number
phone = "  +20-123-456-7890  "
cleaned_phone = phone.strip()
country_code = cleaned_phone[1:3]  # Extract country code
print(country_code)
# Output: 20


# Example 3: Clean CSV data
csv_row = "  Alice  ,  30  ,  Cairo  "
# Split and clean each part
parts = [part.strip() for part in csv_row.split(",")]
print(parts)
# Output: ['Alice', '30', 'Cairo']


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
STRING INDEXING & SLICING - ESSENTIAL FACTS

Indexing:
    • string[index]        → Get single character
    • Positive: 0, 1, 2... → Start from left
    • Negative: -1, -2...  → Start from right

Slicing:
    • string[start:end]    → Extract substring
    • string[:end]         → From beginning to end
    • string[start:]       → From start to end
    • string[::step]       → With step increment
    • string[::-1]         → Reverse string

Whitespace Cleaning:
    • .lstrip()            → Remove left spaces
    • .rstrip()            → Remove right spaces
    • .strip()             → Remove both sides
    • .strip(chars)        → Remove specific characters

Important Notes:
    • Slicing end index is EXCLUSIVE (not included)
    • strip() doesn't affect middle spaces
    • Always strip() user input for clean data
    • Use len() before/after strip() to detect issues
    • String indexing starts at 0, not 1
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to access individual characters using positive and negative indexing
✓ How to extract substrings using slicing syntax [start:end:step]
✓ The difference between lstrip(), rstrip(), and strip()
✓ That slicing end index is exclusive (not included in result)
✓ How to reverse strings using [::-1]
✓ How to extract every nth character using step
✓ Best practice: always strip() user input to remove unwanted spaces
✓ How to detect extra whitespace by comparing lengths
✓ That strip() can remove custom characters, not just spaces
✓ How to combine slicing and cleaning for data processing
✓ Practical use cases: email extraction, phone validation, CSV cleaning
"""
