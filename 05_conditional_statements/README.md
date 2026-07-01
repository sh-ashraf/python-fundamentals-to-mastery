# Chapter 5 — Python Conditional Statements

<p align="center">
  <strong>Learn how to give your programs the ability to make decisions, choose paths, and respond differently based on conditions.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-05-orange" alt="Chapter 05">
  <img src="https://img.shields.io/badge/Focus-Conditionals-purple" alt="Focus: Conditionals">
</p>

---

## 📌 Chapter Overview

This chapter introduces conditional statements, which are the mechanism that allows a program to make decisions. Without conditionals, every program runs the same way every time: line by line, top to bottom, with no choices. Conditionals change that. They allow a program to check a condition and choose a path based on the result.

The chapter moves from the simplest form of a decision (a standalone `if`) through two-way choices (`if/else`), multi-branch decisions (`if/elif/else`), nested conditions, logical operators inside conditions, and independent checks. It finishes with inline if expressions and the `match/case` statement, and applies all of these concepts in two real-world validation challenges.

By the end of this chapter, the learner will be able to write programs that respond intelligently to different inputs and situations.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Explain what a conditional statement is and why it matters.
- Distinguish between straight-line code and conditional code using flowcharts.
- Write standalone `if` statements for optional actions.
- Write `if/else` statements for two-outcome decisions.
- Write `if/elif/else` chains for multi-branch decisions.
- Build multi-elif chains for grading, status codes, and role-based routing.
- Use nested `if` statements for layered, step-by-step decisions.
- Combine conditions using `and` and `or` inside if statements.
- Write independent `if` blocks that always run regardless of each other.
- Write inline if expressions (ternary) for simple one-line decisions.
- Use `match/case` to match a value against multiple exact options.
- Apply conditional logic to real-world email and password validation.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners who have completed Chapter 4 and are ready to apply boolean logic |
| Programming beginners | Learners who want to understand how programs make decisions |
| Data learners | Learners preparing for data validation, rule-based filtering, and conditional processing |
| Review learners | Learners who want a structured refresher on Python decision-making |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Use comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Use logical operators: `and`, `or`, `not`.
- Understand boolean values: `True`, `False`, truthy, falsy.
- Use membership operators: `in`, `not in`.
- Complete Chapters 1 through 4 of this series.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from the simplest possible decision to the most practical and flexible forms of conditional logic.

```text
Standalone if  ("Just Checking")
        ↓
if / else  ("This or That")
        ↓
if / elif / else  ("Branching — Choose One from Many")
        ↓
Multi-elif Chains (grades, status codes, roles)
        ↓
Nested if  ("Layered Tree — Step-by-Step Decisions")
        ↓
Logical Operators inside Conditions (and, or)
        ↓
Independent if Blocks  ("Checklist Mode — Test All Conditions")
        ↓
Inline if / Ternary  ("Quick, Short, Simple Check")
        ↓
match / case  ("Pattern Matcher")
        ↓
Real Validation Challenges (email, password)
```

This sequence is intentional:

