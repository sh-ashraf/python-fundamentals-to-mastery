# Chapter 3: Python Numbers

> Master numeric operations, mathematical functions, and number validation

---

## 📚 Chapter Overview

This chapter covers **everything you need to work with numbers in Python**. From basic arithmetic to advanced mathematical functions, you'll learn how to perform calculations, round numbers, generate random values, and validate numeric data.

By the end of this chapter, you'll be able to:
- Perform arithmetic operations with integers and floats
- Apply mathematical functions for rounding and calculations
- Generate random numbers for testing and simulations
- Validate and check numeric data types

---

## 🎯 Learning Objectives

By completing this chapter, you will be able to:

✅ Understand the difference between `int`, `float`, and `complex` types  
✅ Perform arithmetic operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
✅ Use shorthand assignment operators (`+=`, `-=`, `*=`, etc.)  
✅ Round numbers using `round()`, `floor()`, `ceil()`, and `trunc()`  
✅ Calculate absolute values with `abs()`  
✅ Generate random numbers with the `random` module  
✅ Validate number types with `isinstance()` and `is_integer()`  
✅ Apply mathematical concepts to real-world problems  

---

## 📁 Files in This Chapter

| # | File Name | Topic | Key Concepts |
|---|-----------|-------|--------------|
| 01 | `01_number_types_and_operations.py` | Types & Operations | `int`, `float`, `complex`, arithmetic operators, type conversion, PEMDAS |
| 02 | `02_math_functions_and_validation.py` | Math & Validation | `abs()`, `round()`, `floor()`, `ceil()`, `trunc()`, `random`, validation |

---

## 🔑 Key Concepts Covered

### **1. Number Types & Conversion**
- Three number types: `int`, `float`, `complex`
- Type checking with `type()`
- Type conversion: `int()`, `float()`, `complex()`
- String to number conversion

### **2. Arithmetic Operators**
- Addition (`+`), Subtraction (`-`), Multiplication (`*`)
- Division (`/`) - always returns float
- Floor Division (`//`) - rounds down to integer
- Modulo (`%`) - returns remainder
- Exponentiation (`**`) - power operation
- Shorthand operators: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

### **3. Mathematical Functions**
- Absolute value: `abs()`
- Rounding: `round()`, `math.floor()`, `math.ceil()`, `math.trunc()`
- Understanding banker's rounding
- Negative number rounding behavior

### **4. Random Numbers**
- Random floats: `random.random()`
- Random integers: `random.randint()`
- Use cases: testing, simulations, games

### **5. Number Validation**
- Check if float is whole: `is_integer()`
- Type checking: `isinstance()`
- Input validation techniques

---

## 💻 Code Examples

### **Arithmetic Operations:**
```python
x = 10
y = 3

print(x + y)   # Output: 13 (addition)
print(x - y)   # Output: 7 (subtraction)
print(x * y)   # Output: 30 (multiplication)
print(x / y)   # Output: 3.333... (division, returns float)
print(x // y)  # Output: 3 (floor division)
print(x % y)   # Output: 1 (remainder)
print(x ** y)  # Output: 1000 (10 to power of 3)
```

### **Rounding Numbers:**
```python
import math

price = 35.7

print(round(price))        # Output: 36 (nearest integer)
print(math.floor(price))   # Output: 35 (always down)
print(math.ceil(price))    # Output: 36 (always up)
print(math.trunc(price))   # Output: 35 (chop decimals)
```

### **Random Numbers:**
```python
import random

# Random float between 0 and 1
probability = random.random()
print(probability)  # Output: 0.7462... (varies)

# Random integer (dice roll)
dice = random.randint(1, 6)
print(dice)  # Output: 4 (random 1-6)
```

### **Number Validation:**
```python
x = 7.0
print(x.is_integer())  # Output: True

y = 7.5
print(y.is_integer())  # Output: False

# Type checking
print(isinstance(x, float))  # Output: True
print(isinstance(25, int))   # Output: True
```

---

## 🎯 Practical Challenges

### **Challenge 1: Temperature Converter**
**Task:** Create a function that converts between Celsius and Fahrenheit.

