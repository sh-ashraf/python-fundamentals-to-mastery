# Chapter 6 — Python Loops

<p align="center">
  <strong>Master iteration in Python — automate repetitive tasks, control loop flow, and build scalable data pipelines with for and while loops.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Level-Beginner-brightgreen" alt="Level: Beginner">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Language: Python">
  <img src="https://img.shields.io/badge/Chapter-06-orange" alt="Chapter 06">
  <img src="https://img.shields.io/badge/Focus-Loops-purple" alt="Focus: Loops">
</p>

---

## 📌 Chapter Overview

This chapter introduces loops, which are the mechanism that allows a program to repeat a block of code automatically. Without loops, processing 100 files would require 100 separate code blocks. With loops, the same logic runs once and repeats as many times as needed.

The chapter moves from understanding what loops are and how they work internally, through for loops and their control statements, to nested loops for hierarchical data, and finally to while loops for condition-based iteration. By the end, the learner will be able to build automated, scalable workflows that process data without manual repetition.

---

## 🎯 Learning Outcomes

After completing this chapter, the learner will be able to:

- Explain what a loop is and why it matters for automation and data processing.
- Describe how Python creates an iterator behind the scenes for a for loop.
- Iterate over tuples, lists, strings, and ranges using for loops.
- Use `range()` with start, stop, and step arguments.
- Apply for loops to aggregate data and clean file names.
- Use `break` to exit a loop immediately when a critical condition is met.
- Use `continue` to skip specific iterations without stopping the loop.
- Use `pass` as a placeholder when logic is not yet written.
- Use `for/else` to handle the "not found" scenario cleanly.
- Build nested loops for data combinations, time hierarchies, and database pipelines.
- Write while loops with the three required pillars: initialization, condition, update.
- Use the `while condition` pattern for counters and limited retries.
- Use the `while True` pattern for open-ended input and streaming data.
- Combine while loops with else for maximum-attempt scenarios.
- Choose correctly between for and while loops based on the situation.

---

## 👤 Target Learner

| Learner Type | Description |
|---|---|
| Absolute beginners | Learners who have completed Chapter 5 and are ready to automate repetition |
| Data learners | Learners preparing to process files, columns, rows, and datasets in bulk |
| Programming beginners | Learners who want to understand how Python repeats operations efficiently |
| Review learners | Learners who want a structured refresher on for loops, while loops, and loop control |

---

## 🧩 Prerequisites

Before starting this chapter, the learner should be able to:

- Use variables, data types, and type conversion.
- Use comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Use logical operators: `and`, `or`, `not`.
- Use `if`, `elif`, and `else` for conditional decisions.
- Understand boolean values: `True`, `False`.
- Complete Chapters 1 through 5 of this series.

---

## 🗺️ Learning Path

The chapter follows a deliberate progression from understanding what a loop is and how it works, through the different types and control patterns, to practical automation scenarios.

```text
What Are Loops? (Straight-line vs Loop flowchart)
                    ↓
For Loop Mechanics (iterator, next, StopIteration)
                    ↓
Sequences and range() (tuple, list, string, range)
                    ↓
Real-World For Loop Applications (aggregation, cleansing)
                    ↓
Loop Control: break, continue, pass
                    ↓
For-Else: The "No-Break" Clause
                    ↓
Nested Loops (combinations, hierarchies, pipelines)
                    ↓
While Loops: Condition Pattern (initialization, condition, update)
                    ↓
While Loops: True Pattern (intentional infinite loop + break)
                    ↓
For vs While (choosing the right loop)
```

This sequence is intentional:

1. The learner first understands what a loop is and why it exists.
2. Then the learner masters for loops, which are the safer and more common type.
3. Then the learner learns how to control loops with break, continue, and pass.
4. Then the learner discovers nested loops for multi-dimensional data processing.
5. Finally, the learner learns while loops, which are more powerful but riskier.

---

## 📁 Chapter Files

| Step | File | Topic | Core Skill |
|---|---|---|---|
| 01 | `01_for_loops.py` | For Loops | Iteration, iterator mechanics, sequences, `range()`, aggregation, cleansing |
| 02 | `02_break_continue_pass.py` | Loop Control Statements | `break`, `continue`, `pass`, flowcharts, real-world filtering and security |
| 03 | `03_for_else_and_nested_loops.py` | For-Else and Nested Loops | "No-break" clause, search pattern, data combinations, hierarchies, pipelines |
| 04 | `04_while_loops.py` | While Loops | Three pillars, `while condition`, `while True`, for vs while, max-attempt challenge |

