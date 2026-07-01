"""
================================================================================
PYTHON NUMBERS - PART 2: ROUNDING, RANDOM, AND VALIDATION
================================================================================
Learning Focus: Mathematical functions, rounding methods, random numbers, and validation
"""


# ============================================================================
# NUMBER OPERATIONS OVERVIEW
# ============================================================================
"""
Quick Reference Table:

┌────────────┬────────────────┬───────────────┬────────────────┬──────────────────┬───────────────┐
│ Types      │ Math Operators │ Rounding      │ Advanced Math  │ Random           │ Validation    │
├────────────┼────────────────┼───────────────┼────────────────┼──────────────────┼───────────────┤
│ type()     │ 3 + 2          │ abs()         │ math.sqrt()    │ random.random()  │ is_integer()  │
│ int()      │ 3 - 2          │ round()       │ math.sin()     │ random.randint() │ isinstance()  │
│ float()    │ 3 * 2          │ math.ceil()   │ math.cos()     │                  │               │
│ complex()  │ 3 / 2          │ math.floor()  │ math.log()     │                  │               │
│            │ 3 // 2         │ math.trunc()  │                │                  │               │
│            │ 3 % 2          │               │                │                  │               │
│            │ 3 ** 2         │               │                │                  │               │
└────────────┴────────────────┴───────────────┴────────────────┴──────────────────┴───────────────┘
"""


# ============================================================================
# 1. ABSOLUTE VALUE - abs()
# ============================================================================

# --- abs() Function ---
# abs(value) → Returns the absolute (non-negative) value of a number

print(abs(-5))
# Output: 5

print(abs(5))
# Output: 5

# Use Case: Measure Distance
# Distance is always positive, regardless of direction
distance = abs(2 - 10)
print(distance)
# Output: 8

# Use Case: Calculate Difference
price_difference = abs(100 - 85)
print(f"Price difference: ${price_difference}")
# Output: Price difference: $15


# ============================================================================
# 2. WHY ROUNDING MATTERS
# ============================================================================
"""
⚠️ Sometimes numbers are messy!

Problem:
    Calculations often produce long decimal numbers like 35.54879865
    
Solution:
    We round them to make results easier to read and work with
    
When to use:
    - Financial calculations (show only 2 decimals)
    - Display values to users
    - Data analysis reports
    - Save storage space
"""


# ============================================================================
# 3. ROUNDING FUNCTIONS - COMPREHENSIVE GUIDE
# ============================================================================
"""
================================================================================
ROUNDING FUNCTIONS - QUICK REFERENCE
================================================================================

┌──────────────┬────────────────────────────┬───────────────────┬──────────────────────────────────────┐
│ Function     │ Description                │ Example Input     │ Output                               │
├──────────────┼────────────────────────────┼───────────────────┼──────────────────────────────────────┤
│ math.floor() │ Rounds DOWN to nearest int │ math.floor(1.7)   │ 1                                    │
│              │ (always to lower value)    │ math.floor(1.3)   │ 1                                    │
│              │                            │ math.floor(-1.3)  │ -2 (down means more negative)        │
├──────────────┼────────────────────────────┼───────────────────┼──────────────────────────────────────┤
│ math.ceil()  │ Rounds UP to nearest int   │ math.ceil(1.3)    │ 2                                    │
│              │ (always to higher value)   │ math.ceil(1.7)    │ 2                                    │
│              │                            │ math.ceil(-1.3)   │ -1 (up means less negative)          │
├──────────────┼────────────────────────────┼───────────────────┼──────────────────────────────────────┤
│ round()      │ Rounds to nearest integer  │ round(1.3)        │ 1                                    │
│              │ (based on closest value)   │ round(1.7)        │ 2                                    │
│              │                            │ round(1.5)        │ 2 (Python uses banker's rounding)    │
│              │                            │                   │   => rounds to nearest even number   │
├──────────────┼────────────────────────────┼───────────────────┼──────────────────────────────────────┤
│ math.trunc() │ Cuts off decimal part      │ math.trunc(1.7)   │ 1                                    │
│              │ (no rounding, just chop)   │ math.trunc(-1.7)  │ -1 (toward zero)                     │
└──────────────┴────────────────────────────┴───────────────────┴──────────────────────────────────────┘

🧠 Quick Visual Guide:
    floor → Always DOWN (↓)
    ceil  → Always UP (↑)
    round → Nearest value (↕)
    trunc → Chop decimals (✂️)
"""


