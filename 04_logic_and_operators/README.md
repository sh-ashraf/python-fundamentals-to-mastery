# Chapter 4 — Python Logic and Operators

<p align="center">
  <strong>Build the decision-making foundation that every Python program depends on.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-04-orange" alt="Chapter 04">
  <img src="https://img.shields.io/badge/Focus-Logic%20%26%20Operators-purple" alt="Focus: Logic and Operators">
</p>

---

## 📌 Chapter Overview

This chapter introduces the logical foundation of Python programming. Before a program can make decisions, it needs a way to evaluate conditions and produce true or false results. That is exactly what this chapter teaches.

The chapter moves from understanding boolean values as a data type, to comparing values using operators, to combining multiple conditions using logical operators, and finally to checking membership in collections and identity in memory.

Every concept in this chapter feeds directly into Chapter 5 (Conditionals), where the learner will use these tools to control program behavior.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Explain what boolean values are and how Python produces them.
- Convert any value to boolean using `bool()` and predict the result.
- Identify truthy and falsy values in Python.
- Use `any()` and `all()` to evaluate lists of conditions.
- Use `isinstance()` to verify value types at runtime.
- Compare values using all six comparison operators.
- Combine conditions using `and`, `or`, and `not`.
- Understand and apply operator precedence correctly.
- Use parentheses to control the order of logical evaluation.
- Check membership in strings, lists, tuples, and dictionaries using `in` and `not in`.
- Distinguish between value equality (`==`) and object identity (`is`).
- Apply best practices when checking for `None`.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners who want to understand how Python makes decisions |
| Logic learners | Learners who need to understand conditions before working with if statements |
| Data learners | Learners preparing for data validation, filtering, and conditional processing |
| Review learners | Learners who want to solidify their understanding of Python operators |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Declare and use variables.
- Work with basic Python data types: `int`, `float`, `str`, `bool`, `None`.
- Use `print()` and f-strings.
- Understand what a function is and how to call it.
- Complete Chapters 1, 2, and 3 of this series.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from understanding boolean values as a concept to applying logical thinking in real validation scenarios.

```text
Boolean Values (True / False)
            ↓
Boolean Conversion with bool()
            ↓
Truthy and Falsy Values
            ↓
Boolean Functions: any(), all(), isinstance()
            ↓
Comparison Operators: ==, !=, >, <, >=, <=
            ↓
Logical Operators: and, or, not
            ↓
Operator Precedence and Parentheses
            ↓
Membership Operators: in, not in
            ↓
Identity Operators: is, is not
            ↓
Practical Validation and Security Checks
```

This sequence is intentional:

1. The learner first understands what True and False mean as values.
2. Then the learner learns how Python converts any value into a boolean.
3. Then the learner uses boolean functions to evaluate groups of values.
4. Then the learner compares individual values with comparison operators.
5. Then the learner combines multiple comparisons with logical operators.
6. Then the learner learns how precedence affects results and how to control it.
7. Finally, the learner checks for membership and identity in more advanced scenarios.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_boolean_functions.py` | Boolean Values and Functions | Understanding True, False, truthy/falsy, bool(), any(), all(), isinstance() |
| 02 | `02_comparison_and_logical_operators.py` | Comparison and Logical Operators | Comparing values, combining conditions, operator precedence |
| 03 | `03_membership_and_identity_operators.py` | Membership and Identity Operators | Checking existence in collections, comparing object identity |

---

## 🧭 Recommended Study Order

### 1. Start with Boolean Values

**File:** `01_boolean_functions.py`

Start with boolean values because everything else in this chapter depends on producing and evaluating True and False. Before comparing values or combining conditions, the learner needs to understand what a boolean is and how Python generates one.

The learner studies:

- `True` and `False` as Python values
- `bool()` for explicit conversion
- Truthy and falsy rules
- `any()` for flexible validation
- `all()` for strict validation
- `isinstance()` for type-safe checks

---

### 2. Move to Comparison and Logical Operators

**File:** `02_comparison_and_logical_operators.py`

After understanding boolean values, the learner is ready to produce them by comparing values and combining conditions. This file introduces the full set of comparison and logical operators and explains how they interact through precedence rules.

The learner studies:

- All six comparison operators
- Comparing numbers and strings
- Chained comparisons
- `and`, `or`, `not` with truth tables
- Operator precedence: `not` before `and` before `or`
- Using parentheses to control evaluation
- Real validation challenges combining multiple operators

---

### 3. Finish with Membership and Identity

**File:** `03_membership_and_identity_operators.py`

Once the learner can evaluate and combine conditions, the final file introduces two more operator categories that extend boolean thinking to collections and memory. This file also clarifies the important distinction between value equality and object identity.

The learner studies:

- `in` and `not in` across strings, lists, tuples, and dictionaries
- `is` and `is not` for memory identity
- The difference between `==` and `is`
- Why `is None` is preferred over `== None`
- The difference between `None` and `""`

---

## 🧱 Lesson Breakdown

### Lesson 1 — Boolean Values and Functions

**File:** `01_boolean_functions.py`

This lesson establishes the concept of boolean logic in Python. The learner discovers that every value in Python can be evaluated as either true or false, and that Python provides several built-in tools for working with boolean results.

#### Key Concepts

- `True` and `False` as the only boolean values
- `bool()` converts any value to a boolean
- Truthy values: non-zero numbers, non-empty strings, non-empty collections
- Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `()`, `None`, `False`
- `any()` returns `True` if at least one item is truthy
- `all()` returns `True` only if all items are truthy
- `isinstance()` checks the type of a value at runtime
- `bool` is a subclass of `int`: `True == 1`, `False == 0`

#### Example

```python
# Truthy and falsy
print(bool(0))       # False
print(bool("hello")) # True
print(bool([]))      # False
print(bool(None))    # False

# any() and all()
fields = ["baraa@gmail.com", "0176-123456", ""]
print(any(fields))   # True  - at least one field is filled
print(all(fields))   # False - not all fields are filled

# isinstance()
print(isinstance(42, int))          # True
print(isinstance(42, (int, float))) # True
```

#### Why This Lesson Matters

Most programs need to evaluate conditions before doing anything. Understanding boolean values and truthy/falsy rules gives the learner a mental model for how Python decides what is considered valid or meaningful, which is the basis for all conditional logic.

---

### Lesson 2 — Comparison and Logical Operators

**File:** `02_comparison_and_logical_operators.py`

This lesson teaches the learner how to produce boolean results by comparing values and how to build complex conditions by combining multiple comparisons.

#### Key Concepts

- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`
- String comparison is alphabetical and case-sensitive
- `=` assigns, `==` compares
- Chained comparisons: `18 <= age <= 30`
- `and`: both must be True
- `or`: at least one must be True
- `not`: inverts the result
- Precedence order: `not` → `and` → `or`
- Parentheses override precedence

#### Example

```python
# Comparison
age = 25
print(18 <= age <= 30)   # True

# Logical operators
email = True
password = False
print(email and password) # False - both must be True

# Precedence
X, Y, Z = 5, 8, 6
print(X == 5 or Y > 5 and Z < 4)       # True  (and evaluated first)
print((X == 5 or Y > 5) and Z < 4)     # False (parentheses change order)
```

#### Why This Lesson Matters

Comparison and logical operators are used in every program that makes a decision. Without them, a program cannot check if a user is old enough, if a password is valid, or if a system is under pressure. This lesson gives the learner the tools to build those conditions correctly.

---

### Lesson 3 — Membership and Identity Operators

**File:** `03_membership_and_identity_operators.py`

This lesson extends boolean logic to searching within collections and comparing object identity in memory. It also clarifies one of the most misunderstood distinctions in Python: the difference between `==` and `is`.

#### Key Concepts