---

## 🧭 Recommended Study Order

### 1. Start with For Loops

**File:** `01_for_loops.py`

Start here because for loops are the foundation of all iteration in Python. Before learning how to control or nest loops, the learner needs to understand what a loop is, how Python processes it internally, and what types of data it can iterate over.

The learner studies:

- Loops as "autopilot" for repetitive code
- Straight-line code vs loop statement (flowchart comparison)
- How Python creates an iterator automatically (`iter`, `next`, `StopIteration`)
- Looping over tuples, lists, strings, and ranges
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- Real-world use case 1: aggregation — summing a list of scores
- Real-world use case 2: data cleansing — cleaning file names in bulk

---

### 2. Move to Loop Control Statements

**File:** `02_break_continue_pass.py`

After mastering the basic for loop, the learner needs to know how to modify its behavior. This file introduces the three control statements that allow a loop to stop early, skip specific items, or act as a placeholder.

The learner studies:

- `break`: exits the loop entirely and immediately ("emergency exit")
- `continue`: skips the current iteration only, loop resumes at next item
- `pass`: does nothing — a silent placeholder for future logic
- Behind-the-scenes flowcharts for each statement
- Real-world use: break for SQL injection detection, continue for weekend skipping
- Risk levels: break (critical), continue (medium), pass (none)

---

### 3. Learn For-Else and Nested Loops

**File:** `03_for_else_and_nested_loops.py`

With loop control understood, the learner is ready for two important patterns. For-else adds a clean "not found" handler. Nested loops unlock multi-dimensional data processing.

The learner studies:

- `for/else`: else runs ONLY if no break fired ("no-break" clause)
- Why else without break is pointless — just write it after the loop
- The search pattern: break = found, else = not found
- Real-world: detecting None values, verifying all files are CSV
- Challenge: duplicate file detector using seen list + break + else
- Nested loops: inner loop runs fully for every outer step
- Execution count: outer × inner (× deeper for 3+ levels)
- Application 1: crossing data — color × size combinations
- Application 2: time hierarchy — years → months → days
- Application 3: database pipeline — tables → columns → SQL queries

---

### 4. Finish with While Loops

**File:** `04_while_loops.py`

The final file introduces while loops, which are more powerful than for loops but carry higher risk. The learner discovers two distinct patterns and learns when to choose while over for.

The learner studies:

- While loop: repeats as long as YOUR condition is True
- The 3 pillars: initialization, condition, update (forget update = infinite loop)
- `while condition`: exits naturally when condition becomes False (safer)
- `while True`: intentional infinite loop, requires break to exit (more flexible)
- Combining while with else for the "max attempts" pattern
- For vs while: known iterations (for) vs unknown iterations (while)

---

## 🧱 Lesson Breakdown

### Lesson 1 — For Loops

**File:** `01_for_loops.py`

This lesson introduces loops as the tool that allows Python to repeat a block of code automatically. It explains the for loop from the outside (syntax and sequences) and from the inside (iterator mechanics).

#### Key Concepts

- A loop is "autopilot" for repetitive code — write once, run many times
- The for loop assigns one item at a time from a sequence to the loop variable
- Python creates an iterator automatically using `iter()` and `next()`
- `StopIteration` signals the end of the sequence and terminates the loop
- Sequences: tuple, list, string, `range()`
- `range(stop)` starts at 0; `range(start, stop)` starts at start; `range(start, stop, step)` jumps by step
- `range()` stop value is always excluded

#### Example

```python
# Iterate over a range
for item in range(1, 6):
    print(f"Round: {item}")
# Output: Round: 1, Round: 2, Round: 3, Round: 4, Round: 5

# Aggregate data
scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
print("Final Total:", total)
# Output: Final Total: 265

# Clean file names
files = [' reports.csv ', ' DATA.csv']
for file in files:
    clean = file.strip().lower()
    print(f"Processing: {clean}")
# Output:
# Processing: reports.csv
# Processing: data.csv
```

#### Why This Lesson Matters

Every program that processes more than one item uses a loop. Without loops, data pipelines, file processors, and report generators would be impossible to write at scale. This lesson is the gateway to automation.

---

### Lesson 2 — Break, Continue, and Pass

