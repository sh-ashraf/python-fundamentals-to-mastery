"""
================================================================================
PYTHON CONDITIONAL STATEMENTS - PART 1: IF, ELSE, ELIF
================================================================================
Learning Focus: Understanding conditional logic and decision-making in Python
"""


# ============================================================================
# 1. WHAT ARE CONDITIONAL STATEMENTS?
# ============================================================================
"""
Conditional Statements:
    A checkpoint that checks a condition
    - ✅ True?  Runs the code
    - ❌ False? Skip it
    🚦 Think of it like a traffic light 🚦

================================================================================
   STRAIGHT LINE CODE             VS           CONDITIONAL STATEMENT
================================================================================

         Start                                        Start
           |                                            |
           v                                            v
   +------------------+                        +------------------+
   |    Statement 1   |                        |   Input / Data   |
   +------------------+                        +------------------+
           |                                            |
           v                                            v
   +------------------+                        +------------------+
   |   Statement 2    |                        |    Condition ?   |
   +------------------+                        +------------------+
           |                                      /              \
           v                                 True                False
   +------------------+                       |                    |
   |   Statement 3    |                       v                    v
   +------------------+              +------------------+  +------------------+
           |                         |   True Block     |  |   False Block    |
           v                         +------------------+  +------------------+
   +------------------+                      |                       |
   |   Statement 4    |                      |                       |
   +------------------+                       \                     /
           |                                   \                   /
           v                                    v                 v
   +------------------+                        +------------------+
   |   Statement 5    |                        | Continue Program |
   +------------------+                        +------------------+
          |                                            |
          v                                            v
         End                                          End

--------------------------------------------------------------------------------
Key Difference:
    • Straight-line code runs every statement, top to bottom, no matter what.
    • Conditional code makes a decision and chooses a path based on a condition.
================================================================================
"""


# ============================================================================
# 2. STANDALONE IF STATEMENT
# ============================================================================

# --- Syntax ---
# if condition_1:
#     do A

# Defines the first condition:
# "If this is true, do this — otherwise, do nothing."

"""
================================================================================
                         SIMPLE IF STATEMENT FLOWCHART
================================================================================

                              [Start]
                                 |
    Question              +------v------+
    Boolean Expression -> |     if ?    | ---- True ----> [    A    ]
    Condition             +-------------+                 (Do Something)
                                 |                               |
                                 | False                         |
                            (Do Nothing)                         |
                                 |                               |
                                 v                               v
                               [End] <---------------------------+

--------------------------------------------------------------------------------
Explanation:
    • The program checks a condition.
    • If the condition is True, it executes A (Do Something).
    • If the condition is False, it does nothing.
    • Then the flow ends.
================================================================================
"""

# --- if Rules ---
"""
1. Only one if        → A code block uses exactly one if to start the chain
2. Starts with if     → Every conditional chain must begin with if
3. Condition required → if must always be followed by a condition
4. Can stand alone    → if can be used by itself, without elif or else
"""

score = 100

if score >= 90:
    print("A")
# Output: A


# IMPORTANT - Python Indentation:
# Adding spaces at the beginning of a line shows that the line belongs
# to a code block. This applies to: if, for, while, def, class


# ============================================================================
# 3. TWO-WAY DECISION - if / else
# ============================================================================

# --- Syntax ---
# if condition_1:
#     do A
# else:
#     do B

# else runs only if the if condition is False.
# "If this is true, do A — otherwise, do B."

"""
================================================================================
                          IF / ELSE - GRADE FLOWCHART
================================================================================

                              [Start]
                                 |
                                 v
                           [ if >= 90 ]
                          /            \
                   False /              \ True
                        /                \
                      [ F ]            [ A ]
                     (else)              |
                        \                /
                         \              /
                          v            v
                              [End]

--------------------------------------------------------------------------------
Explanation:
    • If score is greater than or equal to 90, the grade will be A.
    • Otherwise, the grade will be F.
================================================================================
"""

# --- else Rules ---
"""
1. Comes at the end   → else is always the last block in the chain
2. No conditions      → else never takes a condition of its own
3. Optional           → A program can have if without else
4. Cannot stand alone → else must always follow an if (or if/elif)
5. Only one else      → A conditional chain can have at most one else
"""

score = 50

if score >= 90:
    print("A")
else:
    print("F")
# Output: F

# Key Notes:
# - else cannot be used on its own
# - else is optional
# - else must always come at the end


# ============================================================================
# 4. MULTI-CONDITION - if / elif / else
# ============================================================================

# --- Syntax ---
# if condition_1:
#     do A
# elif condition_2:
#     do C
# else:
#     do B

# elif asks a follow-up question that only runs if the previous
# condition was False: "If the first wasn't true, try this one."

"""
================================================================================
                       IF / ELIF / ELSE - GRADE FLOWCHART
================================================================================

                           [Start]
                              |
                              v
                        [ if >= 90 ]
                       /            \
                False /              \ True
                     /                \
              [ elif >= 80 ]         [ A ]
               /        \              |
        False /          \ True        |
             /            \            |
           [ F ]          [ B ]        |
          (else)           |           |
             \             |           /
              \            |          /
               \           v         /
                +-------> [End] <---+

--------------------------------------------------------------------------------
Explanation:
    1) If the score is 90 or more  → assign grade A
    2) Else if the score is 80+    → assign grade B
    3) Otherwise                   → assign grade F
================================================================================
"""

# --- elif Rules ---
"""
1. Comes after if     → elif always follows an if block
2. Multiple elif      → A chain can have many elif blocks
3. Needs a condition  → Unlike else, elif always requires a condition
4. Optional           → A program can use if/else without any elif
5. Cannot stand alone → elif must always follow an if
"""

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
# Output: B


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
CONDITIONAL STATEMENTS - ESSENTIAL FACTS

What They Do:
    • Check a condition and decide which block of code to run
    • True  → run the matching block
    • False → skip it (or check the next condition)

Three Building Blocks:
    • if     → the starting condition (required, only one per chain)
    • elif   → an additional condition (optional, can repeat many times)
    • else   → the fallback with no condition (optional, only one, must be last)

Quick Reference:

    ┌─────────┬──────────────┬───────────┬──────────────┬──────────────────┐
    │ Keyword │ Condition    │ Required  │ Standalone   │ How Many         │
    ├─────────┼──────────────┼───────────┼──────────────┼──────────────────┤
    │ if      │ Yes          │ Yes       │ Yes          │ Exactly one      │
    │ elif    │ Yes          │ No        │ No           │ As many as needed│
    │ else    │ No           │ No        │ No           │ At most one      │
    └─────────┴──────────────┴───────────┴──────────────┴──────────────────┘

Indentation:
    • Python uses indentation (spaces) to define code blocks
    • Applies to: if, elif, else, for, while, def, class

Important Notes:
    • elif and else can never stand alone — they must follow an if
    • else never takes a condition
    • Only the FIRST true condition in a chain runs — the rest are skipped
    • A chain checks conditions top to bottom, in order
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ What conditional statements are and why they matter (checkpoints in code)
✓ The difference between straight-line code and conditional code
✓ How a standalone if statement works and its four rules
✓ How if/else creates a two-way decision
✓ The rules for else: optional, no condition, only one, must come last
✓ How if/elif/else builds a multi-way decision chain
✓ The rules for elif: needs a condition, can repeat, cannot stand alone
✓ How Python uses indentation to define code blocks
✓ How to trace a grade-calculation example through a flowchart
✓ That only the first matching condition in a chain executes
"""