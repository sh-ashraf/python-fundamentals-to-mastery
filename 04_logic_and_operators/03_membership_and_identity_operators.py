"""
================================================================================
PYTHON LOGIC & OPERATORS - PART 3: Membership & Identity Operators
================================================================================
Learning Focus: 
"""

"""
┌──────────────────────┬───────────────────────┬────────────────────────────────────┐
│ Membership           │ in                    │ Value exists in collection         │
│ Operators            │ not in                │ Value does not exist               │
├──────────────────────┼───────────────────────┼────────────────────────────────────┤
│ Identity Operators   │ is                    │ Same object in memory              │
│                      │ is not                │ Different objects                  │
└──────────────────────┴───────────────────────┴────────────────────────────────────┘
"""

# Membership (in) Operator
# Checks if a value inside another value like a string, list, tuple, or other sequence

print("o" in "python")
print(3 not in [1,2,3])

# ==> Task
# Validate that the domain is not on the banned list 
# Security Check: ensure the domain is not banned 
domain = "gmail.com"
banned_domain = ["spam.com", "fake.org", "bot.com"]
print(domain not in banned_domain)

# Identity (is) Operator
# Checks if two variables refer the same object in memory

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']



