**File:** `02_break_continue_pass.py`

This lesson teaches the learner how to modify loop behavior at runtime using three control statements. Each one changes what happens inside the loop in a fundamentally different way.

#### Key Concepts

- `break`: exits the entire loop immediately — nothing after it in the loop runs
- `continue`: skips the rest of the current iteration — loop resumes at next item
- `pass`: does nothing — loop continues normally as if pass wasn't there
- `break` = CRITICAL risk (security, data integrity), `continue` = MEDIUM risk (filtering), `pass` = NO risk (placeholder)
- Quick decision: "Stop everything?" → break | "Skip just this?" → continue | "Plan later?" → pass

#### Example

```python
# break — stop on empty value
names = ['john', 'maria', '', 'omar']
for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')
# Output: Name = john / Name = maria / Empty value detected!

# continue — skip weekends
days = ['Mon', 'Sun', 'Wed', 'Tue']
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(f'Workday: {day}')
# Output: Workday: Mon / Workday: Wed / Workday: Tue
```

#### Why This Lesson Matters

Real data is messy. A list of emails might contain an SQL injection. A list of files might contain non-CSV entries. A list of names might contain empty strings. Loop control statements give the learner precise tools to respond to these situations without rewriting the loop.

---

### Lesson 3 — For-Else and Nested Loops

**File:** `03_for_else_and_nested_loops.py`

This lesson introduces two important patterns that extend the power of for loops. For-else adds a clean search completion handler. Nested loops enable multi-dimensional data processing, which is fundamental to data engineering.

#### Key Concepts

- `for/else`: else runs ONLY if no break fired — think of it as "nobreak"
- Only use else when there is a break inside the loop
- The search pattern: loop to find, break if found, else handles not-found
- Nested loop: inner loop runs its ENTIRE cycle for every single outer step
- Each loop has its own independent iterator
- Execution count: outer_items × inner_items

#### Example

```python
# for/else — search pattern
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even found:", i)
        break
else:
    print("All numbers are odd")
# Output: Even found: 4

# Nested loop — all combinations
colors = ['red', 'blue']
sizes  = ['L', 'M']
for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
# Output: red-L / red-M / blue-L / blue-M

# Database pipeline
tables  = ['customers', 'orders']
columns = ['id', 'create_date']
for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')
```

#### Why This Lesson Matters

For-else removes the need for a `found = False` flag variable, producing cleaner and more Pythonic code. Nested loops are the backbone of metadata-driven data pipelines — processing every combination of tables, columns, dates, or file paths without writing each query manually.

---

### Lesson 4 — While Loops

**File:** `04_while_loops.py`

This lesson introduces while loops, which repeat based on a condition you define rather than a fixed sequence. Two distinct patterns are covered, and the chapter concludes with a full comparison of for vs while.

#### Key Concepts

- While loop: repeats as long as YOUR condition is True
- The 3 pillars: initialization (before), condition (gatekeeper), update (inside — CRITICAL)
- Forgetting the update = condition never becomes False = infinite loop = crash
- Pattern 1 (`while condition`): exits naturally — safer, more readable — counters, retries
- Pattern 2 (`while True`): intentional infinite loop — must use break — streams, APIs, games
- `while/else`: else runs if loop finishes naturally (no break) — max-attempt handler
- For = fixed sequence, known count | While = your condition, unknown count

#### Example

```python
# while condition
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
# Output: Count: 1 ... Count: 5

# while True
while True:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        break
print("Thank You")

# while with else — max attempts
attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out!")
```

#### Why This Lesson Matters

While loops handle the cases that for loops cannot: situations where the number of iterations is unknown, where the program must wait for external input or data, or where a loop must run until a user takes a specific action. These patterns appear in authentication systems, game loops, server polling, and real-time data processing.

---

## 🧠 Core Concepts Summary

| Concept | Syntax | Description | Use When |
|---|---|---|---|
| For loop | `for item in seq:` | Iterate over a fixed sequence | Number of iterations is known |
| range() | `range(start, stop, step)` | Generate numeric sequences | Need index-based or counted loops |
| break | `break` | Exit loop immediately | Critical condition met |
| continue | `continue` | Skip current iteration | Filtering bad or irrelevant data |
| pass | `pass` | Do nothing, placeholder | Logic not yet written |
| for/else | `for: ... else:` | else runs if no break fired | Search pattern, not-found handler |
| Nested loop | `for: for:` | Inner loop runs fully per outer step | Combinations, hierarchies, pipelines |
| While loop | `while cond:` | Repeat while condition is True | Number of iterations is unknown |
| while True | `while True: ... break` | Intentional infinite loop | Open-ended input, streaming, games |
| while/else | `while: ... else:` | else runs if no break fired | Max-attempt patterns |