1. The learner first understands what a condition is and what the simplest check looks like.
2. Then the learner adds an alternative path with `else`.
3. Then the learner adds more paths with `elif`.
4. Then the learner nests decisions inside each other for layered logic.
5. Then the learner combines conditions with `and` and `or` for more expressive checks.
6. Then the learner learns when to keep conditions completely independent.
7. Finally, the learner applies all of this to professional-level validation programs.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_if_else_elif.py` | If, Else, Elif | Standalone if, two-way decisions, multi-branch chains, flowcharts, indentation |
| 02 | `02_nested_and_advanced_conditions.py` | Nested and Advanced Conditions | Multi-elif, nested if, logical operators in conditions, independent if blocks |
| 03 | `03_inline_if_and_match_case.py` | Inline If and Match Case | Ternary expressions, match/case, real validation challenges |

---

## 🧭 Recommended Study Order

### 1. Start with If, Else, Elif

**File:** `01_if_else_elif.py`

Start here because this file builds the entire mental model for conditional statements from scratch. The learner sees flowcharts that contrast straight-line code against conditional code, and then studies each building block one at a time with its rules.

The learner studies:

- What conditional statements are: checkpoints that run code only if a condition is True
- The difference between straight-line code and conditional code (flowchart)
- Standalone `if`: "Just Checking" — if True do this, otherwise do nothing
- `if/else`: "This or That" — always produces one of two outcomes
- `if/elif/else`: "Branching" — choose one from many, stops at first True
- Rules for `if`, `elif`, and `else` (when each can be used and how many are allowed)
- Python indentation as the mechanism that defines code blocks

---

### 2. Move to Nested and Advanced Conditions

**File:** `02_nested_and_advanced_conditions.py`

After mastering the three building blocks, the learner is ready for more sophisticated patterns. This file introduces multi-elif chains for real use cases, nested if for layered decisions, logical operators inside conditions, and independent if blocks for unrelated checks.

The learner studies:

- Multi-elif chains for grades, HTTP status codes, and user roles
- Nested if: "Layered Tree" — the inner check only runs when the outer is True
- Combining `and` and `or` inside conditions as an alternative to nesting
- Independent if blocks: "Checklist Mode" — every check always runs
- The critical difference between chained (`if/elif`) and independent (`if/if`) blocks

---

### 3. Finish with Inline If and Match Case

**File:** `03_inline_if_and_match_case.py`

The final file introduces two compact forms of conditional logic, then applies everything from the chapter to two real validation programs. This file connects the chapter to practical software development.

The learner studies:

- Inline if (ternary): "Quick, short, simple check" — one line for simple two-outcome logic
- Chained inline if for three outcomes
- When to use inline if (simple) vs classical if (complex)
- `match/case`: "Pattern Matcher" — match one exact value to multiple options
- The `|` operator inside case to match multiple values in one branch
- The `_` wildcard as the fallback case
- `match/case` vs `if/elif/else`: when each is the better choice
- Challenge 1: Email validator with six independent rules
- Challenge 2: Password validator with seven independent rules

---

## 🧱 Lesson Breakdown

### Lesson 1 — If, Else, Elif

**File:** `01_if_else_elif.py`

This lesson builds the complete foundation for conditional thinking. Every concept is supported by an ASCII flowchart that shows the program's execution path visually.

#### Key Concepts

- Conditional statement: a checkpoint that checks a condition
- Straight-line code always runs every statement; conditional code chooses a path
- `if`: starts the chain, requires a condition, can stand alone
- `else`: optional fallback, no condition, must be last, only one allowed
- `elif`: follow-up condition, optional, can repeat, cannot stand alone
- Indentation: Python uses spaces to define which code belongs to which block
- Only the first matching condition in a chain runs; the rest are skipped

#### Example

```python
score = 85

# Standalone if
if score >= 90:
    print("A")
# Output: (nothing — condition is False)

# if / else
if score >= 90:
    print("A")
else:
    print("F")
# Output: F

# if / elif / else
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
# Output: B
```

#### Why This Lesson Matters

Without conditionals, a program cannot respond differently to different inputs. Every real program — from a login form to a recommendation engine — depends on the ability to check a condition and choose a path. This lesson gives the learner the building blocks for all of that.

---

### Lesson 2 — Nested and Advanced Conditions

**File:** `02_nested_and_advanced_conditions.py`

This lesson extends conditional logic to real-world patterns. The learner discovers how to handle many outcomes, layer decisions inside each other, combine conditions with logical operators, and run completely independent checks.

#### Key Concepts

- Multi-elif chains: grade ranges, HTTP codes, role-based responses
- Nested if: inner condition only runs when outer condition is already True
- "Layered Tree" — each branch can contain its own decision
- `and` inside if: both conditions must be True to enter the block
- `or` inside if: at least one condition must be True
- Logical operators vs nested if: both solve the same problem, different style
- Independent if blocks: every check runs regardless of others ("Checklist Mode")
- `if/elif/else` stops at first True; independent `if` blocks always all run

#### Example

```python
# Nested if
score = 95
submitted_project = True

if score >= 90:
    if submitted_project:
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "F"

print(grade)  # Output: A+

# Independent if blocks — both always run
if score >= 90:
    print("High Score")   # Output: High Score
else:
    print("Low Score")

if submitted_project:
    print("Project submitted")   # Output: Project submitted
else:
    print("Project missing")
