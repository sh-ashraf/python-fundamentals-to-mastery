"""
================================================================================
PYTHON LOOPS - PART 3: FOR-ELSE AND NESTED LOOPS
================================================================================
Learning Focus: The for-else "no-break" pattern and nested loops for hierarchical data, combinations, and automated pipelines
"""


# ============================================================================
# 1. FOR-ELSE - THE "NO-BREAK" CLAUSE
# ============================================================================

# The else block in a for loop runs ONLY if the loop finishes naturally.
# "Loop completed without a break."
# Think of else here as: "if no break happened, then do this."

"""
================================================================================
   CODE & OUTPUT                              BEHIND THE SCENES (FOR-ELSE)
================================================================================

  [ Python Code ]                                    Start
  +-----------------------+                            |
  | for i in (1, 2, 3):  |                             v
  |     print(i)         |                     +---------------+
  | else:                |     +-------------> |  Last item?   |
  |     print("End")     |     |               +---------------+
  +-----------------------+    |                 |           |
                               |               False       True
  [ Output ]                   |                 |           |
  +-----------------------+    |                 v           v
  | 1                     |    |       +-----------+   +---------------+
  | 2                     |    +-------| print(i)  |   | print("End")  | ← else block
  | 3                     |            +-----------+   +---------------+
  | End                   |                                   |
  +-----------------------+                                   v
                                                             End

--------------------------------------------------------------------------------
Key Concept (The "No-Break" Clause):
    • The name is misleading — think of 'else' in a loop as 'nobreak'
    • else runs ONLY when the loop finishes naturally (all items exhausted)
    • If the loop is interrupted by break or return, else is completely skipped
    • Perfect for the "Not Found" pattern — avoids needing a found = False flag
================================================================================
"""


# ============================================================================
# 2. IMPORTANT: WHEN ELSE IS USELESS
# ============================================================================

# If there's no break in the loop, else always runs.
# So why not just write it after the loop? — exactly, there's no point.

items = [1, 3, 4, 7]

for i in items:
    print(i)
# else:   ← this would run no matter what, so it adds no value here

print("Loop is completed")
# Output:
# 1
# 3
# 4
# 7
# Loop is completed

# RULE: Only use else with loops when there is a break inside the loop.
# That is the only time else behaves differently from code written after the loop.


# ============================================================================
# 3. FOR-ELSE + BREAK - The Search Pattern
# ============================================================================

# The real power: break skips else, natural completion runs else.
# This is ideal for searching — break = found, else = not found.

"""
================================================================================
   CODE & OUTPUT                           BEHIND THE SCENES (ELSE & BREAK)
================================================================================

  [ Python Code ]                                    Start
  +-----------------------+                            |
  | for i in (1, 2, 3):  |                             v <--------------------+
  |     if i == 2:       |                     +---------------+              |
  |         break        |         [X] True----|  Last item?   |              |
  |     print(i)         |          |          +---------------+              |
  | else:                |          |                  |                      |
  |     print("End")     |          |                False                    |
  +-----------------------+          v                  |                     |
                                +---------------+       v                     |
  [ Output ]                    | else:         | +---------------+  False  +-----------+
  +-----------------------+     | print("End")  | |   i == 2 ?    |-------->| print(i)  |
  | 1                     | [X] +---------------+ +---------------+         +-----------+
  |                       |          |                  |
  | (No End Message!)     |          |                True
  +-----------------------+          v                  v
                                    End          +-----------+
                                                 |   break   |
                                                 +-----------+
                                                       |
                                                       v
                                                      End

--------------------------------------------------------------------------------
Key Concept:
    • break fires → else is skipped entirely → goes straight to End
    • Natural loop completion → else block runs → handles "not found" case
    • The [X] marks show that else is crossed out when break triggers
================================================================================
"""

# Example: Find an even number — break if found, else report all odd
items = [1, 3, 4, 7]

for i in items:
    if i % 2 == 0:
        print("Even number found:", i)
        break
else:
    print("All numbers are odd")
# Output: Even number found: 4


# ============================================================================
# 4. REAL-WORLD APPLICATIONS - FOR-ELSE
# ============================================================================

# --- Task 1: Check for Missing Names ---
# Stop as soon as a None is found — else means all names exist

names = ['Kamara', 'Tuba', None, 'Mounika']

for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")
# Output: Found a missing name


# --- Task 2: Verify All Files Are CSV ---
# Stop as soon as a non-CSV is found — else means all files passed

files = [
    'data1.csv',
    'report.pdf',
    'data2.txt',
    'report2.csv'
]

for file in files:
    if not file.endswith('.csv'):
        print("Not all files are CSV")
        break
else:
    print("All files are CSV")
# Output: Not all files are CSV


