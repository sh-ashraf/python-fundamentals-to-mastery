# Chapter 3 — Python Numbers

<p align="center">
  <strong>Master numeric types, arithmetic operations, mathematical functions, and number validation in Python.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-03-orange" alt="Chapter 03">
  <img src="https://img.shields.io/badge/Focus-Numbers-purple" alt="Focus: Numbers">
</p>

---

## 📌 Chapter Overview

This chapter covers how Python handles numeric data. Numbers are the foundation of every calculation, every measurement, and every data-driven decision a program makes. Understanding how Python classifies, converts, and operates on numbers is essential before moving into logic and conditional statements.

The chapter moves from numeric types and type conversion, through arithmetic and shorthand operators, to rounding functions, random number generation, and numeric validation. Each lesson builds on the previous one, and together they give the learner the ability to perform accurate calculations, format results cleanly, and validate numeric input reliably.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Identify the three Python numeric types: `int`, `float`, and `complex`.
- Convert between numeric types using `int()`, `float()`, and `complex()`.
- Explain why string numbers must be converted before arithmetic.
- Use all seven arithmetic operators correctly.
- Understand the difference between regular division and floor division.
- Use modulo to check remainders and even/odd status.
- Apply shorthand assignment operators: `+=`, `-=`, `*=`, and others.
- Follow the correct order of operations using PEMDAS.
- Use `abs()` for absolute value and distance calculations.
- Round numbers using `round()`, `math.floor()`, `math.ceil()`, and `math.trunc()`.
- Generate random floats and integers using the `random` module.
- Validate numeric values using `is_integer()` and `isinstance()`.
- Apply numeric operations to real-world problems: pricing, pagination, temperature conversion.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners who have completed Chapters 1 and 2 and are ready to work with numbers |
| Data learners | Learners preparing for data analysis, financial calculations, and statistical processing |
| Programming beginners | Learners who want to understand how Python handles and validates numeric data |
| Review learners | Learners who want a structured refresher on Python numeric operations |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Create and use variables.
- Use `print()` and f-strings.
- Understand Python data types and use `type()`.
- Convert values using `int()`, `float()`, and `str()`.
- Complete Chapters 1 and 2 of this series.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from understanding what kinds of numbers Python works with, to performing operations on them, to applying mathematical functions and validating results.

```text
Number Types (int, float, complex)
            ↓
Type Conversion (int(), float(), str())
            ↓
Arithmetic Operators (+, -, *, /, //, %, **)
            ↓
Shorthand Assignment Operators (+=, -=, *=, ...)
            ↓
Order of Operations (PEMDAS)
            ↓
Absolute Value (abs())
            ↓
Rounding Functions (round, floor, ceil, trunc)
            ↓
Random Numbers (random.random, random.randint)
            ↓
Number Validation (is_integer, isinstance)
```

This sequence is intentional:

1. The learner first understands what numeric types exist and how to convert between them.
2. Then the learner performs arithmetic and learns how each operator behaves.
3. Then the learner applies mathematical functions for rounding and precision.
4. Finally, the learner generates and validates numeric values for practical use.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_number_types_and_operations.py` | Types, Conversion, Arithmetic | `int`, `float`, `complex`, type conversion, all arithmetic operators, PEMDAS, shorthand operators |
| 02 | `02_math_functions_and_validation.py` | Rounding, Random, Validation | `abs()`, `round()`, `math.floor()`, `math.ceil()`, `math.trunc()`, `random`, `is_integer()`, `isinstance()` |

---

## 🧭 Recommended Study Order

### 1. Start with Number Types and Operations

**File:** `01_number_types_and_operations.py`

Start here because understanding what a number is in Python, and what operations can be performed on it, is the foundation for everything else in this chapter. Without knowing the difference between `/` and `//`, or why `"25" + 5` fails, the learner cannot use rounding or validation functions correctly.

The learner studies:

- `int`, `float`, and `complex` as the three numeric types
- Why string numbers fail in arithmetic and how to fix them
- `int()`, `float()`, and `complex()` for type conversion
- All seven arithmetic operators
- The difference between `/` (float result) and `//` (integer result)
- Modulo `%` for remainders and even/odd checks
- Exponentiation `**` for powers
- Shorthand operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- PEMDAS and how parentheses change results