**Requirements:**
1. Accept temperature and conversion type
2. Use correct formula
3. Round result to 1 decimal place

**Formulas:**
- Celsius to Fahrenheit: `(C × 9/5) + 32`
- Fahrenheit to Celsius: `(F - 32) × 5/9`

**Expected Output:**
```
convert_temp(25, "C to F")  → 77.0°F
convert_temp(77, "F to C")  → 25.0°C
```

---

### **Challenge 2: Even/Odd Counter**
**Task:** Count how many even and odd numbers exist in a range.

**Requirements:**
1. Generate random numbers between 1 and 100
2. Count even numbers (divisible by 2)
3. Count odd numbers
4. Display percentages

**Expected Output:**
```
Generated 50 numbers
Even: 26 (52%)
Odd: 24 (48%)
```

---

### **Challenge 3: Price Calculator**
**Task:** Calculate final price with tax and discount, properly rounded.

**Requirements:**
1. Original price (input)
2. Apply discount percentage
3. Add tax percentage
4. Round to 2 decimal places

**Example:**
```
Original Price: $100
Discount: 20%
Tax: 10%

After discount: $80
After tax: $88.00
Final Price: $88.00
```

---

### **Challenge 4: Pagination Calculator**
**Task:** Calculate number of pages needed for pagination.

**Requirements:**
1. Total items (input)
2. Items per page (input)
3. Calculate pages needed (always round UP)
4. Display results

**Expected Output:**
```
Total items: 157
Items per page: 25
Pages needed: 7
Last page items: 7
```

**Hints:**
- Use `math.ceil()` for pages
- Use `%` to find items on last page

---

## 📊 Quick Reference Tables

### **Number Types**
| Type | Description | Example | Use Case |
|------|-------------|---------|----------|
| `int` | Whole numbers | `42`, `-5`, `0` | Counting, indexing |
| `float` | Decimal numbers | `3.14`, `-0.5` | Measurements, calculations |
| `complex` | Complex numbers | `3+4j` | Advanced math, engineering |

### **Arithmetic Operators**
| Operator | Name | Example | Result | Notes |
|----------|------|---------|--------|-------|
| `+` | Addition | `5 + 3` | `8` | |
| `-` | Subtraction | `5 - 3` | `2` | |
| `*` | Multiplication | `5 * 3` | `15` | |
| `/` | Division | `5 / 2` | `2.5` | Always returns float |
| `//` | Floor Division | `5 // 2` | `2` | Rounds down |
| `%` | Modulo | `5 % 2` | `1` | Remainder |
| `**` | Exponentiation | `5 ** 2` | `25` | Power |

### **Rounding Functions**
| Function | Behavior | `math.floor(1.7)` | `math.ceil(1.3)` | `round(1.5)` | `math.trunc(1.9)` |
|----------|----------|-------------------|------------------|--------------|-------------------|
| **Result** | | `1` | `2` | `2` | `1` |
| **Direction** | | Always DOWN ↓ | Always UP ↑ | Nearest ↕ | Chop decimals ✂️ |
| **Module** | | `math` | `math` | Built-in | `math` |

### **Random Functions**
| Function | Returns | Example | Use Case |
|----------|---------|---------|----------|
| `random.random()` | Float 0.0-1.0 | `0.7462...` | Probability, chance |
| `random.randint(a, b)` | Integer from a to b | `randint(1, 6)` → `4` | Dice, IDs, testing |

### **Validation Functions**
| Function | Purpose | Example | Returns |
|----------|---------|---------|---------|
| `is_integer()` | Check if float is whole | `(7.0).is_integer()` | `True` |
| `isinstance(x, type)` | Check type | `isinstance(5, int)` | `True` |

---

## 🧠 Common Mistakes & Tips