```

#### Why This Lesson Matters

Real programs rarely have just two outcomes. A student grade system needs A, B, C, D, and F. An API needs to handle dozens of status codes. A user system needs to handle admin, moderator, editor, and guest roles. This lesson gives the learner the tools to build all of those patterns correctly.

---

### Lesson 3 — Inline If and Match Case

**File:** `03_inline_if_and_match_case.py`

This lesson introduces two compact forms of conditional logic and applies the full chapter knowledge to two real validation programs that check email and password quality.

#### Key Concepts

- Inline if (ternary): `do A if condition else do B`
- Chained inline if: three outcomes on one readable expression
- Use simple logic with inline if; use classical if for complex logic
- `match value: case option:` matches exact values, runs first match
- `case "A" | "B":` matches multiple values in one case
- `case _:` is the wildcard fallback (equivalent to `else`)
- `match/case` requires Python 3.10+
- Independent if blocks with a `valid` flag for real validation
- `.strip()` before checking, specific messages per rule, final verdict

#### Example

```python
# Inline if
score = 80
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)  # Output: B

# match / case
country = "Egypt"
match country:
    case "United States" | "USA":
        print("US")
    case "Egypt":
        print("EG")
    case _:
        print("Unknown Country")
# Output: EG
```

#### Why This Lesson Matters

Inline if and match/case are tools that appear frequently in professional Python code. Validation programs — checking emails, passwords, phone numbers, and usernames — are among the most common real-world applications of conditional logic. This lesson bridges the gap between learning conditionals and applying them to actual software problems.

---

## 🧠 Core Concepts Summary

| Concept | Form | Description | Use When |
|---|---|---|---|
| Standalone if | `if cond:` | "Just Checking" — do this or nothing | One optional action |
| if / else | `if: else:` | "This or That" — always one of two paths | Two outcomes |
| if / elif / else | `if: elif: else:` | "Branching" — choose one from many | Multiple exclusive outcomes |
| Nested if | `if: if:` | "Layered Tree" — step-by-step decisions | Second check depends on first |
| Logical and/or | `if a and b:` | Combine multiple conditions in one line | Replacing simple nesting |
| Independent ifs | `if: ... if: ...` | "Checklist Mode" — all always run | Unrelated separate checks |
| Inline if | `A if cond else B` | "Quick, short, simple check" | Simple two-outcome one-liner |
| match / case | `match val: case:` | "Pattern Matcher" — exact value routing | Fixed options, exact matching |

---

## 📋 Reference Tables

### The Three Building Blocks

| Keyword | Condition Required | Required | Can Stand Alone | How Many Per Chain |
|---|---|---|---|---|
| `if` | Yes | Yes | Yes | Exactly one |
| `elif` | Yes | No | No | As many as needed |
| `else` | No | No | No | At most one |

### Conditional Forms Comparison

| Form | Nickname | Stops at First True | Always Runs All | Python Version |
|---|---|---|---|---|
| `if` | Just Checking | Yes | — | All |
| `if/else` | This or That | Yes | — | All |
| `if/elif/else` | Branching | Yes | — | All |
| Independent `if` | Checklist Mode | — | Yes | All |
| Inline `if` | Quick Check | Yes | — | All |
| `match/case` | Pattern Matcher | Yes | — | 3.10+ |

### if/elif/else vs match/case

| Feature | if / elif / else | match / case |
|---|---|---|
| Best for | Flexible logic and ranges | Matching exact fixed values |
| Conditions | Any boolean expression | Exact value comparison only |
| Multiple values per branch | Use `or` in condition | Use `\|` inside a case |
| Fallback | `else` | `case _` |
| Python version | All versions | 3.10+ only |

### Inline If Syntax

| Form | Syntax | Example |
|---|---|---|
| Two outcomes | `A if cond else B` | `"A" if score >= 90 else "F"` |
| Three outcomes | `A if c1 else B if c2 else C` | `"A" if s>=90 else "B" if s>=80 else "F"` |

---

## 🧪 Practice Challenges

### Challenge 1 — Grade Calculator

Write a program that takes a score and assigns a grade using a full multi-elif chain.

Requirements:

- 90 and above → A
- 80 to 89 → B
- 70 to 79 → C
- 60 to 69 → D
- Below 60 → F
- Use an inline if to also print "Pass" or "Fail" based on whether the grade is D or above

Expected output:

```text
Score: 85
Grade: B
Result: Pass
```

---

### Challenge 2 — Country Code Router

Write a program that converts a country name to its 2-letter code using match/case.

Requirements:

- Support at least 5 countries
- Use the `|` operator to allow both full name and abbreviation (e.g. "United States" or "USA")
- Use `case _` as a fallback
- Print the code or "Unknown Country"

Expected output:

```text
Country: Egypt
Code: EG
```

---

### Challenge 3 — Access Control System

Write a program that determines whether a user should be granted access.

Requirements:

- User must be logged in OR be a guest
- User must NOT be banned
- Use parentheses to ensure correct precedence
- Test with a banned user and a valid user
- Display the result of each check and the final decision

```python
is_logged_in = True
is_guest = False
is_banned = True
```

Expected output:

```text
Role check:    True
Not banned:    False
Access granted: False
```

---

### Challenge 4 — Nested Grade with Bonus

Write a program that assigns grades using nested if to award bonus grades.

Requirements:

- Score 90+ AND submitted project → A+
- Score 90+ but no project → A
- Score 80–89 → B
- Score 70–79 → C
- Below 70 → F

Expected output:

```text
Score: 95 | Project: True
Grade: A+
```

---

### Challenge 5 — Username Validator

Write a program that validates a username using independent if blocks with a valid flag.

Requirements:

- Must not be empty
- Must be between 5 and 20 characters
- Must contain only letters and digits (no spaces or symbols)
- Must start with a letter
- Must not be the same as the email

Expected output:

```text
Username: coder_pro
Not empty:       True
Valid length:    True
Alphanumeric:    False (contains underscore)
Starts with letter: True
Not same as email:  True
Username is invalid ❌
```

---

## 🏗️ Mini Project — User Registration Validator

### Project Goal

Build a complete registration validation system that checks both an email address and a password, displays a detailed rule-by-rule report, and shows a final registration decision.

### Requirements

The program must validate:

**Email:**
- Not empty
- Contains both `.` and `@`
- Contains exactly one `@`
- Ends with `.com`, `.org`, or `.net`
- Not longer than 254 characters
- Starts and ends with a letter or digit

**Password:**
- Not empty
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- Not the same as the email
- No spaces
- Starts and ends with a letter or digit

### Starter Code

```python
email    = "shehab@gmail.com"
password = "Shehab123"