---

## 📋 Reference Tables

### For Loop — Sequences

| Type | Example | Notes |
|---|---|---|
| Tuple | `for i in (1, 2, 3):` | Immutable sequence |
| List | `for i in [1, 2, "Hi"]:` | Mixed types allowed |
| String | `for c in "Python":` | Iterates character by character |
| range() | `for i in range(1, 10, 2):` | Generates numbers on demand |

### range() Reference

| Syntax | Starts At | Stops Before | Example | Output |
|---|---|---|---|---|
| `range(5)` | 0 | 5 | `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 5)` | 1 | 5 | `range(1, 5)` | 1, 2, 3, 4 |
| `range(1, 10, 2)` | 1 | 10 | `range(1, 10, 2)` | 1, 3, 5, 7, 9 |

### Loop Control Statements

| Statement | Action | Loop Continues? | Risk Level | Best For |
|---|---|---|---|---|
| `break` | Exit immediately | No — loop destroyed | Critical | Security threats, data integrity |
| `continue` | Skip current iteration | Yes — resumes at next item | Medium | Filtering bad or empty data |
| `pass` | Do nothing | Yes — continues normally | None | Placeholder, future planning |

### For vs While

| Feature | For Loop | While Loop |
|---|---|---|
| Iterates over | Fixed sequence (predefined) | Your condition (True/False) |
| Nr. of iterations | Known in advance | Unknown — depends on event |
| Progression | Automatic (gets next item) | Manual (you MUST update) |
| Primary risk | Low — safe and predictable | High — infinite loop risk |
| Best for | "Processing Data" | "Waiting for External Event" |
| Style | Simple / Clear / Safe | Advanced / Flexible / Risk |

### While Loop Patterns

| Pattern | Syntax | Exits When | Best For |
|---|---|---|---|
| While condition | `while cond: ... update` | Condition becomes False | Counters, limited retries |
| While True | `while True: ... if: break` | break fires | Input, streams, APIs, games |
| While else | `while cond: ... else:` | Loop exhausted naturally | Max-attempt handlers |

---

## 🧪 Practice Challenges

### Challenge 1 — Multiplication Table

Write a program that prints the 7-times table from 1 to 10 using a for loop.

Requirements:

- Use `range(1, 11)` for the sequence
- Format each line as: `7 x 1 = 7`

Expected output:

```text
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

---

### Challenge 2 — SQL Injection Scanner

Write a program that scans a list of emails and stops processing as soon as a dangerous value is detected.

Requirements:

- Process each email normally
- If a semicolon `;` is detected, print a warning and stop immediately
- Use `break` for the security exit

```python
emails = ['data@gmail.com', 'baraa@outlook.de', 'DROP TABLE USERS;', 'maria@gmail.com']
```

Expected output:

```text
Processing Email: data@gmail.com
Processing Email: baraa@outlook.de
SQL Injection detected: Hacker Attack!
```

---

### Challenge 3 — Duplicate File Detector

Write a program that checks whether any filename appears more than once.

Requirements:

- Use a `seen` list to track processed filenames
- If a duplicate is found, print "Duplicate found" and stop
- If all files are unique, print "All files are unique"
- Use `for/else` and `break`

```python
file_list = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']
```

Expected output:

```text
Duplicate found: report.csv
```

---

### Challenge 4 — Product Catalog Generator

Write a program that generates all possible product variants using nested loops.

Requirements:

- Use two lists: colors and sizes
- Print every combination in the format: `red - Size L`
- Count and display the total number of combinations at the end

```python
colors = ['red', 'blue', 'green']
sizes  = ['S', 'M', 'L', 'XL']
```

Expected output:

```text
red - Size S
red - Size M
...
green - Size XL
Total combinations: 12
```

---

### Challenge 5 — Agreement Confirmation (Max 3 Attempts)

Write a program that asks the user for agreement with a maximum of 3 attempts.

Requirements:

- Allow up to 3 attempts
- If user types "yes" → print "Glad we're on the same page" and stop
- If 3 attempts are exhausted → print "3 strikes. You're out!"
- Use `while/else` with a counter

Expected output (yes on attempt 2):

```text
Do you agree? (yes/no): no
Do you agree? (yes/no): yes
Glad we're on the same page
```

Expected output (all 3 failed):

```text
Do you agree? (yes/no): no
Do you agree? (yes/no): no
Do you agree? (yes/no): no
3 strikes. You're out!
```

---

## 🏗️ Mini Project — Automated Data Quality Report

### Project Goal

Build a program that scans a dataset of records and produces a complete data quality report — checking for duplicates, missing values, invalid file types, and generating a summary.

### Requirements

The program must:

- Loop through a list of records (each record is a dictionary with name, email, file)
- Check for empty or None names using for-else
- Check for duplicate emails using a seen list and break
- Check that all files end with `.csv` using for-else
- Generate a batch of SQL NULL-check queries using nested loops
- Display a final summary report

### Starter Code

```python
records = [
    {"name": "Alice",  "email": "alice@gmail.com",  "file": "data1.csv"},
    {"name": "Bob",    "email": "bob@outlook.com",   "file": "report.pdf"},
    {"name": None,     "email": "carol@gmail.com",   "file": "data2.csv"},
    {"name": "David",  "email": "alice@gmail.com",   "file": "sales.csv"},
]

