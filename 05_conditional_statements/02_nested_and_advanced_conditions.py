"""
================================================================================
PYTHON CONDITIONAL STATEMENTS - PART 2: NESTED AND ADVANCED CONDITIONS
================================================================================
Learning Focus: Multi-elif chains, nested if statements, logical operators in
                conditions, and independent if blocks
"""


# ============================================================================
# 1. MULTI-ELIF CHAIN - if / elif / elif / else
# ============================================================================

# When you need more than two possible outcomes, add as many elif blocks
# as needed. Python checks each condition top to bottom and runs the first
# one that is True. All others are skipped.

"""
================================================================================
                     IF / ELIF / ELIF / ELSE FLOWCHART
================================================================================

                               [Start]
                                  |
                            [ if >= 90 ]
                           /            \
                    False /              \ True
                         /                \
                  [ elif >= 80 ]          [ A ]
                   /        \
            False /          \ True
                 /            \
          [ elif >= 70 ]      [ B ]
           /        \
    False /          \ True
         /            \
       [ F ]          [ C ]

--------------------------------------------------------------------------------
Explanation:
    1) If score is 90 or more  → grade = A
    2) Else if score is 80+    → grade = B
    3) Else if score is 70+    → grade = C
    4) Otherwise               → grade = F
================================================================================
"""


# ============================================================================
# 2. MULTI-ELIF EXAMPLES
# ============================================================================

# --- Example 1: Student Grades ---
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
# Output: Your grade is: B


# --- Example 2: HTTP Status Codes ---
status = 200

if status == 200:
    print("200 - OK")
elif status == 201:
    print("201 - Created")
elif status == 400:
    print("400 - Bad Request")
elif status == 404:
    print("404 - Not Found")
else:
    print("Unknown Status Code")
# Output: 200 - OK


# --- Example 3: User Roles ---
role = "Admin"

if role == "Admin":
    print("Welcome Admin")
elif role == "Moderator":
    print("Welcome Moderator")
elif role == "Editor":
    print("Welcome Editor")
elif role == "Member":
    print("Welcome Member")
else:
    print("Unknown Role")
# Output: Welcome Admin


# ============================================================================
# 3. NESTED IF - if Inside Another if
# ============================================================================

# A nested if is an if statement placed inside another if block.
# "If the first condition is True, then check the second condition."
# The inner if only runs if the outer if was already True.

"""
================================================================================
                     NESTED IF + ELIF / ELSE FLOWCHART
================================================================================

                               [Start]
                                  |
                            [ if >= 90 ]
                           /            \
                    False /              \ True
                         /                \
                  [ elif >= 80 ]      [ if Project? ]
                   /        \            /        \
            False /          \ True     / False    \ True
                 /            \        /            \
          [ elif >= 70 ]      [ B ]  [ A ]         [ A+ ]
           /        \
    False /          \ True
         /            \
       [ F ]          [ C ]

    Note: Each outer if can contain its own inner if/else

--------------------------------------------------------------------------------
Explanation:
    1) If score >= 90:
          Check inner condition: submitted_project
          - If submitted_project is True  → grade = A+
          - Else                          → grade = A
    2) Else if score >= 80:
          grade = B
    3) Else if score >= 70:
          grade = C
    4) Else:
          grade = F
================================================================================
"""

score = 95
submitted_project = True

if score >= 90:
    if submitted_project:       # Inner condition checked only if score >= 90
        grade = "A+"
    else:
        grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
# Output: Your grade is: A+


# ============================================================================
# 4. CONNECTING CONDITIONS WITH LOGICAL OPERATORS
# ============================================================================

# Instead of nesting, logical operators (and / or) allow combining
# multiple conditions into a single if statement.