- `in`: checks if a value exists in a string, list, tuple, set, or dictionary
- `not in`: checks if a value is absent
- `in` on a dictionary checks keys, not values
- `is`: checks if two variables point to the same object in memory
- `is not`: checks if they are different objects
- `==` compares values, `is` compares identity
- Python caches small integers, which can make `is` return `True` unexpectedly
- Best practice: use `is None` and `is not None`, not `== None`

#### Example

```python
# Membership
banned = ["spam.com", "fake.org"]
domain = "gmail.com"
print(domain not in banned)   # True - safe domain

# Identity vs equality
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)   # True  - same values
print(x is y)   # False - different objects in memory

# None check
email = None
print(email is not None)   # False - best practice for None check
```

#### Why This Lesson Matters

Membership operators are essential for data filtering, search features, and security checks. Identity operators help the learner understand how Python manages memory and avoid subtle bugs when checking for `None`. These are skills that appear constantly in real Python code.

---

## 🧠 Core Concepts Summary

| Concept | Description | Example |
|---|---|---|
| Boolean values | Two possible values: True or False | `x = True` |
| bool() | Converts any value to boolean | `bool(0)` → `False` |
| Truthy value | Any value Python evaluates as True | `bool("hi")` → `True` |
| Falsy value | Any value Python evaluates as False | `bool([])` → `False` |
| any() | True if at least one item is truthy | `any(["", "hi", ""])` → `True` |
| all() | True if all items are truthy | `all(["hi", ""])` → `False` |
| isinstance() | Checks value type at runtime | `isinstance(5, int)` → `True` |
| Comparison operator | Compares two values, returns bool | `10 > 5` → `True` |
| Logical and | Both must be True | `True and False` → `False` |
| Logical or | At least one must be True | `True or False` → `True` |
| Logical not | Inverts the boolean | `not True` → `False` |
| in | Checks existence in collection | `"@" in email` |
| not in | Checks absence from collection | `domain not in banned` |
| is | Checks same object in memory | `value is None` |
| is not | Checks different objects | `value is not None` |

---

## 📋 Reference Tables

### Boolean Functions

| Function | Purpose | Returns | Example |
|---|---|---|---|
| `bool(x)` | Convert to boolean | `bool` | `bool(0)` → `False` |
| `any(iterable)` | True if any item is truthy | `bool` | `any(["", "hi"])` → `True` |
| `all(iterable)` | True if all items are truthy | `bool` | `all(["hi", ""])` → `False` |
| `isinstance(x, t)` | Check if x is type t | `bool` | `isinstance(5, int)` → `True` |

### Truthy and Falsy Values

| Falsy Values | Truthy Values |
|---|---|
| `False` | `True` |
| `None` | Any non-zero number |
| `0`, `0.0` | Any non-empty string |
| `""` (empty string) | Any non-empty list |
| `[]` (empty list) | Any non-empty dictionary |
| `{}` (empty dictionary) | Any non-empty tuple |
| `()` (empty tuple) | Any non-empty set |

### Comparison Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `7 > 3` | `True` |
| `<` | Less than | `3 < 7` | `True` |
| `>=` | Greater than or equal | `7 >= 7` | `True` |
| `<=` | Less than or equal | `3 <= 7` | `True` |

### Logical Operators

| Operator | Meaning | Truth Table Summary | Example |
|---|---|---|---|
| `and` | Both must be True | T and T → T, anything else → F | `age >= 18 and has_id` |
| `or` | At least one must be True | F and F → F, anything else → T | `is_admin or is_editor` |
| `not` | Inverts the value | not T → F, not F → T | `not is_banned` |

### Operator Precedence (High to Low)

| Priority | Operator | Evaluated |
|---|---|---|
| 1 (highest) | `not` | First |
| 2 | `and` | Second |
| 3 (lowest) | `or` | Last |

### Membership and Identity Operators

| Operator | Purpose | Example | Result |
|---|---|---|---|
| `in` | Value exists in collection | `"@" in email` | `True` |
| `not in` | Value absent from collection | `"x" not in "abc"` | `True` |
| `is` | Same object in memory | `value is None` | depends |
| `is not` | Different object in memory | `value is not None` | depends |

