"""
================================================================================
PYTHON LOOPS - PART 2: BREAK, CONTINUE, AND PASS
================================================================================
Learning Focus: Controlling loop flow with break, continue, and pass
"""


# ============================================================================
# 1. FOR LOOP RECAP - QUICK FLOWCHART
# ============================================================================
"""
================================================================================
                             FOR LOOP FLOWCHART
================================================================================

         Start
           |
           | <------------------------------------+
           v                                      |
   +---------------+            False    +---------------+
   |  Last item?   | -----------------> |   Print (i)   |
   +---------------+                    +---------------+
           |
           | True
           v
          End

--------------------------------------------------------------------------------
Code:
    for i in (1, 2, 3):
        print(i)
================================================================================
"""


# ============================================================================
# 2. LOOP CONTROL STATEMENTS - OVERVIEW
# ============================================================================
"""
=================================================================================================
  1. BREAK (When to stop?)     | 2. CONTINUE (When to skip?)    | 3. PASS (When to pass?)
=================================================================================================

         [Start]                        [Start]                          [Start]
            |                              |                                |
            v                              v                                v
    +---> (Loop)                   +---> (Loop) <---------+         +---> (Loop)
    |       |                      |       |              |         |       |
    |       v                      |       v              |         |       v
    |     < ? > --Yes--> [break]   |     < ? > --Yes--> [continue]  |     < ? > --Yes--> [pass]
    |       |              |       |       |                        |       |              |
    |       No             v       |       No                       |       No             |
    |       v            (End)     |       v                        |       v              |
    +--- [Code]                    +--- [Code]                      +--- [Code] <----------+

-------------------------------------------------------------------------------------------------
Key Differences:
    • break    → Exits the loop entirely and immediately (Stop)
    • continue → Skips the current iteration and jumps back to loop start (Skip)
    • pass     → Does nothing, acts as a placeholder, moves to the next line (Pass)
=================================================================================================
"""


# ============================================================================
# 3. BREAK - Emergency Exit
# ============================================================================

# break stops the loop immediately.
# It jumps out and ends the loop right away.
# Think of it as an "emergency exit."

"""
================================================================================
   CODE & OUTPUT                              BEHIND THE SCENES (BREAK)
================================================================================

  [ Python Code ]                                    Start
  +-----------------------+                            |
  | for i in (1, 2, 3):  |                             v
  |     if i == 2:       |              |+---------> +---------------+  True  +-----+
  |         break        |              |            |  Last item?   |------->| End |
  |     print(i)         |              |            +---------------+        +-----+
  +-----------------------+             |                   |
                                        |                 False
  [ Output ]                            |                   | "if"
  +-----------------------+             |                   v
  | 1                     |             |           +---------------+  False  +-----------+
  +-----------------------+             |           |   i == 2 ?    |-------->| print(i)  |
                                        |           +---------------+         +-----------+
                                        |                   |                       |
                                        |                  True                     |
                                        |                   v                       v
                                        |           +---------------+           (loop back)
                                        |           |     break     |
                                        |           +---------------+
                                        |                   |
                                        +------------------End

--------------------------------------------------------------------------------
Key Concept:
    • For item '1': (1 == 2) is False → print(1) → loop back
    • For item '2': (2 == 2) is True  → break fires → loop ends immediately
    • Item '3' is never reached — the loop is completely destroyed
================================================================================
"""

# Example: Stop loop when an empty value is detected
names = ['john', 'maria', '', 'omar']

for name in names:
    if name == '':
        print('Empty value detected!')
        break
    print(f'Name = {name}')
# Output:
# Name = john
# Name = maria
# Empty value detected!


# ============================================================================
# 4. CONTINUE - Skip This One, Go Next
# ============================================================================

# continue skips one loop cycle without stopping the loop.
# "Skip this one and go next."

"""
================================================================================
   CODE & OUTPUT                              BEHIND THE SCENES (CONTINUE)
================================================================================

  [ Python Code ]                                       Start
  +-----------------------+                               |
  | for i in (1, 2, 3):  |              +---------------> v <-------------------+
  |     if i == 2:       |              |            +---------------+          |
  |         continue     |              |            |  Last item?   |          |
  |     print(i)         |  +-----------|------------|  (for loop)   |          |
  +-----------------------+ |           |            +---------------+          |
                            |           |                    |                  |
  [ Output ]                |           |                  False                |
  +-----------------------+ |           |                    |                  |
  | 1                     | |           |                    v                  |
  | 3                     | |  +----------+ True  +---------------+  False  +-----------+
  +-----------------------+ |  |continue  |<------|   i == 2 ?    |-------->| print(i)  |
                            |  +----------+       +---------------+         +-----------+
                            |       |
                            v       v
                           End   (back to Start)

--------------------------------------------------------------------------------
Key Concept:
    • For item '1': (1 == 2) is False → print(1) → loop back
    • For item '2': (2 == 2) is True  → continue fires → skip print(2) → back to start
    • For item '3': (3 == 2) is False → print(3) → loop ends normally
================================================================================
"""

# Example: Skip empty values, keep processing the rest
names = ['john', 'maria', '', 'omar']

for name in names:
    if name == '':
        print('Empty value detected!')
        continue            # Skip the empty name, keep going
    print(f'Name = {name}')
# Output:
# Name = john
# Name = maria
# Empty value detected!
# Name = omar

# Use continue to skip bad or empty data without stopping the whole loop.


# ============================================================================
# 5. PASS - Do Nothing, Keep Going
# ============================================================================