---

### 2. Move to Math Functions and Validation

**File:** `02_math_functions_and_validation.py`

After mastering arithmetic, the learner is ready for mathematical functions that go beyond basic operators. This file introduces the `math` and `random` modules and teaches validation methods for verifying numeric types and values.

The learner studies:

- `abs()` for non-negative distance values
- Why rounding matters in real programs
- `round(x, n)` for rounding to n decimal places
- `math.floor()` for always rounding down
- `math.ceil()` for always rounding up
- `math.trunc()` for removing decimal parts without rounding
- The difference between `int()` and `math.trunc()`
- `random.random()` for random floats between 0 and 1
- `random.randint(a, b)` for random integers in a range
- `is_integer()` for checking if a float has no decimal part
- `isinstance()` for type-safe numeric validation

---

## 🧱 Lesson Breakdown

### Lesson 1 — Number Types and Operations

**File:** `01_number_types_and_operations.py`

This lesson establishes what numbers are in Python and how to work with them mathematically. It covers the full set of arithmetic operators and explains the rules that govern how Python evaluates expressions.

#### Key Concepts

- `int`: whole numbers without decimal points
- `float`: numbers with decimal points
- `complex`: numbers with real and imaginary parts (`3+4j`)
- String numbers (`"24"`) cannot be used in arithmetic without conversion
- `int(x)` converts to integer, `float(x)` converts to float
- `/` always returns a float, even when the result is whole
- `//` performs floor division and always returns an integer
- `%` returns the remainder (useful for even/odd checks)
- `**` raises to a power
- `and` has higher precedence than `or` — use parentheses when combining
- Shorthand operators reduce repetition: `x += 1` instead of `x = x + 1`
- PEMDAS governs evaluation order

#### Example

```python
# Type identification
x = 5
y = 5.7
print(type(x))   # <class 'int'>
print(type(y))   # <class 'float'>

# String number fails
age = "24"
print(age * 3)   # Output: 242424 (repetition, not math)
age = int(age)
print(age * 3)   # Output: 72 (now it is math)

# Division types
print(10 / 3)    # Output: 3.3333...  (always float)
print(10 // 3)   # Output: 3          (floor division)
print(10 % 3)    # Output: 1          (remainder)
print(2 ** 8)    # Output: 256        (power)

# PEMDAS
print(2 + 3 * 4)       # Output: 14 (multiplication first)
print((2 + 3) * 4)     # Output: 20 (parentheses first)

# Shorthand
x = 10
x += 5
print(x)         # Output: 15
```

#### Why This Lesson Matters

Every program that performs calculations, applies discounts, converts units, or processes data depends on arithmetic operators. Understanding the difference between `/` and `//` prevents precision errors. Understanding modulo enables even/odd checks and pagination logic. These are foundational skills for data engineering and any numeric programming.

---

### Lesson 2 — Math Functions and Validation

**File:** `02_math_functions_and_validation.py`

This lesson extends numeric capability beyond basic operators. The learner discovers how to control precision through rounding, introduce randomness for testing and simulation, and verify that a value is the correct numeric type before using it.

#### Key Concepts

- `abs(x)` returns the non-negative absolute value
- Rounding eliminates unnecessary decimal noise in results
- `round(x, n)` rounds to n decimal places using banker's rounding at `.5`
- `math.floor(x)` always rounds down toward negative infinity
- `math.ceil(x)` always rounds up toward positive infinity
- `math.trunc(x)` removes the decimal part (toward zero)
- `int(x)` and `math.trunc(x)` behave the same for positive numbers
- `math` must be imported before using floor, ceil, or trunc
- `random` must be imported before generating random values
- `random.random()` returns a float between 0.0 and 1.0
- `random.randint(a, b)` returns an integer from a to b inclusive
- `float.is_integer()` checks if a float has no decimal part
- `isinstance(x, t)` verifies the type of a value at runtime

#### Example

