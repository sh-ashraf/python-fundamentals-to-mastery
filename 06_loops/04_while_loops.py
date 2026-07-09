"""
================================================================================
PYTHON LOOPS - PART 4: WHILE LOOPS
================================================================================
Learning Focus: While loop mechanics, the two while patterns (condition vs true), infinite loop prevention, and for vs while comparison
"""


# ============================================================================
# 1. WHAT IS A WHILE LOOP?
# ============================================================================

# A while loop repeats a block of code over and over
# as long as a condition remains True.

# Unlike a for loop (which iterates over a fixed sequence),
# a while loop runs based on YOUR condition — not a predefined list.
# This gives more flexibility but introduces the risk of infinite loops.


# ============================================================================
# 2. FOR LOOP VS WHILE LOOP - FULL COMPARISON
# ============================================================================
"""
================================================================================
   FOR LOOP (The Predictable Path)    vs    WHILE LOOP (The Risky Path)
================================================================================

  for i in [1, 2, 3]:                       while i < 4:
      print(i)                                   print(i)

  [ Behind the Scenes ]                     [ Behind the Scenes ]

        Start                                          Start
          |                                              |
  +---------------+                                     v <--------------+
  |  Iterator     |                             +---------------+        |
  | [ 1 | 2 | 3 ] |                   Your -->  |  Condition ?  |        |
  +---------------+                   Condition +---------------+        |
          |                                      True |    | False       |
          v <-----------------------+                 v    v             |
  +---------------+                 |             [Code]  End            |
  |  Last item?   | ----False---> [Code]              |                  |
  +---------------+                 |                 v                  |
          |                         |           +----------+             |
        True                        |           |  i += 1  | -----------+
          |                         |           +----------+
          v                         |
         End                        |
  (Auto-stops when items run out) --+    (Warning: Infinite loop if not updated!)

--------------------------------------------------------------------------------
                          QUICK COMPARISON (Cheat Sheet)
--------------------------------------------------------------------------------

  Feature            FOR Loop                           WHILE Loop
  ─────────────────  ────────────────────────────────   ──────────────────────────────────
  Loop over          Fixed sequence (predefined)        Your condition (True/False)
  Nr. of iterations  Known in advance                   Unknown (depends on event)
  Progression        Automatic (gets next item auto)    Manual (you MUST update variables)
  Primary risk       Low (safe and predictable)         High (infinite loops crash programs)
  Best used for      "Processing Data"                  "Waiting for External Event"
  Style              Simple / Clear / Safe / Limited    Advanced / Flexible / Complex / Risk

--------------------------------------------------------------------------------
  FOR  →  Loop over a fixed sequence   →  Predefined condition
  WHILE → Loop while a condition is True → Your condition
================================================================================
"""


# ============================================================================
# 3. WHILE CONDITION - The Classic Pattern
# ============================================================================

# Three pillars of every while loop:
#   1. Initialization  → set up a tracker variable BEFORE the loop
#   2. Condition       → the "gatekeeper" — checked before every cycle
#   3. Update          → manually change the tracker inside the loop body
#                        (forget this → infinite loop → program crashes!)

"""
================================================================================
   CODE & OUTPUT                          BEHIND THE SCENES (WHILE ANATOMY)
================================================================================

  [ Python Code ]               Initialization → [ i = 1 ]
                                                       |
  i = 1                                                v
  while i < 4:                                      (Start)
      print(i)                                         |
      i += 1                                           v <--------------------+
                                               +---------------+              |
                                     False     |    i < 4 ?    |              |
  [ Output ]                       +---------- +---------------+              |
  +-----------------------+        |                   |                      |
  | 1                     |        |                 True                     |
  | 2                     |        |                   |                      |
  | 3                     |        |                   v                      |
  +-----------------------+        |            +-------------+               |
                                   |            |  print(i)   |               |
                                   |            +-------------+               |
                                   |                   |                      |
                                   |                   v                      |
                                   |            +-------------+               |
                                   |            |   i += 1    | -------------+
                                   |            +-------------+
                                   v
                                  End

--------------------------------------------------------------------------------
  Exits Normally → Condition becomes False
  Safer + More Readable
  Best for: Counter, Limited Retries
--------------------------------------------------------------------------------
Key Concept - The 3 Pillars:
    1. Initialization (i = 1) → set up a starting variable BEFORE the loop
    2. Condition    (i < 4)  → checked before every cycle (True=run, False=end)
    3. Update      (i += 1) → CRITICAL: change the tracker or loop runs forever!
================================================================================
"""

count = 1           # 1. Initialization
while count <= 10:  # 2. Condition
    print(f"Value of count is: {count}")
    count += 2      # 3. Update (skips every other number: 1, 3, 5, 7, 9)
# Output:
# Value of count is: 1
# Value of count is: 3
# Value of count is: 5
# Value of count is: 7
# Value of count is: 9


# ============================================================================
# 4. WHILE CONDITION - Practical Example
# ============================================================================

# Task: Keep asking "Do you agree?" until the user types "yes"

answer = ""                         # Initialization (empty to enter loop)
while answer != "yes":              # Condition
    answer = input("Do you agree? (yes/no): ")
print("Thank You")
# Output (if user types "no", "no", "yes"):
# Do you agree? (yes/no): no
# Do you agree? (yes/no): no
# Do you agree? (yes/no): yes
# Thank You


# ============================================================================
# 5. WHILE TRUE - The "Do-While" Pattern
# ============================================================================

# while True creates an intentionally infinite loop.
# The ONLY exit is a manual break triggered by an if condition inside.
# This ensures the loop body runs AT LEAST ONCE before checking the exit.