---

## 🧪 Practice Challenges

### Challenge 1 — Falsy Value Explorer

Predict the output before running.

Write a program that tests several values with `bool()` and prints each result. Include: `0`, `1`, `""`, `"text"`, `[]`, `[0]`, `None`, `False`, `True`.

Expected output format:

```text
bool(0)      → False
bool(1)      → True
bool("")     → False
bool("text") → True
```

---

### Challenge 2 — Registration Validator

Build a simple form validator that checks two scenarios:

- Flexible registration: at least one contact method (email or phone or username) is provided.
- Strict registration: all three contact methods are provided.

Test with incomplete data and complete data and display the result for each case.

Expected output:

```text
Flexible check (any): True
Strict check (all): False
```

---

### Challenge 3 — Age and Access Validator

Check whether a user qualifies for a service based on age and membership status.

Requirements:

- Age must be between 18 and 65 (inclusive) using a chained comparison.
- User must be either a member or have a guest pass.
- User must not be banned.

```python
age = 30
is_member = False
has_guest_pass = True
is_banned = False
```

Expected output:

```text
Access granted: True
```

---

### Challenge 4 — Security Domain Check

Write a program that checks whether a user's email domain is safe to use.

Requirements:

- Extract the domain from the email address using string methods.
- Check if the domain is not in a banned list.
- Check if the domain ends with `.com` or `.org`.
- Display whether the email passes both checks.

```python
email = "user@gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
```

Expected output:

```text
Domain: gmail.com
Not banned: True
Trusted extension: True
Email is valid: True
```

---

### Challenge 5 — Authorization System

Build a multi-condition authorization system.

Requirements:

- The user must be an admin or moderator.
- The user must not be banned, or must have a verified email.
- Use parentheses to ensure correct precedence.
- Print the result and explain which condition passed or failed.

```python
is_admin = True
is_moderator = False
is_banned = False
has_verified_email = True
```

Expected output:

```text
Role check: True
Ban/Verification check: True
Authorized: True
```

---

## 🏗️ Mini Project — User Validation Engine

### Project Goal

Build a complete validation engine that checks whether a new user registration is valid by evaluating multiple conditions across all chapter topics.

### Requirements

The program should validate:

- Name: not empty and contains only letters
- Age: between 13 and 120 (inclusive)
- Email: not None, not empty, contains `@`, ends with `.com` or `.org`
- Password: at least 8 characters, contains no spaces
- Domain: not in the banned list

The program should display a validation report showing each check individually and a final result.

### Starter Code

```python
# User Registration Validation Engine

name = "Alice"
age = 25
email = "alice@gmail.com"
password = "Secure123"
banned_domains = ["spam.com", "fake.org", "bot.net"]

# --- Validation Checks ---

# Name
name_valid = isinstance(name, str) and name != "" and name.isalpha()

# Age
age_valid = isinstance(age, int) and 13 <= age <= 120

# Email
domain = email.split("@")[-1] if "@" in email else ""
email_valid = (
    email is not None
    and email != ""
    and "@" in email
    and email.endswith((".com", ".org"))
    and domain not in banned_domains
)

# Password
password_valid = len(password) >= 8 and " " not in password

# Final result
all_valid = all([name_valid, age_valid, email_valid, password_valid])

# --- Report ---
print("=" * 40)
print("     USER VALIDATION REPORT")
print("=" * 40)
print(f"Name valid:     {name_valid}")
print(f"Age valid:      {age_valid}")
print(f"Email valid:    {email_valid}")
print(f"Password valid: {password_valid}")
print("=" * 40)
print(f"Registration:   {'APPROVED' if all_valid else 'REJECTED'}")
print("=" * 40)
```

### Expected Output

