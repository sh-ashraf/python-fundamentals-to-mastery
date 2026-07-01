# Chapter 2 — Python Strings

<p align="center">
  <strong>Master the most common data type in Python and learn to manipulate, clean, and validate text like a professional.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-02-orange" alt="Chapter 02">
  <img src="https://img.shields.io/badge/Focus-Strings-purple" alt="Focus: Strings">
</p>

---

## 📌 Chapter Overview

This chapter focuses on strings, which are the most frequently used data type in Python. Every program that communicates with a user, reads a file, processes a form, or cleans data depends on string operations.

The chapter moves from understanding what a string is and how to measure and transform it, to accessing specific characters and extracting parts of it, to searching inside it and validating its content. Each lesson builds directly on the previous one, and together they give the learner the ability to handle real-world text data with confidence.

By the end of this chapter, the learner will be able to clean messy input, extract meaningful parts from structured text, validate user-submitted data, and format output professionally.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Check and convert string types using `type()` and `str()`.
- Measure string length with `len()` and count occurrences with `count()`.
- Transform strings using `replace()`, concatenation, f-strings, `split()`, and repetition.
- Access individual characters using positive and negative indexing.
- Extract substrings using slicing syntax `[start:end:step]`.
- Reverse strings and extract every nth character using step slicing.
- Remove unwanted whitespace using `strip()`, `lstrip()`, and `rstrip()`.
- Detect and count extra spaces by comparing lengths before and after stripping.
- Convert case using `lower()` and `upper()` for consistent comparisons.
- Search for patterns using `startswith()`, `endswith()`, `find()`, and the `in` operator.
- Validate string content using `isalpha()` and `isnumeric()`.
- Combine multiple string methods to clean, extract, and validate real-world data.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners who have completed Chapter 1 and are ready to work with text |
| Data learners | Learners preparing for data cleaning, parsing, and preprocessing tasks |
| Programming beginners | Learners who want to understand how Python handles and manipulates text |
| Review learners | Learners who want a structured refresher on Python string operations |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Create and use variables.
- Use `print()` and f-strings for output.
- Understand what a data type is and how to use `type()`.
- Complete Chapter 1 of this series.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from understanding strings as a data type to applying multiple methods together in real validation and cleaning scenarios.

```text
String Types and Measurement (type, str, len, count)
                    ↓
String Transformations (replace, concatenation, f-strings, split, repetition)
                    ↓
String Indexing (positive and negative index access)
                    ↓
String Slicing (start, end, step extraction)
                    ↓
Whitespace Cleaning (strip, lstrip, rstrip)
                    ↓
Case Conversion (lower, upper)
                    ↓
String Search (startswith, endswith, in, find)
                    ↓
String Validation (isalpha, isnumeric)
                    ↓
Combined Validation and Cleaning
```

This sequence is intentional:

1. The learner first understands strings as values that can be measured and typed.
2. Then the learner transforms and formats strings for output.
3. Then the learner accesses and extracts parts of strings.
4. Then the learner cleans strings by removing unwanted characters.
5. Finally, the learner searches and validates strings to make decisions based on content.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_string_basics_and_transformations.py` | Types, Measurement, Transformations | `type()`, `str()`, `len()`, `count()`, `replace()`, f-strings, `split()`, concatenation |
| 02 | `02_string_indexing_and_slicing.py` | Indexing, Slicing, Cleaning | `[index]`, `[start:end:step]`, `strip()`, `lstrip()`, `rstrip()` |
| 03 | `03_string_search_and_validation.py` | Search, Validation, Case | `lower()`, `upper()`, `startswith()`, `endswith()`, `find()`, `in`, `isalpha()`, `isnumeric()` |

---

## 🧭 Recommended Study Order

### 1. Start with String Basics and Transformations

**File:** `01_string_basics_and_transformations.py`

Start here because strings must be understood as a type before they can be manipulated. This file covers what a string is, how to measure and count its contents, and how to transform it into something more useful.

The learner studies:

- `type()` and `str()` for type checking and conversion
- `len()` for character count
- `count()` for frequency checking
- `replace()` for text cleaning and reformatting
- String concatenation with `+`
- f-strings for clean formatted output
- `split()` for breaking strings into parts
- String repetition with `*`

---

### 2. Move to Indexing, Slicing, and Cleaning

**File:** `02_string_indexing_and_slicing.py`

After knowing how to transform strings, the learner is ready to access specific parts of them. This file teaches character-level access and substring extraction, then introduces whitespace cleaning as a practical extension of slicing knowledge.

The learner studies:

- Positive and negative indexing
- Slicing syntax: `[start:end:step]`
- Leaving start or end empty
- Reversing strings with `[::-1]`
- Extracting every nth character
- `lstrip()`, `rstrip()`, and `strip()`
- Removing custom characters with `strip(char)`
- Detecting whitespace issues by comparing lengths

---

### 3. Finish with Search, Validation, and Case Conversion

**File:** `03_string_search_and_validation.py`

Once the learner can transform and extract from strings, the final file teaches how to search inside them and validate their content. Case conversion is introduced here as a prerequisite for reliable searching.

The learner studies:

- `lower()` and `upper()` for consistent comparison
- `startswith()` and `endswith()` for prefix and suffix checks
- The `in` operator for existence checks
- `find()` for locating substrings dynamically
- `isalpha()` for letter-only validation
- `isnumeric()` for digit-only validation
- Combining methods for multi-condition validation

---

## 🧱 Lesson Breakdown

### Lesson 1 — String Basics and Transformations

**File:** `01_string_basics_and_transformations.py`

This lesson introduces strings as a measurable, transformable data type. The learner discovers the full range of methods available for changing, combining, and restructuring text values.

#### Key Concepts

- `type()` confirms a value is a string
- `str()` converts integers and floats to string for concatenation
- `len()` counts every character including spaces
- `count()` is case-sensitive and counts substring occurrences
- `replace(old, new)` can clean, reformat, or remove text
- `replace()` can be chained for multiple substitutions
- Concatenation joins strings with `+`
- f-strings embed variables and expressions directly inside text
- `split(sep)` breaks a string into a list of parts
- `string * n` repeats a string n times

#### Example

```python
# Measure and count
password = "123a123"
print(len(password))        # Output: 7
print(len(password) < 8)    # Output: True

# Transform
price = "$1,299.99"
clean = price.replace("$", "").replace(",", "")
print(clean)                # Output: 1299.99

# Format
name = "Sam"
age = 34
print(f"My name is {name}, I am {age} years old.")
# Output: My name is Sam, I am 34 years old.

# Split
date = "2026-09-20"
print(date.split("-"))      # Output: ['2026', '09', '20']
```

#### Why This Lesson Matters

String transformation is the foundation of data cleaning. Every dataset contains text that needs to be reformatted, standardized, or split before it can be used. The methods in this lesson appear constantly in data engineering, web development, and automation.

---

### Lesson 2 — Indexing, Slicing, and Cleaning

**File:** `02_string_indexing_and_slicing.py`

This lesson teaches the learner to access and extract precise parts of a string by position. It also introduces whitespace cleaning as an essential skill for handling real-world input.

#### Key Concepts

- Positive index: `string[0]` is the first character
- Negative index: `string[-1]` is the last character
- Slicing: `string[start:end]` is exclusive at end
- Omitting start: `string[:4]` starts from beginning
- Omitting end: `string[3:]` goes to the end
- Step: `string[::2]` extracts every second character
- Reverse: `string[::-1]` reverses the string
- `lstrip()` removes leading spaces
- `rstrip()` removes trailing spaces
- `strip()` removes spaces from both ends
- `strip(chars)` removes specific characters

#### Example

```python
text = "python"

# Indexing
print(text[0])      # Output: p
print(text[-1])     # Output: n

# Slicing
date = "2026-09-20"
print(date[:4])     # Output: 2026
print(date[5:7])    # Output: 09
print(date[8:])     # Output: 20
print(date[::-1])   # Output: 02-90-6202

# Whitespace detection
raw = "    Engineering"
print(len(raw))             # Output: 15
print(len(raw.strip()))     # Output: 11
spaces = len(raw) - len(raw.strip())
print("Spaces found:", spaces)  # Output: Spaces found: 4
```

#### Why This Lesson Matters

Indexing and slicing allow the learner to extract structured data from strings without external libraries. Dates, codes, phone numbers, and identifiers all follow patterns that can be extracted by position. Whitespace cleaning is equally critical because unclean input is one of the most common sources of bugs in programs that process user data.

---

### Lesson 3 — Search, Validation, and Case Conversion

**File:** `03_string_search_and_validation.py`

This lesson completes the chapter by teaching the learner to search inside strings and verify that their content meets specific requirements. Case conversion is introduced as a necessary first step before reliable searching.

#### Key Concepts

- `lower()` and `upper()` standardize text before comparison
- `startswith(sub)` checks prefix
- `endswith(sub)` checks suffix, including tuple of options
- `in` checks for substring existence anywhere in the string
- `find(sub)` returns position or `-1` if not found
- `find()` combined with slicing enables dynamic extraction
- `isalpha()` returns True only for letter-only strings
- `isnumeric()` returns True only for digit-only strings
- All search methods are case-sensitive

#### Example

```python
# Case conversion before comparison
search = "Email".lower().strip()
data = "emAil".lower().strip()
print(search == data)   # Output: True