# ============================================================================
# 5. CHALLENGE - Duplicate File Detector
# ============================================================================
"""
================================================================================
CHALLENGE: Check whether any filename appears more than once

Given:
    file_list = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']

Requirements:
    - If a duplicate filename exists, print: "Duplicate found"
    - Otherwise, print: "All files are unique"

Bonus:
    - Stop checking as soon as the first duplicate is found
    - Solve using a for loop with break and else
================================================================================
"""

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',   # ← duplicate
    'data.csv'
]

seen = []

for file in file_list:
    if file in seen:
        print("Duplicate found:", file)
        break
    seen.append(file)
else:
    print("All files are unique")
# Output: Duplicate found: report.csv


# ============================================================================
# 6. NESTED LOOPS - A LOOP INSIDE A LOOP
# ============================================================================

# A nested loop places one loop inside the body of another loop.
# For every SINGLE step of the outer loop, the inner loop runs its ENTIRE cycle.

"""
================================================================================
   CODE & OUTPUT                           BEHIND THE SCENES (NESTED LOOPS)
================================================================================

  [ Python Code ]                                [ 1 | 2 | 3 ] 
  +-----------------------+                            ^       
  | for x in (1, 2, 3):   |                            |       
  |     for y in (1, 2):  |          Start             |
  |         print(x, y)   |            |               |
  +-----------------------+            | <-------------------------------------------------------------+
                                       v                                                               |
  [ Output ]                       +--------+        False                                             |
  +-----------------------+        | Last   | ----------------------->  Start                          |
  | 1  1                  |        |   ?    |                             |          [ 1 | 2 ]         |
  | 1  2                  |        +--------+                             |              ^             |
  | 2  1                  |            |                                  | <---------+  |             |
  | 2  2                  |            | True                             |           |                |
  | 3  1                  |            |                                  v           |                |
  | 3  2                  |            |                              +--------+      |                |
  +-----------------------+            |                              | Last   |      |   +----------+ |
                                       |                              |   ?    | -False-> |print(x,y)| |
                                       |                              +--------+          +----------+ |
                                       |                                  |                            |
                                       |                                  | True                       |
                                       |                                  v                            |
                                       |                                 End                           |
                                       |                                  |                            |
                                       v                                  |                            |
                                      End                                 +----------------------------+

--------------------------------------------------------------------------------
Key Concept:
    • For every 1 step of the outer loop, the inner loop runs completely
    • Each loop has its own independent iterator and position tracker
    • If outer has X items and inner has Y items → inner body runs X × Y times
    • After each outer step, the inner loop fully resets from scratch
================================================================================
"""

# Basic example: two levels
for x in range(3):      # outer loop
    for y in range(2):  # inner loop
        print(f"({x}, {y})")
# Output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)


# Three levels deep
for x in range(3):      # outer loop
    for y in range(2):  # middle loop
        for z in range(2):  # inner loop
            print(f"({x}, {y}, {z})")
# Output: (0,0,0) (0,0,1) (0,1,0) ... (2,1,1)


# ============================================================================
# 7. NESTED LOOPS - APPLICATION 1: CROSSING DATA (Combinations)
# ============================================================================

# Use nested loops to pair every item from one list with every item in another.

"""
================================================================================
   CROSSING DATA - ALL POSSIBLE COMBINATIONS
================================================================================

      List A (Outer)                        List B (Inner)
    +-------------------+                 +-------------------+
    |      [ A1 ]       | --------------> |      ( B1 )       | → (A1, B1)
    |                   | ------+-------> |      ( B2 )       | → (A1, B2)
    |      [ A2 ]       | --------------> |      ( B1 )       | → (A2, B1)
    |                   | ------+-------> |      ( B2 )       | → (A2, B2)
    |      [ A3 ]       | --------------> |      ( B1 )       | → (A3, B1)
    |                   | ------+-------> |      ( B2 )       | → (A3, B2)
    +-------------------+                 +-------------------+

    Total combinations = len(A) × len(B) = 3 × 2 = 6
================================================================================
"""

# Real example: product catalog — every color paired with every size
colors = ['red', 'blue', 'green']
sizes  = ['L',   'M',   'S'  ]

for color in colors:
    for size in sizes:
        print(f'{color} - Size {size}')
# Output:
# red - Size L
# red - Size M
# red - Size S
# blue - Size L
# ... (9 combinations total)


# ============================================================================
# 8. NESTED LOOPS - APPLICATION 2: NAVIGATE HIERARCHY (Time Series)
# ============================================================================

# Use nested loops to drill through hierarchical structures like time periods.

"""
================================================================================
   3-LEVEL HIERARCHY - TIME SERIES STRUCTURE
================================================================================

  [ Python Code ]                                            ( Start )
          for year in years:                     [ 2026 ]                  [ 2027 ]               <- Level 1
                                                /    |    \                /    |    \ 
              for month in months:           Jan    Feb    Mar          Jan    Feb    Mar         <- Level 2
                                             /|\    /|\    /|\          /|\    /|\    /|\ 
                  for day in days:          1 2 3  1 2 3  1 2 3        1 2 3  1 2 3  1 2 3        <- Level 3
                      Do Something(Action)

  Action: generate report filename for every (year, month, day)
================================================================================
"""