```python
import math
import random

price = 35.54879865

# Rounding
print(round(price, 2))      # Output: 35.55
print(math.floor(price))    # Output: 35
print(math.ceil(price))     # Output: 36
print(math.trunc(price))    # Output: 35

# Negative numbers behave differently
print(math.floor(-1.3))     # Output: -2 (down = more negative)
print(math.ceil(-1.3))      # Output: -1 (up = less negative)
print(math.trunc(-1.7))     # Output: -1 (toward zero)

# Random
print(random.random())          # Output: 0.4738... (varies)
print(random.randint(1, 6))     # Output: 4 (varies, simulates dice)

# Validation
x = 7.0
print(x.is_integer())       # Output: True

y = 70.4
print(isinstance(y, float)) # Output: True
print(isinstance(y, int))   # Output: False
```

#### Why This Lesson Matters

Rounding is essential in any program that displays numbers to users or performs financial calculations. Displaying `35.54879865` instead of `35.55` is unprofessional and confusing. Random number generation is fundamental to testing, simulations, and games. Type validation prevents runtime errors by ensuring a value is numeric before performing operations on it.

---

## 🧠 Core Concepts Summary

| Concept | Method or Operator | Description | Example |
|---|---|---|---|
| Integer type | `int` | Whole numbers | `x = 10` |
| Float type | `float` | Decimal numbers | `x = 3.14` |
| Complex type | `complex` | Real and imaginary | `x = 3+4j` |
| Convert to int | `int(x)` | Converts to integer | `int("25")` → `25` |
| Convert to float | `float(x)` | Converts to float | `float("3")` → `3.0` |
| Addition | `+` | Adds two values | `5 + 3` → `8` |
| Subtraction | `-` | Subtracts | `5 - 3` → `2` |
| Multiplication | `*` | Multiplies | `5 * 3` → `15` |
| Division | `/` | Always returns float | `5 / 2` → `2.5` |
| Floor division | `//` | Returns integer, rounds down | `5 // 2` → `2` |
| Modulo | `%` | Returns remainder | `5 % 2` → `1` |
| Exponentiation | `**` | Raises to power | `2 ** 8` → `256` |
| Absolute value | `abs(x)` | Non-negative value | `abs(-5)` → `5` |
| Round | `round(x, n)` | Rounds to n decimals | `round(3.567, 2)` → `3.57` |
| Floor | `math.floor(x)` | Always rounds down | `math.floor(1.9)` → `1` |
| Ceiling | `math.ceil(x)` | Always rounds up | `math.ceil(1.1)` → `2` |
| Truncate | `math.trunc(x)` | Removes decimal | `math.trunc(1.9)` → `1` |
| Random float | `random.random()` | Float between 0 and 1 | `0.7462...` |
| Random int | `random.randint(a, b)` | Integer from a to b | `randint(1, 6)` → `4` |
| Is whole number | `x.is_integer()` | Float has no decimal | `(7.0).is_integer()` → `True` |
| Type check | `isinstance(x, t)` | Confirms type | `isinstance(5, int)` → `True` |

---

## 📋 Reference Tables

### Arithmetic Operators

| Operator | Name | Example | Result | Notes |
|---|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` | |
| `-` | Subtraction | `5 - 3` | `2` | |
| `*` | Multiplication | `5 * 3` | `15` | |
| `/` | Division | `5 / 2` | `2.5` | Always returns float |
| `//` | Floor Division | `5 // 2` | `2` | Rounds down to integer |
| `%` | Modulo | `5 % 2` | `1` | Returns remainder |
| `**` | Exponentiation | `2 ** 8` | `256` | Raises to power |

### Shorthand Assignment Operators

| Operator | Equivalent | Example | Result |
|---|---|---|---|
| `+=` | `x = x + n` | `x = 5; x += 3` | `8` |
| `-=` | `x = x - n` | `x = 5; x -= 3` | `2` |
| `*=` | `x = x * n` | `x = 5; x *= 3` | `15` |
| `/=` | `x = x / n` | `x = 6; x /= 2` | `3.0` |
| `//=` | `x = x // n` | `x = 7; x //= 2` | `3` |
| `%=` | `x = x % n` | `x = 7; x %= 3` | `1` |
| `**=` | `x = x ** n` | `x = 2; x **= 3` | `8` |

### Rounding Functions Comparison