```text
========================================
     USER VALIDATION REPORT
========================================
Name valid:     True
Age valid:      True
Email valid:    True
Password valid: True
========================================
Registration:   APPROVED
========================================
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Writing `true` or `false` in lowercase | Python raises a `NameError` | Always write `True` and `False` with capital letters |
| Using `==` to check for `None` | Can produce unexpected results depending on context | Use `is None` or `is not None` |
| Confusing `=` with `==` | `=` assigns a value, `==` compares values | Use `==` inside conditions |
| Ignoring operator precedence | `and` evaluates before `or`, which can change results silently | Use parentheses to make logic explicit |
| Assuming `is` compares values | `is` compares memory identity, not value equality | Use `==` for value comparison |
| Forgetting that `in` checks keys in dictionaries | May produce unexpected False results when searching for values | Use `.values()` to search values: `value in d.values()` |
| Treating `None` and `""` as the same | They represent different situations and behave differently | `None` means missing, `""` means empty |
| Using `any()` or `all()` on a non-iterable | Raises a `TypeError` | Always pass a list or other iterable |

---

## 💡 Professional Tips

- Always use parentheses when combining `and` and `or` in the same expression. It removes ambiguity and prevents bugs.
- Prefer `is None` over `== None`. It is the recommended style in Python (PEP 8) and avoids edge cases.
- Use `any()` and `all()` to replace long chains of `or` and `and` conditions on collections.
- Use `isinstance(x, (int, float))` with a tuple to check for multiple types at once.
- When using `in` with a dictionary, remember it checks keys. Use `.values()` or `.items()` when needed.
- Do not rely on `is` for comparing strings or numbers unless you specifically need identity checking.
- Use chained comparisons like `18 <= age <= 65` instead of `age >= 18 and age <= 65` for cleaner code.
- Comment complex boolean expressions to explain the intent, not just the operators.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 5, make sure you can:

- [ ] Explain what `True` and `False` represent as Python values.
- [ ] Predict the result of `bool()` on any given value.
- [ ] List all falsy values in Python from memory.
- [ ] Use `any()` and `all()` to evaluate a list of conditions.
- [ ] Use `isinstance()` to check a value's type before processing it.
- [ ] Use all six comparison operators correctly.
- [ ] Explain why `"a" == "A"` returns `False`.
- [ ] Use `and`, `or`, and `not` to build compound conditions.
- [ ] Explain operator precedence and demonstrate how parentheses change results.
- [ ] Use `in` and `not in` to search across different collection types.
- [ ] Explain the difference between `==` and `is` with a practical example.
- [ ] Use `is not None` correctly when validating optional values.
- [ ] Explain the difference between `None` and `""`.
- [ ] Build the User Validation Engine mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 5 when they can:

1. Run all three chapter files without errors.
2. Explain the output of every print statement in each file.
3. Modify the challenges with different input values and predict the results correctly.
4. Build the mini project independently without referring to the starter code.
5. Identify bugs in boolean logic caused by operator precedence or incorrect use of `is`.
6. Write a multi-condition validation check using comparison, logical, and membership operators together.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 5 — Python Conditional Statements

Chapter 5 uses everything learned in this chapter. The comparison and logical operators become the conditions inside `if`, `elif`, and `else` blocks. The boolean results from membership and identity checks drive the flow of program execution. Without this chapter, conditional statements would have no foundation.

---

## 📚 Additional Resources

- [Python Official Documentation — Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
- [Python Official Documentation — Comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons)
- [Python Official Documentation — Built-in Functions: any, all, bool, isinstance](https://docs.python.org/3/library/functions.html)
- [PEP 8 — Programming Recommendations for None Comparisons](https://peps.python.org/pep-0008/#programming-recommendations)
- [Real Python — Python Booleans](https://realpython.com/python-boolean/)

---

<p align="center">
  <strong>Chapter 4 Complete — Python Logic and Operators ✅</strong>
</p>

<p align="center">
  <a href="../03_numbers/README.md">← Previous Chapter: Python Numbers</a> ·
  <a href="../README.md">Main README</a> ·
  <a href="../05_conditionals/README.md">Next Chapter: Python Conditionals →</a>
</p>