# ============================================================================
# 4. ROUNDING WITH round()
# ============================================================================

import math

price = 35.54879865

# --- round() Function ---
# round(number, ndigits) → Rounds to specified decimal places

# Round to nearest integer (no decimals)
print(round(price))
# Output: 36

# Round to 2 decimal places (common for money)
print(round(price, 2))
# Output: 35.55

# Round to 1 decimal place
print(round(price, 1))
# Output: 35.5

# Use Case: Display prices in reports or invoices
final_price = round(price, 2)
print(f"Price: ${final_price}")
# Output: Price: $35.55


# ============================================================================
# 5. ROUNDING DOWN WITH math.floor()
# ============================================================================

# --- math.floor() Function ---
# math.floor(x) → Always rounds DOWN to nearest integer

# IMPORTANT: floor() is NOT a built-in function
# It belongs to the math module - import it before using

price = 35.54879865

print(math.floor(price))
# Output: 35

# Works with negative numbers (rounds to more negative)
print(math.floor(-1.3))
# Output: -2

print(math.floor(-1.9))
# Output: -2


# ============================================================================
# 6. ROUNDING UP WITH math.ceil()
# ============================================================================

# --- math.ceil() Function ---
# math.ceil(x) → Always rounds UP to nearest integer

print(math.ceil(price))
# Output: 36

# Use Case: Data Engineering - Split Data into Pages
# Example: 100 records, 30 per page → need 4 pages (not 3.33)
total_records = 100
records_per_page = 30
pages_needed = math.ceil(total_records / records_per_page)
print(f"Pages needed: {pages_needed}")
# Output: Pages needed: 4

# Works with negative numbers (rounds to less negative)
print(math.ceil(-1.3))
# Output: -1

print(math.ceil(-1.9))
# Output: -1


# ============================================================================
# 7. TRUNCATING WITH math.trunc()
# ============================================================================

# --- math.trunc() Function ---
# math.trunc(x) → Cuts off decimal part, keeps whole number (no rounding)

price = 35.54879865

print(math.trunc(price))
# Output: 35

# Difference with negative numbers:
print(math.trunc(-1.7))
# Output: -1 (just removes decimal)

print(math.floor(-1.7))
# Output: -2 (rounds down)


# ============================================================================
# 8. COMPARISON - int() vs trunc()
# ============================================================================

price = 35.54879865

# Both remove decimal part for positive numbers
print(int(price))
# Output: 35

print(math.trunc(price))
# Output: 35

# Key Difference: Behavior with negative numbers
negative = -35.9

print(int(negative))
# Output: -35 (truncates toward zero)

print(math.trunc(negative))
# Output: -35 (truncates toward zero)

print(math.floor(negative))
# Output: -36 (rounds down)

# Conclusion: int() and trunc() behave the same way (truncate toward zero)


# ============================================================================
# 9. RANDOM NUMBERS - random.random()
# ============================================================================

import random

# --- random.random() Function ---
# random.random() → Returns random float between 0.0 and 1.0

print(random.random())
# Output: 0.4738562... (changes every time)

# Use Case: Generate random probability
probability = random.random()
if probability > 0.5:
    print("Heads")
else:
    print("Tails")


# ============================================================================
# 10. RANDOM INTEGERS - random.randint()
# ============================================================================

# --- random.randint() Function ---
# random.randint(start, end) → Returns random integer from start to end (both included)

# Simulate rolling a dice (1 to 6)
dice_roll = random.randint(1, 6)
print(dice_roll)
# Output: 3 (random between 1 and 6)

# Use Case: Generate random player ID
player_id = random.randint(1000, 9999)
print(f"Player ID: {player_id}")
# Output: Player ID: 5847 (random 4-digit number)

# Use Case: Random age for testing
test_age = random.randint(18, 65)
print(f"Test age: {test_age}")
# Output: Test age: 42 (random age between 18 and 65)


# ============================================================================
# 11. VALIDATION - is_integer()
# ============================================================================

# --- is_integer() Method ---
# float.is_integer() → Checks if a float has no decimal part (is a whole number)