| Function | Direction | `1.3` | `1.7` | `-1.3` | `-1.7` | Module |
|---|---|---|---|---|---|---|
| `round(x)` | Nearest | `1` | `2` | `-1` | `-2` | Built-in |
| `math.floor(x)` | Always down ↓ | `1` | `1` | `-2` | `-2` | `math` |
| `math.ceil(x)` | Always up ↑ | `2` | `2` | `-1` | `-1` | `math` |
| `math.trunc(x)` | Toward zero ✂️ | `1` | `1` | `-1` | `-1` | `math` |

### Random Functions

| Function | Returns | Range | Example |
|---|---|---|---|
| `random.random()` | `float` | 0.0 to 1.0 | `0.7462...` |
| `random.randint(a, b)` | `int` | a to b (inclusive) | `randint(1, 6)` → `4` |

---

## 🧪 Practice Challenges

### Challenge 1 — Division Explorer

Write a program that demonstrates the difference between all three division-related operators using the same two numbers.

Requirements:

- Use `x = 17` and `y = 5`
- Show regular division, floor division, and modulo
- Label each result clearly

Expected output:

```text
17 / 5  = 3.4
17 // 5 = 3
17 % 5  = 2
```

---

### Challenge 2 — Even or Odd Checker

Write a program that generates a random integer between 1 and 100 and checks whether it is even or odd.

Requirements:

- Use `random.randint()` to generate the number
- Use modulo `%` to determine even or odd
- Display the number and the result

Expected output:

```text
Random number: 47
47 is odd
```

---

### Challenge 3 — Price Formatter

Write a program that takes a raw price and produces two formatted versions.

Requirements:

- Start with: `price = 19.987654`
- Round to 2 decimal places using `round()`
- Round down using `math.floor()`
- Round up using `math.ceil()`
- Display all three versions with labels

Expected output:

```text
Original:  19.987654
Rounded:   19.99
Floor:     19
Ceiling:   20
```

---

### Challenge 4 — Pagination Calculator

Write a program that calculates the number of pages needed to display a set of records.

Requirements:

- Total records: `157`
- Records per page: `25`
- Use `math.ceil()` to calculate pages needed
- Use `%` to calculate how many records are on the last page
- Display both results

Expected output:

```text
Total records:    157
Records per page: 25
Pages needed:     7
Last page items:  7
```

---

### Challenge 5 — Temperature Converter

Write a program that converts between Celsius and Fahrenheit and rounds the result.

Requirements:

- Convert `25°C` to Fahrenheit using `(C × 9/5) + 32`
- Convert `77°F` to Celsius using `(F - 32) × 5/9`
- Round both results to 1 decimal place
- Display the results with labels

Expected output:

```text
25°C = 77.0°F
77°F = 25.0°C
```

---

## 🏗️ Mini Project — Smart Invoice Calculator

### Project Goal

Build a program that calculates a final invoice amount from a raw price by applying a discount, adding tax, and rounding the result correctly.

### Requirements

The program must:

- Accept a product name, original price, discount percentage, and tax percentage.
- Validate that the price is a number using `isinstance()`.
- Calculate the discounted price.
- Calculate the taxed price.
- Round the final result to 2 decimal places.
- Display a full invoice summary.

### Starter Code

```python
import math

product  = "Python Course"
price    = 199.99
discount = 20   # percent
tax      = 8    # percent

# Validate
if not isinstance(price, (int, float)):
    print("Invalid price")
else:
    # Calculate
    discount_amount = price * (discount / 100)
    after_discount  = price - discount_amount
    tax_amount      = after_discount * (tax / 100)
    final_price     = round(after_discount + tax_amount, 2)

    # Display
    print("=" * 40)
    print("           INVOICE SUMMARY")
    print("=" * 40)
    print(f"Product:          {product}")
    print(f"Original Price:   ${price}")
    print(f"Discount ({discount}%):    -${round(discount_amount, 2)}")
    print(f"After Discount:   ${round(after_discount, 2)}")
    print(f"Tax ({tax}%):         +${round(tax_amount, 2)}")
    print("=" * 40)
    print(f"Final Price:      ${final_price}")
    print("=" * 40)
```

### Expected Output

