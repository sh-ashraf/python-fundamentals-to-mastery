# Chapter 1 — Python Fundamentals

<p align="center">
  <strong>Build the essential foundation that every Python program depends on.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-01-orange" alt="Chapter 01">
  <img src="https://img.shields.io/badge/Focus-Fundamentals-purple" alt="Focus: Fundamentals">
</p>

---

## 📌 Chapter Overview

This chapter introduces the essential building blocks that every Python learner must understand before moving into any other topic. It answers four fundamental questions that every program must be able to address: how to display information, how to store information, how to receive information from the user, and how Python classifies the different kinds of information it works with.

The chapter moves deliberately from output, to storage, to input, to type awareness. Each lesson prepares the learner for the next one, and together they give the learner the ability to write small, interactive, and meaningful Python programs from the very beginning.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Use `print()` to display text, variables, and formatted output.
- Apply escape sequences to control how text appears in the console.
- Produce multi-line output using three different techniques.
- Create, reuse, and update variables using correct naming conventions.
- Collect user input at runtime using `input()`.
- Explain why `input()` always returns a string regardless of what the user types.
- Convert values between types using `int()`, `float()`, `str()`, and `bool()`.
- Distinguish between hard-coded and dynamic values.
- Identify Python's basic data types using `type()`.
- Explain the difference between `int`, `float`, `str`, `bool`, and `None`.
- Understand dynamic typing and predict how a variable's type can change.
- Build small interactive programs that combine output, variables, input, and type conversion.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners starting Python with no previous programming background |
| Programming beginners | Learners who need a clear foundation before moving into advanced topics |
| Data learners | Learners preparing for data analysis, data engineering, automation, or AI |
| Review learners | Learners who want to revisit Python basics in a structured and professional way |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Open and run a Python file using a code editor or terminal.
- Understand that Python executes code line by line from top to bottom.
- Read basic programming terms such as function, value, variable, input, and output.

No previous programming experience is required.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from displaying output to understanding how Python classifies the values that programs produce and receive.

```text
Displaying Output with print()
            ↓
Formatting Output with Escape Sequences
            ↓
Storing Values with Variables
            ↓
Receiving Values with input()
            ↓
Converting Types with int(), float(), str()
            ↓
Understanding Python Data Types
            ↓
Dynamic Typing and Type Checking
```

This sequence is intentional:

1. The learner first sees how Python communicates results to the user.
2. Then the learner stores values instead of repeating fixed text.
3. Then the learner makes programs interactive by receiving values from the user.
4. Then the learner converts those values into the correct type for calculation.
5. Finally, the learner understands how Python classifies and manages all values.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_print_and_escape_sequences.py` | Output and Formatting | Displaying text, escape sequences, multi-line output |
| 02 | `02_variables_and_storage.py` | Variables and Storage | Storing, reusing, and updating values |
| 03 | `03_input_and_type_conversion.py` | Input and Type Conversion | Receiving input, converting types, dynamic values |
| 04 | `04_data_types_overview.py` | Data Types | Identifying and working with Python value types |

---

## 🧭 Recommended Study Order

### 1. Start with Output

**File:** `01_print_and_escape_sequences.py`

Start with `print()` because it gives the learner immediate feedback. Before storing or receiving values, the learner needs to know how Python shows results. Every example in the following lessons depends on `print()` to verify the output.

The learner studies:

- Basic `print()` syntax and usage
- Escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`, `\b`
- Three techniques for multi-line output
- The `sep` and `end` parameters

---

### 2. Move to Variables

**File:** `02_variables_and_storage.py`

After understanding output, the learner needs to store values and reuse them across multiple print statements. Variables eliminate repetition and make programs flexible.

The learner studies:

- Variable assignment and reuse
- Variable reassignment and updating
- String concatenation with variables
- Naming conventions and rules
- Hard-coded values vs stored values

---

### 3. Add User Input

**File:** `03_input_and_type_conversion.py`

Once variables are understood, the learner is ready to store values that come from the user rather than the code itself. This makes programs interactive and introduces the concept of type conversion.

The learner studies:

- `input()` and how it works
- Why `input()` always returns a string
- Converting input with `int()` and `float()`
- The difference between hard-coded and dynamic values
- f-strings for combining different value types

---

### 4. Understand Data Types

**File:** `04_data_types_overview.py`

After working with values of different kinds, the learner is ready to understand how Python classifies and manages those values. This lesson ties together everything from the previous three files.

The learner studies:

- The three categories of Python data types
- Primitive types: `int`, `float`, `str`, `bool`, `NoneType`
- Collection types: `list`, `tuple`, `set`, `dict`
- Checking types with `type()`
- Dynamic typing
- Type conversion functions

---

## 🧱 Lesson Breakdown

### Lesson 1 — Output with print()

**File:** `01_print_and_escape_sequences.py`

This lesson introduces the first interaction between a program and its user: output. The learner discovers how to display any message to the console and how to control the appearance of that output using escape sequences and multi-line techniques.

#### Key Concepts

- `print()` as a built-in Python function
- Escape sequences: `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (double quote), `\'` (single quote), `\b` (backspace)
- Method 1: `\n` inside a single string
- Method 2: String continuation across multiple lines
- Method 3: Triple-quoted strings
- `sep` and `end` parameters

#### Example

```python
print("Hello, Python!")
# Output: Hello, Python!

print("Line 1\nLine 2")
# Output:
# Line 1
# Line 2

print("A", "B", "C", sep="-")
# Output: A-B-C
```

#### Why This Lesson Matters

`print()` is the most immediate way for a learner to see whether their code is working. It is also one of the most practical tools for testing and debugging. Understanding escape sequences allows the learner to format output clearly, which becomes important as programs grow more complex.

---

### Lesson 2 — Variables and Storage

**File:** `02_variables_and_storage.py`

This lesson explains how to give values a name so they can be stored, reused, and updated throughout a program. Variables eliminate the need to repeat values and make code easier to maintain.

#### Key Concepts

- Variable assignment with `=`
- Reusing the same variable in multiple places
- Updating a variable with a new value
- String concatenation with variables
- `snake_case` naming convention
- Python naming rules

#### Example

```python
name = "Shehab"
language = "Python"

print(name, "is learning", language)
# Output: Shehab is learning Python

# Update the variable
language = "SQL"
print(language)
# Output: SQL
```

#### Why This Lesson Matters

Almost every program stores information in variables. Without variables, a program would need to repeat the same value in every line. Understanding how to name and update variables is the foundation of writing readable and maintainable code.

---

### Lesson 3 — User Input and Type Conversion

**File:** `03_input_and_type_conversion.py`

This lesson makes programs interactive. Instead of working with values the programmer defined in advance, the program can now receive values from the user at runtime. It also introduces the critical concept of type conversion, which is necessary because `input()` always returns a string.

#### Key Concepts

- `input()` for collecting runtime values
- Why `input()` returns a string regardless of what is typed
- `int()` for converting to integer
- `float()` for converting to decimal
- Hard-coded values vs dynamic values
- f-strings for formatted output

#### Example

```python
name = input("Enter your name: ")
# User types: Ahmed

age = int(input("Enter your age: "))
# User types: 25

print(f"{name} is {age} years old")
# Output: Ahmed is 25 years old

print(age + 5)
# Output: 30
```

#### Why This Lesson Matters

Most real programs do not work with fixed values only. They receive data from users, files, or databases. `input()` is the beginner-friendly starting point for understanding interactive programs. Type conversion is equally important because without it, the learner cannot perform calculations on values entered by the user.

---

### Lesson 4 — Data Types Overview

**File:** `04_data_types_overview.py`

This lesson gives the learner a complete mental model of how Python classifies values. After working with strings, numbers, booleans, and None across the previous lessons, the learner is now ready to understand the system that organizes them all.

#### Key Concepts

- Three categories: no value, single value, multi value
- Primitive types: `int`, `float`, `str`, `bool`, `NoneType`
- Collection types: `list`, `tuple`, `set`, `dict`
- `type()` for checking a value's type
- Dynamic typing: a variable can hold different types over time
- Type conversion: `int()`, `float()`, `str()`, `bool()`
- `None` vs `""` vs `"  "`: three different concepts

#### Example

```python
age = 21
height = 175.5
name = "Shehab"
is_student = True
future_job = None

print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
print(type(future_job)) # <class 'NoneType'>

# Dynamic typing
x = 10
print(type(x))  # <class 'int'>
x = "Python"
print(type(x))  # <class 'str'>
```

#### Why This Lesson Matters

Understanding data types prevents common errors that beginners encounter constantly: adding a string to a number, confusing `None` with an empty string, or not knowing why `type()` returns an unexpected result. This lesson brings the whole chapter together and prepares the learner for every chapter that follows.

---

## 🧠 Core Concepts Summary