years  = [2026, 2027]
months = ['Jan', 'Feb']
days   = range(1, 29)

for y in years:
    for m in months:
        for d in days:
            print(f'report_{y}_{m}_{d}.csv')
# Output:
# report_2026_Jan_1.csv
# report_2026_Jan_2.csv
# ... (112 filenames total)


# ============================================================================
# 9. NESTED LOOPS - APPLICATION 3: DATABASE METADATA PIPELINE
# ============================================================================

# Use nested loops to generate SQL queries automatically across tables and columns.
# This is the foundation of metadata-driven data pipelines.

"""
================================================================================
   DRILL-DOWN: Tables → Columns → Rows
================================================================================

  [ Python Code ]                                   Table                          Table 
                                                +---+---+---+                  +---+---+---+ 
                                                | ~ | ~ | ~ |                  | ~ | ~ | ~ | 
      for table in tables:   ---------------->  +---+---+---+                  +---+---+---+ 
                                                | ~ | ~ | ~ |                  | ~ | ~ | ~ | 
                                                +---+---+---+                  +---+---+---+ 
                                                   /  |  \                        /   |   \ 
                                                 /    |    \                    /     |     \ 
        for col in columns:  ---------+        /      |      \                /       |       \ 
                                      |    Column   Column   Column         Column   Column   Column 
                                      |     +---+    +---+    +---+          +---+    +---+    +---+ 
                                      +-->  | ~ |    | ~ |    | ~ |          | ~ |    | ~ |    | ~ | 
                                            +---+    +---+    +---+          +---+    +---+    +---+ 
                                            | ~ |    | ~ |    | ~ |          | ~ |    | ~ |    | ~ | 
                                            +---+    +---+    +---+          +---+    +---+    +---+ 
          for row in rows:   ---------+      /|\      /|\      /|\            /|\      /|\      /|\ 
              Do Something            |     / | \    / | \    / | \          / | \    / | \    / | \ 
                                      |   row row row  ...     ...            ...      ...      ... 
                                      +-> [~] [~] [~]  [~][~][~] [~][~][~]    [~][~][~] [~][~][~] [~][~][~] 

  Goal: Generate one SQL NULL-check query per (table, column) combination
================================================================================
"""

tables  = ['customers', 'orders', 'products', 'prices']
columns = ['id', 'create_date']

for t in tables:
    for c in columns:
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')
# Output:
# SELECT count(*) FROM customers WHERE id IS NULL;
# SELECT count(*) FROM customers WHERE create_date IS NULL;
# SELECT count(*) FROM orders WHERE id IS NULL;
# SELECT count(*) FROM orders WHERE create_date IS NULL;
# ... (8 queries total — 4 tables × 2 columns)


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
FOR-ELSE AND NESTED LOOPS - ESSENTIAL FACTS

for-else (The "No-Break" Clause):
    • else runs ONLY if the loop finishes naturally (no break fired)
    • Think of it as: "if no break happened, then do this"
    • If break fires → else is completely skipped
    • Only useful when combined with a break inside the loop
    • Without a break, else always runs → just write it after the loop

The Search Pattern:
    for item in collection:
        if condition_met:
            # handle found case
            break
    else:
        # handle not-found case (only runs if no break fired)

Nested Loops:
    • A loop placed inside the body of another loop
    • Outer loop runs once → inner loop runs its entire cycle → repeat
    • Each loop has its own independent iterator
    • Execution count: outer items × inner items
    • Inner loop fully resets at each outer step

Nested Loop Use Cases:
    • Crossing data      → pair every item from A with every item from B
    • Time hierarchies   → years → months → days (report generation)
    • Database pipelines → tables → columns → rows (SQL generation)
    • File systems       → folders → subfolders → files
    • Grids/matrices     → rows → columns → cells

Important Notes:
    • Only use for-else when break exists inside the loop
    • Nested loops can go 3+ levels deep but become harder to read
    • Inner body execution = outer_count × inner_count × deeper_count
    • Nested loops are the foundation of metadata-driven pipelines
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ What for-else means: else runs only if no break fired (the "no-break" clause)
✓ Why else without break is pointless — just write it after the loop
✓ The search pattern: break = found, else = not found
✓ Real-world use 1: detecting None values in a list
✓ Real-world use 2: verifying all files are a specific type
✓ Challenge: duplicate file detector using seen list + break + else
✓ What a nested loop is: inner loop runs fully for every outer step
✓ Execution count formula: outer × inner (× deeper for 3+ levels)
✓ That each loop has its own independent iterator and position
✓ Nested loop use 1: crossing data — all color × size combinations
✓ Nested loop use 2: time hierarchy — years → months → days
✓ Nested loop use 3: database pipeline — tables → columns → SQL queries
✓ Why nested loops matter for data engineering: automated, scalable pipelines
"""