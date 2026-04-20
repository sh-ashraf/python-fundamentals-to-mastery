# Chapter 1: Python Fundamentals

> Master the essential building blocks of Python programming

---

## 📚 Chapter Overview

This chapter covers the **core fundamentals** every Python programmer must know. By the end of this chapter, you'll understand how to:
- Display output to users
- Get input from users
- Store and manipulate data
- Work with Python's type system

---

## 🎯 Learning Objectives

By completing this chapter, you will be able to:

✅ Use `print()` to display formatted output  
✅ Understand and use escape sequences (`\n`, `\t`, `\\`, etc.)  
✅ Create and use variables to store data  
✅ Get user input with `input()` and convert types  
✅ Identify and work with Python's basic data types  
✅ Understand dynamic typing and type checking  

---

## 📁 Files in This Chapter

| # | File Name | Topic | Key Concepts |
|---|-----------|-------|--------------|
| 01 | `01_print_and_escape_sequences.py` | Output Basics | `print()`, escape sequences, multi-line output |
| 02 | `02_variables_and_storage.py` | Variables | Variable creation, naming conventions, reassignment |
| 03 | `03_input_and_type_conversion.py` | User Input | `input()`, `int()`, `float()`, type conversion |
| 04 | `04_data_types_overview.py` | Data Types | `int`, `float`, `str`, `bool`, `None`, `type()` |

---

## 🔑 Key Concepts Covered

### **1. Output with print()**
- Basic `print()` syntax
- Escape sequences: `\n`, `\t`, `\\`, `\"`, `\'`, `\b`
- Multi-line output methods
- String concatenation vs comma separation

### **2. Variables**
- Variable creation and assignment
- Naming conventions (snake_case)
- Variable reassignment
- Hard-coded vs dynamic values

### **3. User Input**
- `input()` function basics
- Type conversion: `int()`, `float()`, `str()`
- Handling user-provided data
- Input validation concepts

### **4. Data Types**
- Primitive types: `int`, `float`, `str`, `bool`
- Special type: `NoneType`
- Type checking with `type()`
- Dynamic typing in Python
- Collections overview: `list`, `tuple`, `set`, `dict`

---

## 💻 Code Examples

### **Quick Print Example:**
```python
print("Hello, Python!")
print("Line 1\nLine 2")  # Outputs on separate lines
```

### **Variables:**
```python
name = "Shehab"
age = 21
print(name, "is", age, "years old")
```

### **User Input:**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name} is {age} years old")
```

### **Type Checking:**
```python
x = 10
print(type(x))  # <class 'int'>

x = "Python"
print(type(x))  # <class 'str'>
```

---

## 🎯 Practical Challenges

### **Challenge 1: Personal Info Display**
Create a program that:
1. Asks for your name, age, and city
2. Displays them in a formatted message
3. Uses proper type conversion for age

### **Challenge 2: Email Generator**
Create a program that:
1. Takes a username as input
2. Combines it with a domain (`@example.com`)
3. Displays the complete email address

### **Challenge 3: Type Explorer**
Create variables of each type (`int`, `float`, `str`, `bool`, `None`) and display their types using `type()`.

---

## 📊 Chapter Summary

| Concept | Function/Keyword | Returns/Type | Example |
|---------|-----------------|--------------|---------|
| **Output** | `print()` | None | `print("Hello")` |
| **Input** | `input()` | `str` | `name = input("Name: ")` |
| **Type Check** | `type()` | type class | `type(10)` → `<class 'int'>` |
| **Convert to Int** | `int()` | `int` | `int("42")` → `42` |
| **Convert to Float** | `float()` | `float` | `float("3.14")` → `3.14` |
| **Convert to String** | `str()` | `str` | `str(42)` → `"42"` |

---

## 🧠 Common Mistakes & Tips

### **Mistakes to Avoid:**
❌ Forgetting that `input()` always returns a string  
❌ Using quotes around numbers makes them strings (`"123"` is `str`, not `int`)  
❌ Trying to do math with string numbers without converting first  
❌ Confusing `None` with empty string `""`  

### **Pro Tips:**
✅ Always convert `input()` when you need numbers  
✅ Use `type()` to verify variable types when debugging  
✅ Use meaningful variable names (`user_age` not `x`)  
✅ Test your code with different inputs  

---

## 📝 What You Learned

After completing this chapter, you should know:

- ✅ How to output data with `print()`
- ✅ How to format output using escape sequences
- ✅ How to store data in variables
- ✅ How to get user input and convert types
- ✅ The difference between Python's basic data types
- ✅ How to check types with `type()`
- ✅ How Python uses dynamic typing

---

## 🚀 Next Steps

**Ready for Chapter 2?** Move on to:
- **Chapter 2: Python Strings** - Learn string manipulation, slicing, and methods

**Want More Practice?**
- Combine multiple concepts in one program
- Create a simple calculator using `input()` and type conversion
- Build a mad-libs game using string concatenation

---

## 📚 Additional Resources

- [Python Official Docs - Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Real Python - Variables Guide](https://realpython.com/python-variables/)
- [Python Type System Guide](https://docs.python.org/3/library/stdtypes.html)

---

<div align="center">

**Chapter 1 Complete!** ✅

[← Back to Main README](../README.md) | [Next Chapter: Strings →](../02_strings/)

</div>