# Search
email = "user@gmail.com"
print("@" in email)                     # Output: True
print(email.endswith(".com"))           # Output: True
print(email.find("@"))                  # Output: 4

# Dynamic extraction with find()
phone = "+48-176-12345"
print(phone[phone.find("-") + 1:])     # Output: 176-12345

# Validation
print("Egypt".isalpha())               # Output: True
print("01234".isnumeric())             # Output: True
print("Egypt1".isalpha())              # Output: False
```

#### Why This Lesson Matters

Search and validation are the basis of form handling, input sanitization, and data quality checks. Every application that accepts user input needs to verify that the data is in the correct format before processing it. The methods in this lesson make that possible without external libraries.

---

## 🧠 Core Concepts Summary

| Concept | Method or Syntax | Description | Example |
|---|---|---|---|
| Type check | `type(x)` | Returns the type of a value | `type("hi")` → `<class 'str'>` |
| Convert to string | `str(x)` | Converts value to string | `str(25)` → `"25"` |
| Length | `len(s)` | Counts all characters | `len("hello")` → `5` |
| Count occurrences | `s.count(x)` | Counts substring appearances | `"aab".count("a")` → `2` |
| Replace | `s.replace(old, new)` | Swaps or removes text | `"hi".replace("i", "o")` → `"ho"` |
| Concatenation | `s1 + s2` | Joins two strings | `"py" + "thon"` → `"python"` |
| f-string | `f"{var}"` | Embeds variables in text | `f"age: {25}"` |
| Split | `s.split(sep)` | Breaks into list | `"a,b".split(",")` → `['a','b']` |
| Repetition | `s * n` | Repeats string | `"ha" * 3` → `"hahaha"` |
| Indexing | `s[i]` | Accesses character at position | `"abc"[0]` → `"a"` |
| Slicing | `s[start:end:step]` | Extracts substring | `"python"[:3]` → `"pyt"` |
| Strip | `s.strip()` | Removes leading/trailing spaces | `" hi ".strip()` → `"hi"` |
| Lowercase | `s.lower()` | Converts to lowercase | `"HI".lower()` → `"hi"` |
| Uppercase | `s.upper()` | Converts to uppercase | `"hi".upper()` → `"HI"` |
| Starts with | `s.startswith(x)` | Checks prefix | `"abc".startswith("a")` → `True` |
| Ends with | `s.endswith(x)` | Checks suffix | `"abc".endswith("c")` → `True` |
| Search | `x in s` | Checks substring existence | `"@" in email` → `True` |
| Find position | `s.find(x)` | Returns index or -1 | `"abc".find("b")` → `1` |
| Letters only | `s.isalpha()` | True if only letters | `"abc".isalpha()` → `True` |
| Digits only | `s.isnumeric()` | True if only digits | `"123".isnumeric()` → `True` |

---

## 📋 Reference Tables

### String Transformation Methods

| Method | Purpose | Example | Result |
|---|---|---|---|
| `s.replace(old, new)` | Swap or remove text | `"a-b".replace("-", "")` | `"ab"` |
| `s.split(sep)` | Break into list | `"a,b,c".split(",")` | `['a','b','c']` |
| `str(x)` | Convert to string | `str(42)` | `"42"` |
| `s * n` | Repeat string | `"-" * 5` | `"-----"` |
| `s1 + s2` | Join strings | `"py" + "thon"` | `"python"` |

### Slicing Reference

| Syntax | Meaning | Example | Result |
|---|---|---|---|
| `s[i]` | Character at index i | `"abc"[1]` | `"b"` |
| `s[-i]` | Character from end | `"abc"[-1]` | `"c"` |
| `s[start:end]` | Substring (end excluded) | `"python"[1:4]` | `"yth"` |
| `s[:end]` | From beginning to end | `"python"[:3]` | `"pyt"` |
| `s[start:]` | From start to end | `"python"[3:]` | `"hon"` |
| `s[::step]` | Every nth character | `"python"[::2]` | `"pto"` |
| `s[::-1]` | Reversed string | `"python"[::-1]` | `"nohtyp"` |

### Whitespace Cleaning Methods

| Method | Removes From | Custom Characters | Example |
|---|---|---|---|
| `s.lstrip()` | Left side only | No | `"  hi".lstrip()` → `"hi"` |
| `s.rstrip()` | Right side only | No | `"hi  ".rstrip()` → `"hi"` |
| `s.strip()` | Both sides | No | `"  hi  ".strip()` → `"hi"` |
| `s.strip(chars)` | Both sides | Yes | `"##hi##".strip("#")` → `"hi"` |

### Search and Validation Methods

| Method | Purpose | Returns | Case Sensitive |
|---|---|---|---|
| `s.startswith(x)` | Check prefix | `bool` | Yes |
| `s.endswith(x)` | Check suffix | `bool` | Yes |
| `x in s` | Check existence | `bool` | Yes |
| `s.find(x)` | Find position | `int` (-1 if not found) | Yes |
| `s.lower()` | To lowercase | `str` | — |
| `s.upper()` | To uppercase | `str` | — |
| `s.isalpha()` | Letters only | `bool` | — |
| `s.isnumeric()` | Digits only | `bool` | — |

---

## 🧪 Practice Challenges

### Challenge 1 — Phone Number Formatter

Write a program that takes a messy phone number and produces a clean digit-only string.

Requirements:

- Start with: `"+49 (176) 123-4567"`
- Remove `+`, spaces, parentheses, and hyphens
- Replace `+` with `"00"`
- Display the clean result

Expected output:

```text
0049176123456
```

---

### Challenge 2 — Date Parser

Write a program that extracts the year, month, and day from a date string using slicing.

Requirements:

- Start with: `"2026-09-20"`
- Extract each part using `[start:end]` slicing
- Display each part on a separate line with a label

Expected output:

```text
Year:  2026
Month: 09
Day:   20
```

---

### Challenge 3 — Input Cleaner

Write a program that receives a messy string and produces a cleaned version.

Requirements:

- Strip leading and trailing whitespace
- Convert to lowercase
- Count the number of spaces that were removed
- Display the result and the space count

Input:

```text
"   Python PROGRAMMING   "
```

Expected output:

```text
Cleaned: python programming
Spaces removed: 6
```

---

### Challenge 4 — Email Validator

Write a program that validates an email address using multiple string methods.

Requirements:

- Check that the email is not empty
- Check that it contains exactly one `@`
- Check that it ends with `.com` or `.org`
- Check that the domain is not in a banned list
- Display a result for each check and a final verdict

```python
email = "user@gmail.com"
banned = ["spam.com", "fake.org"]
```

Expected output:

```text
Not empty:        True
Contains @:       True
Valid extension:  True
Domain not banned: True
Email is valid:   True
```

---

### Challenge 5 — Data Row Parser

Write a program that parses a messy CSV-style data row, cleans each field, and displays the result.

Requirements:

- Start with: `"  Alice  ,  engineer  ,  cairo  "`
- Split by comma
- Strip each part
- Convert to lowercase
- Display labeled output

Expected output:

```text
Name:  alice
Role:  engineer
City:  cairo
```

---

## 🏗️ Mini Project — Contact Data Cleaner

### Project Goal

Build a program that receives raw contact data, cleans every field, validates the result, and displays a structured contact card.

### Requirements

The program must:

- Accept a name, email, and phone number as strings.
- Strip whitespace from all fields.
- Convert name and email to lowercase.
- Validate the name contains only letters.
- Validate the email contains `@` and ends with `.com` or `.org`.
- Validate the phone contains only digits.
- Display a contact card showing cleaned values and validation results.

### Starter Code

```python
# Raw input data
raw_name  = "  ALICE  "
raw_email = "  Alice@Gmail.COM  "
raw_phone = "0123456789"