email_valid    = True
password_valid = True

# --- Email Validation ---
email = email.strip()

if email == "":
    print("Email: cannot be empty")
    email_valid = False
if not ('.' in email and '@' in email):
    print("Email: must contain . and @")
    email_valid = False
if email.count('@') != 1:
    print("Email: must contain exactly one @")
    email_valid = False
if not email.endswith(('.com', '.org', '.net')):
    print("Email: must end with .com, .org, or .net")
    email_valid = False
if len(email) > 254:
    print("Email: must not exceed 254 characters")
    email_valid = False
if email != "" and not (email[0].isalnum() and email[-1].isalnum()):
    print("Email: must start and end with a letter or digit")
    email_valid = False

# --- Password Validation ---
password = password.strip()

if password == "":
    print("Password: cannot be empty")
    password_valid = False
if len(password) < 8:
    print("Password: must be at least 8 characters")
    password_valid = False
if not any(char.isupper() for char in password):
    print("Password: must include at least one uppercase letter")
    password_valid = False
if not any(char.islower() for char in password):
    print("Password: must include at least one lowercase letter")
    password_valid = False
if password == email:
    print("Password: must not be the same as the email")
    password_valid = False
if " " in password:
    print("Password: must not contain spaces")
    password_valid = False
if password != "" and not (password[0].isalnum() and password[-1].isalnum()):
    print("Password: must start and end with a letter or digit")
    password_valid = False

# --- Final Report ---
print("=" * 40)
print("     REGISTRATION REPORT")
print("=" * 40)
print(f"Email:    {'✅ Valid' if email_valid    else '❌ Invalid'}")
print(f"Password: {'✅ Valid' if password_valid else '❌ Invalid'}")
print("=" * 40)
if email_valid and password_valid:
    print("Registration: APPROVED ✅")
else:
    print("Registration: REJECTED ❌")
print("=" * 40)
```

### Expected Output

```text
========================================
     REGISTRATION REPORT
