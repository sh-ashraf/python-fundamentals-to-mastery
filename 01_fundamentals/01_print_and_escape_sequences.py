"""
================================================================================
PYTHON PRINT() FUNCTION - STUDY NOTES
================================================================================
Learning Focus: Understanding print() basics and escape sequences
"""


# ============================================================================
# 1. BASIC PRINT USAGE
# ============================================================================
# The simplest way to output text in Python

print("Hi, this is my first python code")


# ============================================================================
# 2. ESCAPE SEQUENCES
# ============================================================================
# Special characters that control how text is displayed

# \" - Displays double quotes inside single-quoted strings
print(' Hi " python " ')

# \' - Displays single quotes inside single-quoted strings
print(' Hi \' python \' ')

# \\ - Displays a backslash (escapes the escape character)
print(' Hi \\ python \\ ')

# \n - Creates a new line
print(' Hi \n python ')

# \t - Creates a horizontal tab space
print(' Hi \t python ')

# \b - Backspace (removes the previous character)
print(' Hi python\b ')


# ============================================================================
# 3. MULTI-LINE OUTPUT TECHNIQUES
# ============================================================================

# Method 1: Using \n escape sequences in a single string
print("Your Learning Path: \n -Python Basics \n -Data Engineering \n -AI ")


# Method 2: String concatenation across multiple lines
print("Your Learning Path: "
      "\n -Python Basics "
      "\n -Data Engineering "
      "\n -AI ")


# Method 3: Triple-quoted strings (preserves formatting)
print(""" Your Learning Path: 
\t-Python Basics  
\t-Data Engineering  
\t-AI """)


# ============================================================================
# 4. SUMMARY - print() FUNCTION
# ============================================================================
"""
print() - Built-in Python Function

PURPOSE:
    Display messages and output to the console for users

USE CASES:
    • Communicate with users
    • Show program results
    • Debug code during development
    • Test functionality and behavior

SYNTAX:
    print(value, ..., sep=' ', end='\n')
"""


# ============================================================================
# 5. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use the print() function in Python
✓ How escape sequences work: \n (newline), \t (tab), \\ (backslash), \" (double quote), \' (single quote), \b (backspace)
✓ Three different methods to print multi-line text
✓ Best practices for formatting output
"""