| Concept | Description | Example |
|---|---|---|
| `print()` | Displays output to the console | `print("Hello")` |
| Escape sequence | Controls text formatting inside strings | `\n`, `\t`, `\\` |
| Variable | A named container that stores a value | `name = "Ahmed"` |
| `input()` | Collects a value from the user at runtime | `name = input("Name: ")` |
| Type conversion | Changes a value from one type to another | `int("25")` → `25` |
| `type()` | Returns the data type of a value | `type(25)` → `<class 'int'>` |
| Dynamic typing | A variable can hold different types over time | `x = 10`, then `x = "text"` |
| `None` | Represents the absence of a value | `future_job = None` |

---

## 📋 Reference Tables

### Escape Sequences

| Sequence | Effect | Example Output |
|---|---|---|
| `\n` | New line | Moves to next line |
| `\t` | Horizontal tab | Adds tab space |
| `\\` | Backslash | Prints `\` |
| `\"` | Double quote | Prints `"` |
| `\'` | Single quote | Prints `'` |
| `\b` | Backspace | Removes previous character |

### Type Conversion Functions

| Function | Purpose | Example | Result |
|---|---|---|---|
| `int(x)` | Convert to integer | `int("25")` | `25` |
| `float(x)` | Convert to decimal | `float("1.75")` | `1.75` |
| `str(x)` | Convert to string | `str(25)` | `"25"` |
| `bool(x)` | Convert to boolean | `bool(0)` | `False` |

### Python Data Types

| Category | Type | Description | Example |
|---|---|---|---|
| No Value | `NoneType` | Absence of a value | `None` |
| Single Value | `int` | Whole numbers | `42`, `-5` |
| Single Value | `float` | Decimal numbers | `3.14` |
| Single Value | `str` | Text | `"Hello"` |
| Single Value | `bool` | True or False | `True` |
| Multi Value | `list` | Ordered, mutable | `[1, 2, 3]` |
| Multi Value | `tuple` | Ordered, immutable | `(1, 2, 3)` |
| Multi Value | `set` | Unordered, unique | `{1, 2, 3}` |
| Multi Value | `dict` | Key-value pairs | `{"name": "Ahmed"}` |

### None vs Empty String vs Whitespace

| Value | Type | Meaning | `bool()` Result |
|---|---|---|---|
| `None` | `NoneType` | No value exists | `False` |
| `""` | `str` | Value exists but is empty | `False` |
| `"  "` | `str` | Value exists, contains spaces | `False` |

---

## 🧪 Practice Challenges

### Challenge 1 — Escape Sequence Explorer

Write a program that uses at least four different escape sequences in a single print statement. Display a formatted block of text that includes a title, a new line, a tab-indented list, and a separator line using repeated characters.

Expected output format:

```text
My Learning Path:
	- Python Basics
	- Data Engineering
	- AI
--------------------
```

---

### Challenge 2 — Variable Reuse Demonstrator

Create a program that stores a name and a domain in two variables. Use those variables to generate three different email addresses and one full profile URL by combining the variables with string concatenation.

Expected output:

```text
info@datawithbaraa.com
support@datawithbaraa.com
admin@datawithbaraa.com
www.datawithbaraa.com/profile
```

---

### Challenge 3 — Interactive Profile Builder

Write a program that asks the user for their name, age, and city. Convert the age to an integer, then display a formatted profile using an f-string.

Expected output:

```text
Enter your name: Sara
Enter your age: 22
Enter your city: Cairo

Profile:
Name: Sara
Age: 22
City: Cairo
In 10 years, Sara will be 32 years old.
```

---

### Challenge 4 — Type Detective

Create variables of five different types: `int`, `float`, `str`, `bool`, and `None`. Print each variable alongside its type and a brief description of what type it is.

Expected output:

```text
25 → <class 'int'> → whole number
1.75 → <class 'float'> → decimal number
Ahmed → <class 'str'> → text
True → <class 'bool'> → boolean
None → <class 'NoneType'> → no value
```

---

### Challenge 5 — Dynamic Typing Demonstrator

Create a single variable and assign it three different values of three different types one after another. After each assignment, print the value and its type to show how the type changes.

Expected output:

```text
Value: 10 | Type: <class 'int'>
Value: Python | Type: <class 'str'>
Value: 3.14 | Type: <class 'float'>
```

---

## 🏗️ Mini Project — Interactive Profile Card

### Project Goal

Build a small interactive program that collects personal information from the user and displays a clean, formatted profile card that includes the value and the data type of each field.

### Requirements

The program must:

- Ask for name, age, city, height in meters, and student status.
- Store each value in a clearly named variable.
- Convert age to `int` and height to `float`.
- Convert student status from a yes/no answer to `bool`.
- Display a formatted profile card using f-strings.
- Print the data type of each value below the card.

### Starter Code

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("=" * 35)
print("         USER PROFILE CARD")
print("=" * 35)
print(f"Name:    {name}")
print(f"Age:     {age}")
print(f"City:    {city}")
print(f"Height:  {height}m")
print(f"Student: {is_student}")
print("=" * 35)

print("\nData Types:")
print(f"Name:    {type(name)}")
print(f"Age:     {type(age)}")
print(f"City:    {type(city)}")
print(f"Height:  {type(height)}")
print(f"Student: {type(is_student)}")
```