### **Mistakes to Avoid:**
❌ Forgetting that `/` always returns a float (even `6 / 2` → `2.0`)  
❌ Confusing `//` (floor division) with `/` (regular division)  
❌ Trying to do math with string numbers without conversion  
❌ Using `round()` for floor/ceiling (use `math.floor()` or `math.ceil()`)  
❌ Forgetting to `import math` before using `floor()`, `ceil()`, `trunc()`  
❌ Forgetting to `import random` before generating random numbers  
❌ Assuming `round(1.5)` → `2` always (banker's rounding rounds to even)  

### **Pro Tips:**
✅ Use `//` for integer division (e.g., pagination, splitting items)  
✅ Use `%` to check even/odd: `if x % 2 == 0` means even  
✅ Use `abs()` for distance calculations (always positive)  
✅ Use `math.ceil()` for "at least" calculations (pages needed, batches)  
✅ Use `round(x, 2)` for money (always 2 decimal places)  
✅ Use `random.seed()` for reproducible random numbers in testing  
✅ Remember PEMDAS: Parentheses, Exponents, Multiply/Divide, Add/Subtract  

---

## 📝 What You Learned

After completing this chapter, you should know:

- ✅ The three main number types in Python
- ✅ How to perform all basic arithmetic operations
- ✅ The difference between `/` and `//`
- ✅ How to use modulo (`%`) for remainders and even/odd checks
- ✅ How to convert between number types
- ✅ Four different ways to round numbers
- ✅ How to generate random numbers for testing
- ✅ How to validate numeric data
- ✅ Real-world applications: pricing, pagination, temperature conversion

---

## 🚀 Next Steps

**Ready for Chapter 4?** Move on to:
- **Chapter 4: Logic & Operators** - Master boolean logic, comparison operators, and conditional thinking

**Want More Practice?**
- Build a simple calculator with all operators
- Create a dice game using random numbers
- Make a tip calculator with proper rounding
- Build a number guessing game
- Create a unit converter (distance, weight, temperature)

---

## 📚 Additional Resources

- [Python Official Docs - Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python Math Module](https://docs.python.org/3/library/math.html)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Real Python - Numbers Guide](https://realpython.com/python-numbers/)

---

## 💡 Study Tips for This Chapter

### **Practice Strategy:**
1. **Master the Operators:** Practice each operator until it's second nature
2. **Understand Division:** Know when to use `/` vs `//` vs `%`
3. **Rounding Practice:** Try each rounding function with positive and negative numbers
4. **Build Projects:** Create calculators that use multiple operations

### **Common Use Cases to Practice:**
- Price calculations (tax, discount, rounding)
- Data pagination (floor division, ceiling)
- Even/odd checking (modulo)
- Distance calculations (absolute value)
- Random testing data generation

### **Debugging Tips:**
- Print intermediate results to verify calculations
- Check types with `type()` when operations fail
- Remember division always returns float
- Test rounding with negative numbers to understand behavior

---

## 🔗 Integration with Other Chapters

### **Builds On:**
- **Chapter 1:** Variables, data types, `print()`, `input()`
- **Chapter 2:** String conversion, formatting with f-strings

### **Prepares For:**
- **Chapter 4:** Boolean results from comparisons (`x > y`)
- **Chapter 5:** Numeric conditions in if statements
- **Chapter 6:** Loop counters and ranges

### **Real-World Connection:**
Numbers are fundamental in programming:
- Financial calculations (banking, e-commerce)
- Data analysis and statistics
- Game development (scores, physics)
- Scientific computing
- Machine learning algorithms

---

## 🎓 Mathematical Concepts Covered

### **PEMDAS - Order of Operations:**
```
1. Parentheses    ()
2. Exponents      **
3. Multiply/Divide  *, /, //, %
4. Add/Subtract   +, -
```

### **Division Types:**
- **Regular Division (`/`)**: Always returns float
- **Floor Division (`//`)**: Returns integer, rounds down
- **Modulo (`%`)**: Returns remainder

### **Rounding Types:**
- **Nearest**: `round()` - to closest value
- **Down**: `math.floor()` - always lower
- **Up**: `math.ceil()` - always higher
- **Truncate**: `math.trunc()` - remove decimals

---

<div align="center">

**Chapter 3 Complete!** ✅

[← Previous: Strings](../02_strings/Readme.md) | [Main README](../03_numbers/README.md) | [Next: Logic & Operators →](../04_logic_and_operators/README.md)

</div>