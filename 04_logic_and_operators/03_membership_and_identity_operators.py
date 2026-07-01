"""
================================================================================
PYTHON LOGIC & OPERATORS - PART 3: MEMBERSHIP & IDENTITY OPERATORS
================================================================================
Learning Focus: Checking membership in collections and object identity in memory
"""


# ============================================================================
# 1. OPERATORS OVERVIEW
# ============================================================================
"""
┌──────────────────────┬───────────────────────┬────────────────────────────────────┐
│ Category             │ Operator              │ Purpose                            │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Membership           │ in                    │ Value EXISTS in collection         │
│ Operators            │ not in                │ Value does NOT exist               │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Identity Operators   │ is                    │ Same object in memory              │
│                      │ is not                │ Different objects in memory        │
└──────────────────────┴───────────────────────┴────────────────────────────────────┘
"""


# ============================================================================
# 2. MEMBERSHIP OPERATOR - in
# ============================================================================

# --- in Operator ---
# value in collection → Returns True if value EXISTS in the collection
# Works with: strings, lists, tuples, sets, dictionaries

# Check if character exists in a string
print("o" in "python")
# Output: True ("o" is in "python")

print("z" in "python")
# Output: False ("z" is not in "python")


# ============================================================================
# 3. MEMBERSHIP OPERATOR - not in
# ============================================================================

# --- not in Operator ---
# value not in collection → Returns True if value does NOT exist

print(3 not in [1, 2, 3])
# Output: False (3 IS in the list)

print(5 not in [1, 2, 3])
# Output: True (5 is NOT in the list)


# ============================================================================
# 4. MEMBERSHIP ACROSS DIFFERENT COLLECTIONS
# ============================================================================

# --- Checking in a String ---
email = "user@gmail.com"
print("@" in email)
# Output: True

# --- Checking in a List ---
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
# Output: True

# --- Checking in a Tuple ---
allowed_roles = ("admin", "editor", "viewer")
print("admin" in allowed_roles)
# Output: True

# --- Checking in a Dictionary (checks keys by default) ---
user = {"name": "Alice", "age": 25}
print("name" in user)
# Output: True (checks keys, not values)

print("Alice" in user)
# Output: False (values are not checked by default)


# ============================================================================
# 5. PRACTICAL TASK - Security: Domain Blacklist Check
# ============================================================================

# Use Case: Validate that a domain is NOT on the banned list
# Security Check: ensure the domain is not banned

domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.com"]

print(domain not in banned_domains)
# Output: True (gmail.com is safe - not in banned list)

# Test with a banned domain
domain = "spam.com"
print(domain not in banned_domains)
# Output: False (spam.com is banned - block it!)


# ============================================================================
# 6. IDENTITY OPERATOR - is
# ============================================================================

# --- is Operator ---
# x is y → Returns True if x and y point to the SAME object in memory
#
# KEY DIFFERENCE:
# == checks if VALUES are equal
# is checks if they are the EXACT SAME object in memory


# --- Example 1: Lists (mutable objects) ---
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)
# Output: True (same VALUES)

print(x is y)
# Output: False (different objects in memory)
# Two separate lists were created, even though they look identical


# --- Example 2: Small Integers (cached objects) ---
x = 10
y = 10

print(x == y)
# Output: True (same VALUE)

print(x is y)
# Output: True (same object in memory!)
# Python caches small integers (-5 to 256) for performance
# So x and y both point to the same object


# ============================================================================
# 7. == vs is - THE CRITICAL DIFFERENCE
# ============================================================================
"""
Understanding the difference:

    ==  → Value Comparison
          "Do these two values LOOK the same?"
          "apple" == "apple" → True

    is  → Identity Comparison
          "Are these two variables pointing to the SAME object?"
          x is y → Are x and y literally the same object in memory?

Visual Example:

    x = ['a', 'b', 'c']     →  [Memory Address: 0x1A]  →  ['a', 'b', 'c']
    y = ['a', 'b', 'c']     →  [Memory Address: 0x2B]  →  ['a', 'b', 'c']

    x == y  → True  (both hold ['a', 'b', 'c'])
    x is y  → False (different memory addresses!)

Best Practice:
    • Use ==  for comparing values (strings, numbers, lists)
    • Use is  ONLY for comparing with None
"""