x = 7.0
print(x.is_integer())
# Output: True (7.0 is a whole number)

y = 7.1
print(y.is_integer())
# Output: False (7.1 has decimal part)

# Use Case: Validate division result
result = 10 / 2
if result.is_integer():
    print(f"{result} is a whole number")
else:
    print(f"{result} has decimals")
# Output: 5.0 is a whole number


# ============================================================================
# 12. VALIDATION - isinstance()
# ============================================================================

# --- isinstance() Function ---
# isinstance(value, type) → Checks if a value belongs to a certain data type

x = 70.4

# Check if x is an integer
print(isinstance(x, int))
# Output: False

# Check if x is a float
print(isinstance(x, float))
# Output: True

# Use Case: Validate user input type
age = 25
if isinstance(age, int):
    print("Age is valid (integer)")
else:
    print("Age must be a whole number")
# Output: Age is valid (integer)

# Check multiple types
value = 3.14
if isinstance(value, (int, float)):
    print("Value is a number")
# Output: Value is a number


# ============================================================================
# 13. PYTHON CHALLENGE - Random Even/Odd Checker
# ============================================================================
"""
Challenge: Generate a random integer and check if it's even

Requirements:
1. Generate random number between 1 and 100
2. Display the number
3. Check if it's even or odd
4. Print the result
"""

# Solution:
import random

# Generate a random integer between 1 and 100
number = random.randint(1, 100)
print("Random Number:", number)
# Output: Random Number: 47 (example)

# Check if the number is even using modulo operator
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
# Output: The number is odd


# ============================================================================
# 14. PRACTICAL EXAMPLES - Combining Concepts
# ============================================================================

# Example 1: Round prices for display
import math
import random

prices = [19.99876, 25.12345, 99.99999]
rounded_prices = [round(p, 2) for p in prices]
print(f"Prices: {rounded_prices}")
# Output: Prices: [20.0, 25.12, 100.0]


# Example 2: Calculate pages needed for pagination
total_items = 157
items_per_page = 25
total_pages = math.ceil(total_items / items_per_page)
print(f"Total pages: {total_pages}")
# Output: Total pages: 7


# Example 3: Generate random discount
discount = random.randint(10, 50)
price = 100
final = price - (price * discount / 100)
print(f"Original: ${price}, Discount: {discount}%, Final: ${round(final, 2)}")
# Output: Original: $100, Discount: 23%, Final: $77.0


# Example 4: Validate calculation result
result = 100 / 3
if result.is_integer():
    print(int(result))
else:
    print(round(result, 2))
# Output: 33.33


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
ROUNDING, RANDOM & VALIDATION - ESSENTIAL FACTS

Absolute Value:
    • abs(x)           → Always positive value

Rounding Functions:
    • round(x, n)      → Round to n decimal places (nearest value)
    • math.floor(x)    → Always round DOWN (↓)
    • math.ceil(x)     → Always round UP (↑)
    • math.trunc(x)    → Cut off decimals (no rounding)
    • int(x)           → Same as trunc() for numbers

Random Numbers:
    • random.random()       → Float between 0.0 and 1.0
    • random.randint(a, b)  → Integer from a to b (inclusive)

Validation:
    • .is_integer()     → Check if float is whole number
    • isinstance(x, t)  → Check if x is type t

Important Notes:
    • floor() and ceil() need: import math
    • random functions need: import random
    • round() uses banker's rounding (rounds .5 to nearest even)
    • int() and trunc() behave identically
    • floor() rounds to MORE negative, ceil() to LESS negative
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use abs() to get absolute values for distance calculations
✓ Why rounding is important (readability, storage, display)
✓ Four different rounding methods: round(), floor(), ceil(), trunc()
✓ That floor() always rounds DOWN (more negative)
✓ That ceil() always rounds UP (less negative)
✓ That trunc() just chops off decimals without rounding
✓ The difference between int() and trunc() (they're the same)
✓ How to generate random floats with random.random()
✓ How to generate random integers with random.randint()
✓ How to validate if a float is a whole number with is_integer()
✓ How to check data types with isinstance()
✓ Real-world use cases: pagination, pricing, discounts, validation
✓ That both math and random modules need to be imported
"""