# pass is a placeholder where nothing happens.
# "For now... just keep going. Do nothing."
# Used during the planning phase when structure exists but logic doesn't.

"""
================================================================================
   CODE & OUTPUT                              BEHIND THE SCENES (PASS)
================================================================================

  [ Python Code ]                                       Start
  +-----------------------+                               |
  | for i in (1, 2, 3):  |                               v <--------------------+
  |     if i == 2:       |                       +---------------+               |
  |         pass         |               True    |  Last item?   |               |
  |     print(i)         |        +--------------|  (for loop)   |               |
  +-----------------------+       |              +---------------+               |
                                  |                      |                       |
  [ Output ]                      |                    False                     |
  +-----------------------+       |                      |                       |
  | 1                     |       |                      v                       |
  | 2                     |       |              +---------------+               |
  | 3                     |       |        True  |   i == 2 ?    |  False        |
  +-----------------------+       |   +----------| (Condition)   |----------+    |
                                  |   |          +---------------+          |    |
                                  |   v                                     v    |
                                  | +------+                          +-----------+
                                  | | pass |                          | print(i)  |
                                  | +------+                          +-----------+
                                  |   |                                     |
                                  |   +-------------------------------------+
                                  v
                                 End

--------------------------------------------------------------------------------
Key Concept:
    • pass does absolutely nothing when executed
    • When i == 2: condition is True → pass runs → no change to flow
    • Execution continues to the next line: print(i)
    • So 1, 2, and 3 all print normally — pass never interrupted anything
================================================================================
"""

# Example: Placeholder while planning how to handle empty values
names = ['john', 'maria', '', 'omar']

for name in names:
    if name == '':
        # TODO: Handle empty value properly later
        name = name.replace('', 'unknown')
    print(f'Name = {name}')
# Output:
# Name = john
# Name = maria
# Name = unknown
# Name = omar


# ============================================================================
# 6. REAL-WORLD APPLICATIONS
# ============================================================================

# --- Task 1: Skip Weekends (continue) ---
# Loop through a list of days and print only working days,
# skipping the weekends.

days     = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']

for day in days:
    if day in weekends:
        continue            # Skip this day, it's a weekend
    print(f'Workday: {day}')
# Output:
# Workday: Mon
# Workday: Wed
# Workday: Tue


# --- Task 2: Detect SQL Injection and Stop (break) ---
# Scan emails to block unsafe data from entering your system.
# Stop processing immediately when a threat is detected.

emails = [
    'data@gmail.com',
    'baraa@outlook.de',
    'DROP TABLE USERS;',    # ← SQL injection attempt
    'maria@gmail.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection detected: Hacker Attack!')
        break               # Stop everything — security threat found
    print(f'Processing Email: {email}')
# Output:
# Processing Email: data@gmail.com
# Processing Email: baraa@outlook.de
# SQL Injection detected: Hacker Attack!


# ============================================================================
# 7. BREAK VS CONTINUE VS PASS - FULL COMPARISON
# ============================================================================
"""
========================================================================================================
    [ break ]                     [ continue ]                       [ pass ]
========================================================================================================
    Exit immediately              Skip 1 iteration                   Do Nothing
--------------------------------------------------------------------------------------------------------
  [ ~ ] |                       [ ~ ] |                              [ ~ ] |
  [ ~ ] |                       [ ~ ] |                              [ ~ ] |
  [ X ] +-----> (Stop!)         [ X ] +---+  (Skip loop body)        [ ~ ] +-----> (Keep going)
  [ X ]                         [ ~ ]     |                          [ ~ ] |
  [ X ]                         [ ~ ] <---+                          [ ~ ] v

  Risk Level: CRITICAL           Risk Level: MEDIUM                  Risk Level: NONE
  Use for:                       Use for:                            Use for:
    • Security threats             • Empty or bad rows                 • Future planning
    • Cost control                 • Empty files or data               • Placeholder logic
    • Data integrity               • Skip special cases                • Skeleton code

========================================================================================================
"""


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
BREAK, CONTINUE, PASS - ESSENTIAL FACTS

What They Are:
    Loop control statements that modify how a for or while loop executes.

break:
    • Exits the entire loop immediately
    • Remaining iterations are never executed
    • Use when: a critical condition is met (security, error, integrity risk)

continue:
    • Skips the rest of the current iteration only
    • Loop continues to the next item normally
    • Use when: filtering bad, empty, or irrelevant data

pass:
    • Does absolutely nothing
    • Loop continues exactly as if pass wasn't there
    • Use when: you need a structural placeholder while planning logic

Quick Decision Guide:
    "Do I need to stop everything?"  → break
    "Do I need to skip just this?"   → continue
    "Do I need to plan for later?"   → pass

Real-World Use Cases:
    • break    → SQL injection detected → stop processing all emails
    • continue → empty row found        → skip it, keep processing rest
    • pass     → logic not written yet  → placeholder, move on for now
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ What loop control statements are and why they matter
✓ How break exits the entire loop immediately when triggered
✓ How continue skips only the current iteration and resumes from the next
✓ How pass acts as a silent placeholder that doesn't affect loop flow
✓ The critical difference: break = stop all, continue = skip one, pass = nothing
✓ Real-world use of break: detecting SQL injection and halting processing
✓ Real-world use of continue: skipping weekends or empty data rows
✓ Real-world use of pass: placeholder during code planning phase
✓ The risk levels: break (critical), continue (medium), pass (none)
✓ How to read and trace loop control flowcharts step by step
"""