"""
================================================================================
   1. AND Operator (Strict)        |        2. OR Operator (Flexible)
================================================================================

           [Start]                 |                [Start]
              |                    |                   |
              v                    |                   v
  [ if >= 90 AND Project? ]        |       [ if >= 90 OR Project? ]
         /         \               |              /         \
  False /           \ True         |       False /           \ True
       /             \             |            /             \
     [ F ]          [ A ]          |          [ F ]          [ A ]

--------------------------------------------------------------------------------
AND Explanation:                   | OR Explanation:
- MUST satisfy BOTH conditions.    | - Needs ONLY ONE condition to be True.
- Fails if even ONE is False.      | - Fails ONLY if BOTH are False.
================================================================================
"""

score = 100
submitted_project = False

if score >= 90 and submitted_project:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
# Output: Your grade is: A
# score >= 90 is True, but submitted_project is False
# AND requires both → A+ is skipped → falls to elif score >= 90 → A


# ============================================================================
# 5. INDEPENDENT IF BLOCKS - Separate Checks
# ============================================================================

# Unlike an if/elif/else chain (which stops at the first True condition),
# independent if blocks are separate statements.
# EVERY if is checked, regardless of what the others return.

"""
Each if block is fully independent — no connection between them:

    +---------------+
    |      if       |   ← Checked every time
    +---------------+
         (no link)
    +---------------+
    |      if       |   ← Also checked every time (even if the first was True)
    +---------------+
         (no link)
    +---------------+
    |      if       |   ← Also checked every time (always evaluated)
    +---------------+

================================================================================
                       INDEPENDENT IFs FLOWCHART
================================================================================

                               [Start]
                                  |
                                  v
                     [ if score >= 90 ? ]
                    /                    \
             False /                      \ True
                  /                        \
           [ Low Score ]               [ High Score ]
                  \                        /
                   \                      /
                    v                    v
                    +----→ [ Continue ]←-+
                                  |
                                  v
                     [ if submitted_project ? ]   ← Always checked
                    /                    \
             False /                      \ True
                  /                        \
    [ Not Submitted ]              [ Project Submitted ]
                  \                        /
                   +------→ [ End ] ←------+

--------------------------------------------------------------------------------
Key Difference:
    if/elif/else  → stops after the first True condition
    independent   → ALL blocks are always checked, no matter what
================================================================================
"""

score = 50
submitted_project = False

# First independent check
if score >= 90:
    print("High Score")
else:
    print("Low Score")
# Output: Low Score

# Second independent check (always runs, no matter what happened above)
if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")
# Output: Project is not submitted


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
NESTED AND ADVANCED CONDITIONS - ESSENTIAL FACTS

Multi-elif Chain:
    • Add as many elif blocks as needed
    • Python checks from top to bottom and stops at the first True
    • Use for: grade ranges, status codes, role levels

Nested if:
    • An if block placed inside another if block
    • The inner block only runs when the outer condition is already True
    • Use for: adding a second layer of checking inside a True branch

Logical Operators in Conditions:
    • and → BOTH conditions must be True to enter the block
    • or  → EITHER condition being True is enough to enter the block
    • Use to replace simple nested ifs with a single clean condition

Independent if Blocks:
    • Each if is a separate statement with no connection to the others
    • ALL blocks are always checked, even if a previous one was True
    • Use when: each condition is a separate concern that must be checked
                regardless of the others

Chained vs Independent:
    • if/elif/else → stops at first True (use when conditions are exclusive)
    • separate ifs → all always run (use when conditions are unrelated)
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to build multi-elif chains for more than two possible outcomes
✓ Real-world examples: student grades, HTTP status codes, user roles
✓ That Python checks elif conditions top to bottom and stops at the first True
✓ How nested if works: inner block only runs when outer condition is True
✓ How to use 'and' to require both conditions to be True
✓ How to use 'or' to require only one condition to be True
✓ The difference between nested if and logical operators (and/or)
✓ How independent if blocks work: all are always evaluated
✓ The key difference between if/elif/else (stops early) vs independent ifs (always runs all blocks)
✓ When to use chained conditions vs independent conditions
"""