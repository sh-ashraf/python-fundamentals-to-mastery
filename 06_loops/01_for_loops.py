"""
================================================================================
PYTHON LOOPS - PART 1: FOR LOOPS
================================================================================
Learning Focus: Understanding iteration, for loop mechanics, sequences,range(), real-world use cases, and loop-based challenges
"""


# ============================================================================
# 1. WHAT ARE LOOPS?
# ============================================================================

# Loops control the flow of code and repeat a block of code
# over and over until a condition is met.
# Think of them as "autopilot" — write the logic once, run it many times.

"""
================================================================================
   STRAIGHT LINE CODE             VS              LOOP STATEMENT
================================================================================

      Start                                          Start
        |                                              |
        v                                              v
+---------------+                              +---------------+
|  print(...)   |                              |  Setup / Init |
+---------------+                              +---------------+
        |                                              |
        v                                              v
+---------------+                              +---------------+   False   +---------------+
|    x = 5      |                          +-> |  Condition ?  | --------> | Post-Loop     |
+---------------+                          |   | (For / While) |           | Statements    |
        |                                  |   +---------------+           +---------------+
        v                                  |           |                           |
+---------------+                          |          True                         v
|   input()     |                          |           |                          End
+---------------+                          |           v
        |                                  |   +---------------+
        v                                  |   |  Loop Body    |
+---------------+                          +-- |  (Action)     |
|   upper()     |                              +---------------+
+---------------+
        |
        v
       End

--------------------------------------------------------------------------------
Key Difference:
    • Straight-line code runs every statement sequentially, top to bottom.
    • Loop statements (for/while) repeat a block of code as long as a
      condition is True, creating a cycle before moving forward (False).
================================================================================
"""


# ============================================================================
# 2. WHAT IS A FOR LOOP?
# ============================================================================

# A for loop goes through a sequence one item at a time
# and executes the same block of code for each item.

for i in (1, 2, 3):
    print(i)
# Output:
# 1
# 2
# 3


# ============================================================================
# 3. HOW DOES A FOR LOOP WORK BEHIND THE SCENES?
# ============================================================================
"""
Python automatically creates an Iterator from the sequence.

Step 1: Get an iterator from the sequence.
Step 2: Ask the iterator for the next item.
Step 3: If an item exists:
            - Store it in the loop variable (i)
            - Execute the loop body
Step 4: Repeat until there are no more items.
Step 5: When the iterator is exhausted, Python stops the loop automatically.
"""

"""
================================================================================
  CODE & OUTPUT                              BEHIND THE SCENES (FOR LOOP)
================================================================================

  [ Python Code ]                                    Start
  +-----------------------+                            |
  | for i in (1, 2, 3):  |                             v
  |     print(i)         |                     +----------------+
  +-----------------------+                    | Get Iterator   |
                                               | from (1, 2, 3) |
                                               +----------------+
                                                       |
  [ Output ]                                           v
  +-----------------------+        +-------> +----------------+  False  +---------------+
  | 1                     |        |         |  Last item?    | ------> |   print(i)    |
  | 2                     |        |         |  (Is Empty?)   |         +---------------+
  | 3                     |        |         +----------------+                 |
  +-----------------------+        |                 |                          |
                                   |               True                         |
                                   |                 |                          |
                                   |                 v                          |
                                   |                End                         |
                                   |                                            |
                                   +--------------------------------------------+

--------------------------------------------------------------------------------
Key Concept:
    • A 'for' loop automatically creates an iterator from the sequence.
    • It repeatedly asks the iterator for the next item.
    • If an item is returned, it is assigned to the loop variable and the
      loop body executes.
    • When there are no more items, the iterator raises StopIteration
      and the loop ends.
    • An iterator remembers its current position, so it always knows
      what comes next.
================================================================================
"""


# ============================================================================
# 4. THE ITERATOR UNDER THE HOOD
# ============================================================================

# You never see the iterator, but Python creates and uses it automatically.
# A for loop like this:

# for i in (1, 2, 3):
#     print(i)

# is roughly equivalent to:

iterator = iter((1, 2, 3))

while True:
    try:
        i = next(iterator)
        print(i)
    except StopIteration:
        break
# Output:
# 1
# 2
# 3


# ============================================================================
# 5. YOUR FIRST FOR LOOP
# ============================================================================

# Without a loop (repetitive and inefficient):
# print("Round: 1")
# print("Round: 2")
# print("Round: 3")
# print("Round: 4")
# print("Round: 5")

# With a loop (clean and scalable):
items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")
# Output:
# Round: 1
# Round: 2
# Round: 3
# Round: 4
# Round: 5


# ============================================================================
# 6. SEQUENCES YOU CAN LOOP OVER
# ============================================================================

# --- Tuple ---
items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")
# Output: Round: 1 ... Round: 5


# --- List ---
items = [1, 2, 3, 4, "Hi"]
for item in items:
    print(f"Round: {item}")
# Output: Round: 1 ... Round: Hi


# --- String (character by character) ---
items = "Python"
for item in items:
    print(f"Round: {item}")
# Output: Round: P ... Round: n