missing_name     = False
duplicate_email  = False
non_csv_found    = False
seen_emails      = []

# --- Check 1: Missing Names ---
for record in records:
    if record["name"] is None:
        missing_name = True
        break
else:
    missing_name = False

# --- Check 2: Duplicate Emails ---
for record in records:
    email = record["email"]
    if email in seen_emails:
        duplicate_email = True
        break
    seen_emails.append(email)

# --- Check 3: Non-CSV Files ---
for record in records:
    if not record["file"].endswith(".csv"):
        non_csv_found = True
        break
else:
    non_csv_found = False

# --- SQL NULL Check Queries (Nested Loop) ---
tables  = ["customers", "orders"]
columns = ["id", "email", "create_date"]

print("=" * 50)
print("     SQL NULL CHECK QUERIES")
print("=" * 50)
for t in tables:
    for c in columns:
        print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL;")

# --- Final Report ---
print("=" * 50)
print("     DATA QUALITY REPORT")
print("=" * 50)
print(f"Missing names:     {'⚠️  Found'  if missing_name    else '✅ None'}")
print(f"Duplicate emails:  {'⚠️  Found'  if duplicate_email else '✅ None'}")
print(f"Non-CSV files:     {'⚠️  Found'  if non_csv_found   else '✅ None'}")
print("=" * 50)
all_clean = not any([missing_name, duplicate_email, non_csv_found])
print(f"Overall Status:    {'✅ CLEAN' if all_clean else '❌ ISSUES FOUND'}")
print("=" * 50)
```

### Expected Output

```text
==================================================
     SQL NULL CHECK QUERIES
==================================================
SELECT count(*) FROM customers WHERE id IS NULL;
SELECT count(*) FROM customers WHERE email IS NULL;
SELECT count(*) FROM customers WHERE create_date IS NULL;
SELECT count(*) FROM orders WHERE id IS NULL;
SELECT count(*) FROM orders WHERE email IS NULL;
SELECT count(*) FROM orders WHERE create_date IS NULL;
==================================================
     DATA QUALITY REPORT
