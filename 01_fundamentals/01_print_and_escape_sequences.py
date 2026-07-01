"""
================================================================================
PYTHON FUNDAMENTALS - PRINT() FUNCTION
================================================================================
Learning Focus: Understanding print() basics and escape sequences
"""


# ============================================================================
# 1. BASIC PRINT USAGE
# ============================================================================
# The simplest way to output text in Python

print("Hi, this is my first python code")
# Output: Hi, this is my first python code


# ============================================================================
# 2. ESCAPE SEQUENCES
# ============================================================================
# Special characters that control how text is displayed

# \" - Displays double quotes inside single-quoted strings
print(' Hi " python " ')
# Output:  Hi " python " 

# \' - Displays single quotes inside single-quoted strings
print(' Hi \' python \' ')
# Output:  Hi ' python ' 

# \\ - Displays a backslash (escapes the escape character)
print(' Hi \\ python \\ ')
# Output:  Hi \ python \ 

# \n - Creates a new line
print(' Hi \n python ')
# Output:  Hi 
#          python 

# \t - Creates a horizontal tab space
print(' Hi \t python ')
# Output:  Hi 	 python 

# \b - Backspace (removes the previous character)
print(' Hi python\b ')
# Output:  Hi pytho 


# ============================================================================
# 3. MULTI-LINE OUTPUT TECHNIQUES
# ============================================================================

# Method 1: Using \n escape sequences in a single string
print("Your Learning Path: \n -Python Basics \n -Data Engineering \n -AI ")
# Output: Your Learning Path: 
#          -Python Basics 
#          -Data Engineering 
#          -AI 


# Method 2: String concatenation across multiple lines
print("Your Learning Path: "
      "\n -Python Basics "
      "\n -Data Engineering "
      "\n -AI ")
# Output: Your Learning Path: 
#          -Python Basics 
#          -Data Engineering 
#          -AI 


# Method 3: Triple-quoted strings (preserves formatting)
print(""" Your Learning Path: 
\t-Python Basics  
\t-Data Engineering  
\t-AI """)
# Output:  Your Learning Path: 
# 	-Python Basics  
# 	-Data Engineering  
# 	-AI 


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
    
PARAMETERS:
    • value(s) - What to print (can be multiple, separated by commas)
    • sep - Separator between values (default: space)
    • end - What to print at the end (default: newline)

EXAMPLES:
    print("Hello")                    → Hello
    print("A", "B", "C")              → A B C
    print("A", "B", sep="-")          → A-B
    print("Hello", end="!")           → Hello!
"""


# ============================================================================
# 5. DAILY LEARNING RECORD
# ============================================================================
"""
What I learned today:
✓ How to use the print() function in Python
✓ How escape sequences work: \n (newline), \t (tab), \\ (backslash), 
  \" (double quote), \' (single quote), \b (backspace)
✓ Three different methods to print multi-line text
✓ Best practices for formatting output
✓ The difference between escape sequences and regular characters
✓ How \b removes the previous character
"""