"""
================================================================================
   CODE & OUTPUT                        BEHIND THE SCENES (WHILE TRUE + BREAK)
================================================================================

  [ Python Code ]                                   Start
                                                      |
  while True:                                         v <-----------------------+
      Do Something                            +---------------+                 |
                                              |     True      | ←── always True |
      if x == 'stop':                         +---------------+                 |
          break                                       |                         |
                                                    True                        |
                                                      |                         |
                                                      v                         |
                                              +---------------+                 |
                                              | Do Something  |                 |
                                              +---------------+                 |
                                                      |                         |
                                                      v                         |
                                              +---------------+                 |
                                              | x == 'stop' ? | ----False------+
                                              +---------------+
                                                      |
                                                    True
                                                      |
                                                      v
                                                +-----------+
                                            [-] |   break   |
                                                +-----------+
                                                      |
                                                      v
                                                     End

--------------------------------------------------------------------------------
  Must have extra: if + break
  Risk of infinite loop + More Flexible
  Open-ended: waiting → Database / Stream / API
--------------------------------------------------------------------------------
Key Concept - The "Do-While" Pattern:
    • while True runs forever — the top condition is hardcoded True
    • The ONLY way out is a break inside an if condition in the body
    • Forces the loop body to execute AT LEAST ONCE before checking exit
    • Standard Python way to emulate a "do-while" loop
    • Use for: user login prompts, continuous data streams, game main loops
================================================================================
"""

while True:
    answer = input("Do you agree? (yes/no): ")

    if answer == "yes":
        break

print("Thank You")
# Output (if user types "no", "no", "yes"):
# Do you agree? (yes/no): no
# Do you agree? (yes/no): no
# Do you agree? (yes/no): yes
# Thank You


# ============================================================================
# 6. WHILE CONDITION vs WHILE TRUE - QUICK COMPARISON
# ============================================================================
"""
================================================================================
  WHILE CONDITION                    vs    WHILE TRUE
================================================================================

  while i < 4:                             while True:
      print(i)                                 x = input("Type: ")
      i += 1                                   if x == "stop":
                                                   break

  Exits Normally → Condition = False       Must have extra: if + break

  Safer + More Readable                    Risk of infinite loop + More Flexible

  Best for:                                Best for:
    • Counter                                • Database polling
    • Limited retries                        • Data stream reading
                                             • API waiting
                                             • Game loops

================================================================================
"""


# ============================================================================
# 7. CHALLENGE - Agreement Confirmation with Limited Attempts
# ============================================================================
"""
================================================================================
CHALLENGE: Ask the user for agreement with a maximum of 3 attempts

Requirements:
    - Allow the user up to 3 attempts
    - If the user types "yes" → print: "Glad we're on the same page"
    - Stop asking immediately after a valid "yes" answer
    - If the user fails to type "yes" after 3 attempts → print: "3 Strikes, You're Out!"

Hint: Uses while-else — else runs only if no break fired
================================================================================
"""

attempts = 0                         # 1. Initialization

while attempts < 3:                  # 2. Condition (max 3 tries)
    answer = input("Do you agree? (yes/no): ")

    if answer == "yes":
        print("Glad we're on the same page")
        break                        # Exit immediately — success

    attempts += 1                    # 3. Update (count the failed attempt)

else:
    print("3 strikes. You're out!")  # Runs only if loop exhausted naturally (no break)

# Output (if user types "no", "no", "no"):
# Do you agree? (yes/no): no
# Do you agree? (yes/no): no
# Do you agree? (yes/no): no
# 3 strikes. You're out!

# Output (if user types "no", "yes"):
# Do you agree? (yes/no): no
# Do you agree? (yes/no): yes
# Glad we're on the same page


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
WHILE LOOPS - ESSENTIAL FACTS

What is a While Loop?
    • Repeats a block of code as long as a condition is True
    • Unlike for loops, iteration count is UNKNOWN (depends on external event)
    • You define the condition — "your condition", not a predefined sequence

The 3 Pillars (for while condition pattern):
    1. Initialization → set up tracker variable BEFORE the loop
    2. Condition      → checked before every cycle (gatekeeper)
    3. Update         → MUST manually change tracker inside loop body
                        (forgetting this = infinite loop = crash!)

Two While Patterns:

    while condition:           →  Exits normally when condition becomes False
        code                      Safer, more readable
        update                    Best for: counters, limited retries

    while True:                →  Runs forever — MUST use break to exit
        code                      More flexible, higher risk
        if condition:             Best for: user input, streams, APIs, games
            break

While + Else:
    • else in a while loop runs only if the loop exits naturally (no break)
    • Same "no-break" clause as for-else
    • Perfect for: "max attempts" patterns

For vs While:
    • For  → fixed sequence, known count, "Processing Data"
    • While → your condition, unknown count, "Waiting for External Event"

Important Notes:
    • Always include an update step in while condition loops
    • Always include a break exit in while True loops
    • while True is the Pythonic way to simulate a "do-while" loop
    • Combining while with else adds a clean "failed all attempts" handler
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ What a while loop is and how it differs from a for loop
✓ The key distinction: for = fixed sequence (known), while = your condition (unknown)
✓ The 3 pillars of a while loop: initialization, condition, update
✓ That forgetting the update step causes an infinite loop and crashes the program
✓ The "while condition" pattern — exits naturally when condition becomes False
✓ The "while True" pattern — intentional infinite loop that requires a break to exit
✓ When to use while condition (counter, retries) vs while True (streams, APIs, input)
✓ How while True simulates a "do-while" loop (body runs at least once)
✓ How to combine while with else for the "max attempts" pattern
✓ That while-else works the same as for-else: else skipped if break fires
✓ The full for vs while comparison: safety, flexibility, use cases, risk level
✓ Challenge: 3-attempt agreement loop using while + else + break + counter
"""