```text
========================================
           INVOICE SUMMARY
========================================
Product:          Python Course
Original Price:   $199.99
Discount (20%):   -$40.0
After Discount:   $159.99
Tax (8%):         +$12.8
========================================
Final Price:      $172.79
========================================
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Forgetting that `/` always returns float | `6 / 2` returns `3.0` not `3` | Use `//` when an integer result is needed |
| Confusing `//` with `/` | Floor division drops decimal, regular division keeps it | Choose the operator based on whether decimal matters |
| Not converting string numbers before arithmetic | `"5" + 3` raises `TypeError` | Wrap with `int()` or `float()` first |
| Forgetting to `import math` | `math.floor()` raises `NameError` | Always add `import math` at the top of the file |
| Forgetting to `import random` | `random.randint()` raises `NameError` | Always add `import random` at the top of the file |
| Assuming `round(1.5)` always gives `2` | Python uses banker's rounding: rounds to nearest even | Be aware of this when precision is critical |
| Using `is` instead of `isinstance()` for type checking | `is int` is not valid Python | Use `isinstance(x, int)` for type checking |
| Ignoring operator precedence | `2 + 3 * 4` gives `14` not `20` | Use parentheses to make intent explicit |

---

## 💡 Professional Tips

- Use `//` for pagination, batching, and any calculation where you need a whole number result.
- Use `%` to check even/odd status and to find remainders in data splits.
- Use `round(x, 2)` consistently for any money-related calculation.
- Use `math.ceil()` whenever the result must be "at least" a certain value, such as number of pages or batches.
- Always import `math` and `random` at the top of the file, not inside a function or conditional.
- Use `abs()` for distance and difference calculations where direction does not matter.
- Remember that `math.floor()` and `math.ceil()` behave differently on negative numbers.
- Use `isinstance(x, (int, float))` to accept both integers and floats in a single check.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 4, make sure you can:

- [ ] Identify the three Python numeric types: `int`, `float`, `complex`.
- [ ] Explain why `"25" * 3` gives `"252525"` instead of `75`.
- [ ] Convert string numbers to `int` and `float` for arithmetic.
- [ ] Use all seven arithmetic operators correctly.
- [ ] Explain the difference between `/` and `//`.
- [ ] Use modulo `%` to check if a number is even or odd.
- [ ] Use shorthand operators: `+=`, `-=`, `*=`, and others.
- [ ] Apply PEMDAS and use parentheses to control evaluation order.
- [ ] Use `abs()` for absolute value calculations.
- [ ] Explain the difference between `round()`, `floor()`, `ceil()`, and `trunc()`.
- [ ] Use `math.floor()` and `math.ceil()` correctly including with negative numbers.
- [ ] Generate random floats and integers using the `random` module.
- [ ] Use `is_integer()` to check if a float has no decimal part.
- [ ] Use `isinstance()` to validate a value's numeric type.
- [ ] Build the Smart Invoice Calculator mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 4 when they can:

1. Run both chapter files without errors.
2. Explain the output of every print statement in each file.
3. Modify examples with different values and predict the results correctly.
4. Complete all five practice challenges without referring to the solutions.
5. Build the mini project independently without referring to the starter code.
6. Explain when to use `//` instead of `/` and why it matters.
7. Explain the difference in behavior between `math.floor()` and `math.trunc()` on negative numbers.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 4 — Python Logic and Operators

Chapter 4 introduces boolean logic, which depends directly on the numeric skills built here. Comparison operators produce `True` or `False` by comparing numeric values. Modulo results feed into even/odd conditions. The `isinstance()` function introduced in this chapter reappears in Chapter 4 as a validation tool in boolean expressions.

---

## 📚 Additional Resources

- [Python Official Documentation — Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Official Documentation — math Module](https://docs.python.org/3/library/math.html)
- [Python Official Documentation — random Module](https://docs.python.org/3/library/random.html)
- [PEP 8 — Number Formatting Recommendations](https://peps.python.org/pep-0008/)
- [Real Python — Python Numbers](https://realpython.com/python-numbers/)

---

<p align="center">
  <strong>Chapter 3 Complete — Python Numbers ✅</strong>
</p>

<p align="center">
  <a href="../02_strings/Readme.md">← Previous Chapter: Python Strings</a> ·
  <a href="../README.md">Main README</a> ·
  <a href="../04_logic_and_operators/README.md">Next Chapter: Python Logic and Operators →</a>
</p>