==================================================
Missing names:     ⚠️  Found
Duplicate emails:  ⚠️  Found
Non-CSV files:     ⚠️  Found
==================================================
Overall Status:    ❌ ISSUES FOUND
==================================================
```

---

## ⚠️ Common Mistakes

| Mistake | Why It Is a Problem | Correct Approach |
|---|---|---|
| Forgetting the update step in a while loop | Condition never becomes False → infinite loop → crash | Always include `counter += 1` or similar inside the while body |
| Using `elif` or `else` without `break` in a for-else | `else` always runs — adds no value without a `break` | Only use `for/else` when a `break` exists inside the loop |
| Using `continue` when `break` is needed | Loop keeps running after a critical error is found | Use `break` for critical conditions, `continue` for filtering |
| Modifying the sequence while looping over it | Produces unexpected behavior or skips items | Loop over a copy or collect items to modify, then apply changes after |
| Using `range(n)` when you need `range(1, n+1)` | Output starts at 0, not 1 | Use `range(1, n+1)` when you need 1-based iteration |
| Forgetting that `range()` stop is excluded | `range(1, 5)` gives 1, 2, 3, 4 — not 5 | Always mentally check: stop - 1 is the last value |
| Nesting too many loops without comments | Code becomes impossible to read or debug | Comment each loop level (outer, inner, innermost) |
| Using a for loop when the count is unknown | for loops require a fixed sequence | Use a while loop when iteration count depends on an event |

---

## 💡 Professional Tips

- Use the loop variable name meaningfully: `for file in files` is clearer than `for i in files`.
- Always comment nested loop levels: `# outer: years`, `# inner: months` helps trace logic fast.
- Use `for/else` instead of a `found = False` flag variable for cleaner search code.
- In while loops, place the update step at the very end of the loop body to avoid skipping it.
- Prefer `while condition` over `while True` unless the exit logic genuinely cannot be expressed as a simple condition.
- Always add `.strip()` before processing string values in a loop — extra whitespace is a common source of silent bugs.
- Use `enumerate()` when you need both the index and the item: `for i, name in enumerate(names)`.
- When building SQL queries or file paths with nested loops, store results in a list instead of printing immediately — it makes the output easier to reuse.

---

## ✅ Self-Assessment Checklist

Before moving to Chapter 7, make sure you can:

- [ ] Explain what a loop is and why it replaces repetitive code.
- [ ] Explain how Python creates an iterator behind the scenes for a for loop.
- [ ] Write a for loop over a tuple, list, string, and range.
- [ ] Use all three forms of `range()`: stop, start+stop, start+stop+step.
- [ ] Explain why `range()` stop is always excluded.
- [ ] Use `break` to exit a loop immediately when a condition is met.
- [ ] Use `continue` to skip specific iterations without stopping the loop.
- [ ] Use `pass` as a placeholder inside a loop body.
- [ ] Explain the difference between `break`, `continue`, and `pass`.
- [ ] Use `for/else` correctly and explain when `else` runs vs when it is skipped.
- [ ] Explain why `for/else` without a `break` is pointless.
- [ ] Write a nested loop and calculate the total number of iterations.
- [ ] Apply nested loops to generate combinations and database SQL queries.
- [ ] Write a while loop with all three pillars: initialization, condition, update.
- [ ] Explain what happens when the update step is missing.
- [ ] Use `while True` with a `break` for open-ended input scenarios.
- [ ] Combine `while` with `else` for the max-attempts pattern.
- [ ] Choose correctly between a for loop and a while loop for a given task.
- [ ] Build the Automated Data Quality Report mini project independently.

---

## 🏁 Completion Criteria

The learner is ready for Chapter 7 when they can:

1. Run all four chapter files without errors.
2. Explain the output of every print statement in each file.
3. Modify examples with different data and predict the results correctly.
4. Complete all five practice challenges without referring to the solutions.
5. Build the mini project independently without referring to the starter code.
6. Explain the difference between `for/else` and code written after a for loop.
7. Write a nested loop that generates SQL queries for a new set of tables and columns.
8. Explain when to choose `while True` vs `while condition` and justify the choice.

---

## ➡️ Next Chapter

After completing this chapter, move to:

## Chapter 7 — Python Data Structures

Chapter 7 introduces lists, tuples, sets, and dictionaries — the structures that store the sequences loops iterate over. Every loop in this chapter iterated over a list or a range. Chapter 7 teaches the learner how to create, modify, search, and manage those collections. The two chapters are deeply connected: loops process data structures, and data structures hold the data that loops operate on.

---

## 📚 Additional Resources

- [Python Official Documentation — For Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Official Documentation — While Statements](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Python Official Documentation — range()](https://docs.python.org/3/library/stdtypes.html#range)
- [Python Official Documentation — break and continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)
- [Real Python — Python for Loops](https://realpython.com/python-for-loop/)
- [Real Python — Python while Loops](https://realpython.com/python-while-loop/)

---

<p align="center">
  <strong>Chapter 6 Complete — Python Loops ✅</strong>
</p>

<p align="center">
  <a href="../05_conditionals/README.md">← Previous Chapter: Conditional Statements</a> ·
  <a href="../README.md">Main README</a> ·
  <a href="../07_data_structures/README.md">Next Chapter: Python Data Structures →</a>
</p>