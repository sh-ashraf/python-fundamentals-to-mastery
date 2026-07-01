"""
================================================================================
PYTHON NUMBERS - PART 1: TYPES AND OPERATIONS
================================================================================
Learning Focus: Number types, type conversion, and mathematical operators
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
# 1. NUMBER TYPES IN PYTHON
# ============================================================================

# Python has three main numeric types:

# --- Integer (int) ---
# Whole numbers without decimal points
x = 5
print(type(x))
# Output: <class 'int'>

# --- Float (float) ---
# Numbers with decimal points
y = 5.7
print(type(y))
# Output: <class 'float'>

# --- Complex (complex) ---
# Numbers with real and imaginary parts (a + bj)
z = 2 + 3j
print(type(z))
# Output: <class 'complex'>


# ============================================================================
# 2. COMMON MISTAKE - Numbers as Strings
# ============================================================================

# PROBLEM: Numbers in quotes are strings, not numbers!
x = "24"  # "24" is a string, not a number
print(type(x))
# Output: <class 'str'>

# What happens when you try math with a string?
print(x * 3)
# Output: 242424
# Python repeats the text instead of doing math!


# ============================================================================
# 3. TYPE CONVERSION - String to Integer
# ============================================================================

# --- int() Function ---
# int(value) → Converts compatible value to integer

x = "24"
print(type(x))
# Output: <class 'str'>

# Convert string to integer
x = int(x)
print(type(x))
# Output: <class 'int'>

# Now math works correctly
print(x * 3)
# Output: 72


# ============================================================================
# 4. TYPE CONVERSION - String to Float
# ============================================================================

# --- float() Function ---
# float(value) → Converts compatible value to float

x = "3"
print(float(x))
# Output: 3.0

# Convert integer to float
x = 5
print(float(x))
# Output: 5.0

# Use case: When you need decimal precision
price = "19"
price_with_tax = float(price) * 1.15
print(price_with_tax)
# Output: 21.85


# ============================================================================
# 5. TYPE CONVERSION - Creating Complex Numbers
# ============================================================================

# --- complex() Function ---
# complex(real, imag) → Creates a complex number

x = 3   # Real part
y = 4   # Imaginary part
result = complex(x, y)
print(result)
# Output: (3+4j)

# Direct creation
z = 2 + 5j
print(type(z))
# Output: <class 'complex'>


# ============================================================================
# 6. ARITHMETIC OPERATORS
# ============================================================================

x = 10
y = 5

# --- Addition (+) ---
print(x + y)
# Output: 15

# --- Subtraction (-) ---
print(x - y)
# Output: 5

# --- Multiplication (*) ---
print(x * y)
# Output: 50

# --- Division (/) ---
# Always returns a float, even if result is whole number
print(x / y)
# Output: 2.0

# --- Floor Division (//) ---
# Divides and rounds DOWN to nearest integer
print(x // y)
# Output: 2

# Example: Floor division with decimal result
print(7 // 2)
# Output: 3 (not 3.5)

# --- Modulo (%) ---
# Returns the remainder after division
print(x % y)
# Output: 0

# Example: Check if number is even or odd
print(7 % 2)
# Output: 1 (odd number)

print(8 % 2)
# Output: 0 (even number)

# --- Exponentiation (**) ---
# Raises number to a power
print(x ** y)
# Output: 100000 (10 to the power of 5)

# Example: Calculate square
print(5 ** 2)
# Output: 25


# ============================================================================
# 7. SHORTHAND ASSIGNMENT OPERATORS
# ============================================================================

# Instead of: x = x + 3
# Use: x += 3

# --- Addition Assignment (+=) ---
x = 2
x = x + 3
print(x)
# Output: 5

# Shorthand version
x = 2
x += 3
print(x)
# Output: 5


# --- Subtraction Assignment (-=) ---
x = 5
x -= 1
print(x)
# Output: 4


# --- Multiplication Assignment (*=) ---
x = 4
x *= 2
print(x)
# Output: 8

# Long form equivalent
x = 4
x = x * 2
print(x)
# Output: 8


# --- Other Shorthand Operators ---
# All arithmetic operators have shorthand versions:

x = 10
x /= 2   # x = x / 2
print(x)
# Output: 5.0

x = 10
x //= 3  # x = x // 3
print(x)
# Output: 3

x = 10
x %= 3   # x = x % 3
print(x)
# Output: 1

x = 2
x **= 3  # x = x ** 3
print(x)
# Output: 8


# ============================================================================
# 8. ORDER OF OPERATIONS (PEMDAS)
# ============================================================================

# Python follows standard mathematical order:
# 1. Parentheses ()
# 2. Exponents **
# 3. Multiplication/Division *, /, //, %
# 4. Addition/Subtraction +, -

result = 2 + 3 * 4
print(result)
# Output: 14 (not 20)
# Multiplication happens first: 3 * 4 = 12, then 2 + 12 = 14

# Use parentheses to change order
result = (2 + 3) * 4
print(result)
# Output: 20
# Parentheses first: 2 + 3 = 5, then 5 * 4 = 20


# ============================================================================
# 9. PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Calculate area of rectangle
width = 5.5
height = 3.2
area = width * height
print(f"Area: {area}")
# Output: Area: 17.6


# Example 2: Convert temperature (Celsius to Fahrenheit)
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
# Output: 25°C = 77.0°F


# Example 3: Calculate discount
price = 100
discount_percent = 20
discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount
print(f"Final price: ${final_price}")
# Output: Final price: $80.0


# Example 4: Check if number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
# Output: 7 is odd


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
NUMBER TYPES & OPERATIONS - ESSENTIAL FACTS

Number Types:
    • int       → Whole numbers (5, -3, 0)
    • float     → Decimal numbers (3.14, -0.5)
    • complex   → Complex numbers (3+4j)

Type Conversion:
    • int(x)      → Convert to integer
    • float(x)    → Convert to float
    • complex(r,i) → Create complex number

Arithmetic Operators:
    • +     → Addition
    • -     → Subtraction
    • *     → Multiplication
    • /     → Division (always returns float)
    • //    → Floor division (rounds down)
    • %     → Modulo (remainder)
    • **    → Exponentiation (power)

Shorthand Operators:
    • +=    → Add and assign
    • -=    → Subtract and assign
    • *=    → Multiply and assign
    • /=    → Divide and assign
    • //=   → Floor divide and assign
    • %=    → Modulo and assign
    • **=   → Exponent and assign

Important Notes:
    • Division (/) ALWAYS returns float, even if result is whole number
    • Floor division (//) always rounds DOWN
    • String numbers ("24") need int() or float() for math
    • Use % to check even/odd: even if x % 2 == 0
    • Follow PEMDAS order of operations
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ The three main number types in Python: int, float, complex
✓ How to check number types with type()
✓ How to convert between types using int(), float(), and complex()
✓ That string numbers need conversion before math operations
✓ All seven arithmetic operators: +, -, *, /, //, %, **
✓ The difference between / (regular division) and // (floor division)
✓ How to use modulo (%) to find remainders and check even/odd
✓ Shorthand assignment operators (+=, -=, *=, etc.)
✓ Order of operations (PEMDAS) in Python
✓ Practical applications: area calculation, temperature conversion, discounts
✓ That division always returns a float, even for whole numbers
"""