### Expected Output

```text
Enter your name: Ahmed
Enter your age: 25
Enter your city: Cairo
Enter your height in meters: 1.75
Are you a student? (yes/no): yes

===================================
         USER PROFILE CARD
===================================
Name:    Ahmed
Age:     25
City:    Cairo
Height:  1.75m
Student: True
===================================

Data Types:
Name:    <class 'str'>
Age:     <class 'int'>
City:    <class 'str'>
Height:  <class 'float'>
Student: <class 'bool'>
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Forgetting that `input()` returns a string | Math operations will raise a `TypeError` | Wrap with `int()` or `float()` before using in calculations |
| Writing numbers inside quotes | Python treats `"25"` as text, not a number | Use `25` without quotes for numeric values |
| Using `=` instead of `==` for comparison | `=` assigns a value, it does not compare | Use `==` when comparing, `=` when assigning |
| Confusing `None` with `""` | They represent different situations | `None` means no value, `""` means an empty string exists |
| Joining a string and an integer with `+` | Raises a `TypeError` | Use f-strings or convert with `str()` |
| Using reserved keywords as variable names | Python raises a `SyntaxError` | Avoid names like `if`, `for`, `while`, `type`, `input` |
| Writing `true` or `false` in lowercase | Python raises a `NameError` | Always write `True` and `False` with capital letters |
| Not storing `input()` in a variable | The value is lost immediately | Always assign `input()` to a variable |

---

## 💡 Professional Tips

- Use f-strings instead of `+` concatenation when combining values of different types. They are cleaner and less error-prone.
- Choose meaningful variable names from the very beginning. A habit of clear naming pays off in every project.
- Convert `input()` immediately when you know you need a number. Do not wait until later in the code.
- Use `type()` actively while learning. Print the type of any value you are unsure about.
- Read error messages carefully. Python error messages tell you exactly what went wrong and on which line.
- Keep examples small and focused. Test one concept at a time before combining them.
- Comment the reason behind important decisions in your code, not just what the code does.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 2, make sure you can:

- [ ] Use `print()` to display text, variables, and calculations.
- [ ] Apply escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`, `\b`.
- [ ] Produce multi-line output using three different methods.
- [ ] Create, reuse, and update variables.
- [ ] Follow Python naming conventions and rules.
- [ ] Use `input()` to collect values from the user.
- [ ] Explain why `input()` always returns a string.
- [ ] Convert input to `int` and `float` for numeric operations.
- [ ] Use f-strings to produce formatted output.
- [ ] Distinguish between hard-coded and dynamic values.
- [ ] Identify the type of any value using `type()`.
- [ ] Explain the difference between `None`, `""`, and `"  "`.
- [ ] Explain what dynamic typing means in Python.
- [ ] Build the Interactive Profile Card mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 2 when they can:

1. Run all four chapter files without errors.
2. Explain the purpose and output of every print statement in each file.
3. Modify examples with different values and predict the results correctly.
4. Complete all five practice challenges independently.
5. Build the mini project without referring to the starter code.
6. Explain why type conversion is necessary when using `input()` for calculations.
7. Identify the data type of any value without running `type()`.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 2 — Python Strings

Chapter 2 builds directly on this foundation. Since strings are introduced in Chapter 1, the next chapter goes deeper into everything that can be done with text: transforming it, slicing it, searching inside it, cleaning it, and validating it. Every string method in Chapter 2 depends on the variable and output skills built here.

---

## 📚 Additional Resources

- [Python Official Documentation — Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python Official Documentation — Standard Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 — Python Style Guide](https://peps.python.org/pep-0008/)
- [Real Python — Python Variables](https://realpython.com/python-variables/)
- [Real Python — Python Input and Output](https://realpython.com/python-input-output/)

---

<p align="center">
  <strong>Chapter 1 Complete — Python Fundamentals ✅</strong>
</p>

<p align="center">
  <a href="../README.md">Main README</a> ·
  <a href="../02_strings/README.md">Next Chapter: Python Strings →</a>
</p>