# Clean
name  = raw_name.strip().lower()
email = raw_email.strip().lower()
phone = raw_phone.strip()

# Validate
name_valid  = name.isalpha()
email_valid = "@" in email and email.endswith((".com", ".org"))
phone_valid = phone.isnumeric() and len(phone) == 10

# Display
print("=" * 40)
print("         CONTACT CARD")
print("=" * 40)
print(f"Name:  {name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print("=" * 40)
print("Validation:")
print(f"Name valid:  {name_valid}")
print(f"Email valid: {email_valid}")
print(f"Phone valid: {phone_valid}")
print("=" * 40)
all_valid = all([name_valid, email_valid, phone_valid])
print(f"Contact:     {'APPROVED' if all_valid else 'REJECTED'}")
print("=" * 40)
```

### Expected Output

```text
========================================
         CONTACT CARD
========================================
Name:  alice
Email: alice@gmail.com
Phone: 0123456789
========================================
Validation:
Name valid:  True
Email valid: True
Phone valid: True
========================================
Contact:     APPROVED
========================================
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Forgetting that strings are immutable | Methods return new strings, not modified originals | Always assign the result: `clean = s.strip()` |
| Ignoring case before comparing | `"Email" == "email"` returns False | Always use `.lower()` or `.upper()` before comparing |
| Misunderstanding slicing end index | `s[0:4]` includes index 0, 1, 2, 3 but NOT 4 | Remember: end index is exclusive |
| Using `is` instead of `==` for string comparison | `is` checks memory identity, not value | Use `==` to compare string content |
| Not stripping user input | Extra spaces cause silent mismatches | Always call `.strip()` on input before processing |
| Assuming `find()` raises an error when not found | `find()` returns `-1` silently | Always check `if result != -1` before using the position |
| Using `isalpha()` on strings with spaces | Spaces make `isalpha()` return False | Use `.replace(" ", "")` before calling `isalpha()` if needed |
| Chaining methods without testing steps | Hard to debug when a chain fails | Test each method step by step during development |

---

## 💡 Professional Tips

- Always call `.strip()` on any string that comes from user input, a file, or a database before processing it.
- Use `.lower()` and `.strip()` together before any comparison: `s.strip().lower()`.
- Prefer f-strings over `+` concatenation. They are more readable and handle type conversion automatically.
- Use `find()` combined with slicing for dynamic extraction when the position of a separator varies.
- Use `endswith()` with a tuple to check multiple extensions at once: `f.endswith((".csv", ".xlsx"))`.
- Chain `replace()` from left to right for sequential cleaning: `s.replace(",", "").replace(" ", "")`.
- Test edge cases: empty strings, strings with only spaces, strings with special characters.
- Use `count()` to detect data quality issues before processing.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 3, make sure you can:

- [ ] Use `type()` to confirm a value is a string.
- [ ] Use `str()` to convert a number to a string for concatenation.
- [ ] Use `len()` to count characters in any string.
- [ ] Use `count()` to find how many times a substring appears.
- [ ] Use `replace()` to clean, reformat, and remove text.
- [ ] Chain multiple `replace()` calls for complex cleaning.
- [ ] Use f-strings to embed variables and expressions in text.
- [ ] Use `split()` to break a string into a list of parts.
- [ ] Access a character by its positive and negative index.
- [ ] Extract a substring using `[start:end:step]` slicing.
- [ ] Reverse a string using `[::-1]`.
- [ ] Use `strip()`, `lstrip()`, and `rstrip()` to remove whitespace.
- [ ] Remove custom characters with `strip(chars)`.
- [ ] Detect extra spaces by comparing `len()` before and after `strip()`.
- [ ] Use `lower()` and `upper()` before comparing strings.
- [ ] Use `startswith()` and `endswith()` for prefix and suffix checks.
- [ ] Use the `in` operator to check if a substring exists.
- [ ] Use `find()` to locate a substring dynamically.
- [ ] Use `isalpha()` and `isnumeric()` for content validation.
- [ ] Combine multiple methods for real-world data cleaning and validation.
- [ ] Build the Contact Data Cleaner mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 3 when they can:

1. Run all three chapter files without errors.
2. Explain the output of every print statement in each file.
3. Modify examples with different input values and predict the results correctly.
4. Complete all five practice challenges without referring to the solutions.
5. Build the mini project independently without referring to the starter code.
6. Explain the difference between indexing and slicing with a practical example.
7. Explain why case conversion must happen before string comparison.
8. Explain why `find()` returning `-1` is not an error.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 3 — Python Numbers

Chapter 3 builds on the type conversion skills introduced here. The learner already knows how to convert strings to numbers using `int()` and `float()`. Chapter 3 goes deeper into how Python handles numeric types, performs arithmetic, rounds results, generates random values, and validates numeric data.

---

## 📚 Additional Resources

- [Python Official Documentation — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python Official Documentation — Built-in Functions](https://docs.python.org/3/library/functions.html)
- [PEP 8 — String Style Recommendations](https://peps.python.org/pep-0008/)
- [Real Python — Python Strings](https://realpython.com/python-strings/)
- [Real Python — Python f-Strings](https://realpython.com/python-f-strings/)

---

<p align="center">
  <strong>Chapter 2 Complete — Python Strings ✅</strong>
</p>

<p align="center">
  <a href="../01_fundamentals/README.md">← Previous Chapter: Python Fundamentals</a> ·
  <a href="../README.md">Main README</a> ·
  <a href="../03_numbers/README.md">Next Chapter: Python Numbers →</a>
</p>