========================================
Email:    ✅ Valid
Password: ✅ Valid
========================================
Registration: APPROVED ✅
========================================
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Using `=` instead of `==` inside a condition | `=` assigns a value, does not compare | Use `==` for comparison inside `if` |
| Forgetting the colon `:` after `if`, `elif`, or `else` | Raises a `SyntaxError` | Always end the condition line with `:` |
| Incorrect indentation inside a block | Python raises an `IndentationError` | Use 4 spaces consistently for each level |
| Writing `elif` or `else` without a preceding `if` | Raises a `SyntaxError` | `elif` and `else` must always follow an `if` |
| Assuming `elif` always runs after `if` | `elif` only runs if all previous conditions were False | Use independent `if` blocks when all conditions must be checked |
| Using `match/case` in Python below 3.10 | Raises a `SyntaxError` | Check Python version or use `if/elif/else` instead |
| Overusing inline if for complex logic | Makes code hard to read | Use inline if only for simple two-outcome expressions |
| Not stripping user input before validating | Leading or trailing spaces cause silent failures | Always call `.strip()` before any validation check |

---

## 💡 Professional Tips

- Always use parentheses when combining `and` and `or` in the same condition. It removes ambiguity and prevents bugs caused by operator precedence.
- Use independent `if` blocks (not `elif`) when you need to collect all failed conditions, such as in a form validator that shows multiple error messages.
- Use a `valid = True` flag with independent ifs to track overall validity while still checking every rule.
- Prefer `match/case` over long `if/elif` chains when matching a single variable against many fixed exact values.
- Keep inline if expressions on one or two lines maximum. If it needs more, switch to classical if.
- Add `.strip()` to every string input before any conditional check. Extra whitespace is a frequent source of silent validation bugs.
- Use `any(char.isupper() for char in password)` to check character properties across a string without writing a loop explicitly.
- Comment the intent of complex conditions, not just the operators. `# both must be True for access` is more useful than `# and`.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 6, make sure you can:

- [ ] Explain the difference between straight-line code and conditional code.
- [ ] Write a standalone `if` statement with correct syntax and indentation.
- [ ] Write `if/else` for a two-outcome decision.
- [ ] Write `if/elif/else` for a multi-branch decision.
- [ ] Explain why only the first True condition in a chain executes.
- [ ] Build a multi-elif chain for grade ranges, status codes, or roles.
- [ ] Write a nested `if` and explain when the inner block runs.
- [ ] Use `and` and `or` inside a condition to replace simple nesting.
- [ ] Explain the difference between chained `elif` and independent `if` blocks.
- [ ] Write an inline if for a simple two-outcome decision.
- [ ] Chain inline ifs for three outcomes.
- [ ] Write a `match/case` statement with a wildcard `case _`.
- [ ] Use `|` inside a case to match multiple values.
- [ ] Explain when to use `match/case` instead of `if/elif/else`.
- [ ] Build a multi-rule validator using independent ifs and a `valid` flag.
- [ ] Build the User Registration Validator mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 6 when they can:

1. Run all three chapter files without errors.
2. Explain the output of every print statement in each file.
3. Modify examples with different input values and predict the results correctly.
4. Complete all five practice challenges without referring to the solutions.
5. Build the mini project independently without referring to the starter code.
6. Explain the difference between `if/elif` and independent `if` blocks and choose correctly.
7. Write a real validator for a new input type (phone number, username, URL) applying the same pattern.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 6 — Python Loops

Chapter 6 builds directly on what was learned here. Every loop uses a condition to decide whether to keep running or stop. The `while` loop uses an `if`-style condition. Loop control statements (`break`, `continue`, `pass`) are conditional actions. The pattern of checking a condition and deciding what to do next, which this chapter establishes, is the core mechanism of every loop.

---

## 📚 Additional Resources

- [Python Official Documentation — if Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Official Documentation — match Statements](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
- [PEP 634 — Structural Pattern Matching](https://peps.python.org/pep-0634/)
- [Real Python — Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Real Python — Python match Statement](https://realpython.com/python310-new-features/#structural-pattern-matching)

---

<p align="center">
  <strong>Chapter 5 Complete — Python Conditional Statements ✅</strong>
</p>

<p align="center">
  <a href="../04_logic_and_operators/README.md">← Previous Chapter: Logic and Operators</a> ·
  <a href="../README.md">Main README</a> ·
  <a href="../06_loops/README.md">Next Chapter: Python Loops →</a>
</p>