# ============================================================================
# 7. THE RANGE() FUNCTION
# ============================================================================

# range() generates a sequence of numbers for the loop to iterate over.

# --- range(stop) → starts at 0, stops before stop ---
for item in range(5):
    print(f"Round: {item}")
# Output: Round: 0, 1, 2, 3, 4


# --- range(start, stop) → starts at start, stops before stop ---
for item in range(1, 5):
    print(f"Round: {item}")
# Output: Round: 1, 2, 3, 4


# --- range(start, stop, step) → jumps by step each time ---
for item in range(1, 10, 2):
    print(f"Round: {item}")
# Output: Round: 1, 3, 5, 7, 9


# ============================================================================
# 8. WHY FOR LOOPS MATTER - REAL-WORLD CONTEXT
# ============================================================================
"""
Question:
    "I have to process 100 different files and apply the same cleaning
    steps to each one. Should I write 100 separate blocks of code?"

Answer:
    No! That would be inefficient and error-prone.
    In Python, we use a For Loop to automate this.
    By writing the logic just once, you can tell Python to iterate
    through all your files — or columns in a table — automatically,
    saving time and ensuring consistency.

Key Takeaway:
    For Loops are not just programming syntax.
    They are the essential tool for any Data Analyst or Engineer
    looking to build automated, error-free workflows.

Real-World Applications:
    • Automation:      Move or load multiple files or tables at once
    • Data Cleansing:  Clean whitespace, fix cases, rename columns
    • Aggregation:     Calculate totals, counts, or averages from lists
"""


# ============================================================================
# 9. USE CASE 1 - AGGREGATION (Summing Scores)
# ============================================================================

# Use for loops to go through values and aggregate data
# such as summing, counting, or averaging.

scores = [80, 50, 60, 75]
total = 0

for score in scores:
    total += score      # use the loop variable, not the sequence name
    print("Current Total:", total)

print("Final Total:", total)
# Output:
# Current Total: 80
# Current Total: 130
# Current Total: 190
# Current Total: 265
# Final Total: 265


# ============================================================================
# 10. USE CASE 2 - DATA CLEANSING (Cleaning File Names)
# ============================================================================

# Use for loops to transform data — clean first, transform second.
# Always in that order.

files = [' reports.csv ', ' DATA.csv', ' final.txt']

for file in files:
    clean_name = file.strip().lower().replace('txt', 'csv')
    print(f"Processing: {clean_name}")
# Output:
# Processing: reports.csv
# Processing: data.csv
# Processing: final.csv


# ============================================================================
# 11. CHALLENGE 1 - Multiplication Table
# ============================================================================
"""
Task: Print the 7-times table from 1 to 10 using a for loop
"""

table = 7

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")
# Output:
# 7 x 1  = 7
# 7 x 2  = 14
# ...
# 7 x 10 = 70


# ============================================================================
# 12. CHALLENGE 2 - Star Pyramid
# ============================================================================
"""
Task: Print a left-aligned pyramid of stars with 6 rows using a for loop
"""

for i in range(1, 7):
    print("*" * i)
# Output:
# *
# **
# ***
# ****
# *****
# ******


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
FOR LOOPS - ESSENTIAL FACTS

What is a For Loop?
    • A loop that iterates over a sequence one item at a time
    • Executes the same block of code for each item
    • Stops automatically when the sequence is exhausted

How It Works Behind the Scenes:
    • Python creates an iterator from the sequence
    • Calls next() on the iterator each cycle
    • Assigns the item to the loop variable
    • Raises StopIteration when done → loop ends

Sequences You Can Loop Over:
    • tuple     → (1, 2, 3)
    • list      → [1, 2, 3, "Hi"]
    • string    → "Python" (character by character)
    • range()   → generates numeric sequences

range() Function:
    • range(stop)             → 0 to stop-1
    • range(start, stop)      → start to stop-1
    • range(start, stop, step) → start to stop-1, jumping by step

Real-World Use Cases:
    • Aggregation   → summing, counting, averaging values
    • Cleansing     → strip, lower, replace on each item
    • Automation    → process many files or columns with one block of code

Important Notes:
    • Use the loop variable (item), not the sequence name, inside the body
    • Clean before transforming: strip() then lower() then replace()
    • range() stop value is always EXCLUDED (not included in output)
    • For loops are the foundation of scalable data pipelines
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ What a loop is and why it matters (autopilot for repetitive code)
✓ The difference between straight-line code and loop statements (flowchart)
✓ How a for loop iterates over a sequence one item at a time
✓ How Python creates an iterator behind the scenes (iter, next, StopIteration)
✓ How to loop over tuples, lists, strings, and ranges
✓ The three forms of range(): stop / start+stop / start+stop+step
✓ That range() stop value is always excluded
✓ Real-world use case 1: aggregation — summing scores with a running total
✓ Real-world use case 2: data cleansing — cleaning file names in a list
✓ The rule: always clean (strip) before transforming (lower, replace)
✓ Challenge 1: printing a multiplication table using range(1, 11)
✓ Challenge 2: printing a left-aligned star pyramid using string repetition
✓ Why for loops are essential for data engineering and automation
"""