# ============================================================================
# 8. IDENTITY OPERATOR - is not
# ============================================================================

# --- is not Operator ---
# x is not y → Returns True if x and y are DIFFERENT objects in memory

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x is not y)
# Output: True (they are different objects in memory)

# Most common use case: checking for None
value = None
print(value is not None)
# Output: False (value IS None)

value = "Hello"
print(value is not None)
# Output: True (value is NOT None)


# ============================================================================
# 9. PRACTICAL TASK - Email Validation
# ============================================================================

# Use Case: Validate that email is filled in and not empty
# Must check: email exists AND is not empty

# Case A: Empty String
emailA = ""    # "" means the value is known but empty (it's a string)
print(emailA != "")
# Output: False (emailA is empty → invalid)


# Case B: None value
emailB = None  # None means no value at all (completely missing)

# Method 1: Using !=
print(emailB != None and emailB != "")
# Output: False (emailB is None → invalid)

# Method 2: Using is not (RECOMMENDED for None checks)
print(emailB is not None and emailB != "")
# Output: False (emailB is None → invalid)

# ⭐ Best Practice: Always use 'is not None' instead of '!= None'


# ============================================================================
# 10. NONE vs EMPTY STRING - IMPORTANT DISTINCTION
# ============================================================================
"""
Critical Difference:

    None:
        • Means "no value at all" - completely missing
        • Type: NoneType
        • Use case: Variable not yet set
        • Example: emailB = None

    "" (Empty String):
        • Means the value exists but is empty
        • Type: str
        • Use case: User left a field blank
        • Example: emailA = ""

    Both are falsy, but they are NOT the same:
        bool(None)  → False
        bool("")    → False
        None == ""  → False  (different types!)
        None is ""  → False

    ✅ Use is/is not to check for None
    ✅ Use ==/!= to check for empty string
"""


# Demonstrating the difference:
emailA = ""
emailB = None

print(type(emailA))
# Output: <class 'str'>

print(type(emailB))
# Output: <class 'NoneType'>

print(emailA == emailB)
# Output: False (they are NOT equal)

print(emailA is emailB)
# Output: False (completely different objects)


# ============================================================================
# KEY CONCEPTS SUMMARY
# ============================================================================
"""
MEMBERSHIP & IDENTITY OPERATORS - ESSENTIAL FACTS

Membership Operators:
    • x in y        → True if x EXISTS in y
    • x not in y    → True if x does NOT exist in y
    • Works with: strings, lists, tuples, sets, dict (checks keys)

Identity Operators:
    • x is y        → True if SAME object in memory
    • x is not y    → True if DIFFERENT objects in memory

== vs is:
    • ==    → Compares VALUES
    • is    → Compares MEMORY ADDRESS (identity)

When to use is:
    ✅ Checking for None:   if value is None
    ✅ Checking not None:   if value is not None
    ❌ Comparing values:    use == instead

Important Notes:
    • Python caches small integers (-5 to 256) → x is y can be True
    • Two lists with same values are NOT the same object
    • None and "" are both falsy but completely different
    • Always use 'is not None' (not '!= None') for None checks
    • 'in' with dictionaries checks KEYS, not values
"""


# ============================================================================
# DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use 'in' to check if a value exists in a collection
✓ How to use 'not in' to check if a value is absent
✓ That 'in' works with strings, lists, tuples, sets, and dictionaries
✓ That 'in' checks KEYS when used with dictionaries (not values)
✓ The critical difference between == and is:
  ✓ == compares VALUES
  ✓ is compares MEMORY ADDRESSES (identity)
✓ That Python caches small integers, so 'is' can be True for numbers
✓ That two lists with same values are different objects in memory
✓ How to use 'is not' for safer None checks
✓ The difference between None and empty string "":
  ✓ None = value is missing/unknown
  ✓ "" = value exists but is empty
✓ Best practice: always use 'is None' / 'is not None' for None checks
✓ Real-world use cases: domain blacklist, email validation, security checks
"""
