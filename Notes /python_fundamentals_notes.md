# Python Fundamentals — Developer Notes

> **Audience:** Beginner to intermediate learners preparing for practical development and interviews  
> **Perspective:** Practical notes from a Python application-development and debugging perspective  
> **Python baseline:** Examples target modern Python 3 (generally compatible with Python 3.10+ unless stated otherwise).

---

## Table of Contents

1. [Introduction to Python](#1-introduction-to-python)
2. [Features of Python](#2-features-of-python)
3. [Applications of Python](#3-applications-of-python)
4. [Python Versions](#4-python-versions)
5. [Python Data Types](#5-python-data-types)
6. [Python Variable Declaration](#6-python-variable-declaration)
7. [Python Type Casting](#7-python-type-casting)
8. [Python User Input](#8-python-user-input)
9. [Python Operators and Operations](#9-python-operators-and-operations)
10. [Common Errors and Debugging Tips](#10-common-errors-and-debugging-tips)
11. [Practice Exercises](#11-practice-exercises)
12. [Quick Revision](#12-quick-revision)

---

## 1. Introduction to Python

Python is a **high-level, general-purpose programming language** known for readable syntax and a broad ecosystem of libraries. It supports procedural, object-oriented, and functional programming styles.

### First Python program

```python
print("Hello, World!")
```

Output:

```text
Hello, World!
```

### How Python code runs

A typical CPython workflow is:

1. Write source code in a `.py` file.
2. The interpreter parses and compiles the source to Python bytecode.
3. The Python virtual machine executes that bytecode.

The exact implementation can vary. **CPython** is the standard and most widely used implementation; other implementations include PyPy.

### Example: a small calculation

```python
price = 250
quantity = 3
total = price * quantity

print("Total:", total)
```

Output:

```text
Total: 750
```

### Important terminology

- **Source code:** The Python instructions written by a developer.
- **Interpreter:** Software that runs Python programs.
- **Bytecode:** An intermediate instruction format used by CPython.
- **Library:** Reusable code that provides functionality.
- **Package:** A way to organize and distribute reusable Python modules.
- **Module:** Usually a Python file that can be imported.

### Where to write Python

- A local editor or IDE, such as VS Code or PyCharm.
- A terminal using `python filename.py` or, on some systems, `python3 filename.py`.
- A notebook environment for exploratory work and data analysis.

Check the installed version:

```bash
python --version
```

If that command is not recognized, try:

```bash
python3 --version
```

---

## 2. Features of Python

| Feature | What it means | Practical implication |
|---|---|---|
| Readable syntax | Code often resembles plain English | Easier to review and maintain |
| High-level language | Many low-level details are handled for you | Faster application development |
| Dynamically typed | A variable name can refer to values of different types | Flexible, but runtime mistakes are possible |
| Strongly typed | Incompatible types are not silently combined in many operations | Convert values explicitly when needed |
| Multi-paradigm | Supports procedural, object-oriented, and functional styles | Choose the style that fits the problem |
| Large standard library | Many common tasks need no third-party package | Useful built-in tools are readily available |
| Rich ecosystem | Many packages are available through tools such as `pip` | Useful for web, data, automation, and testing |
| Cross-platform | Python is available on major operating systems | Many scripts can run across platforms |
| Automatic memory management | Python manages object memory, including garbage collection | Developers usually do not manually free objects |
| Extensible and embeddable | Can work with native code and be embedded in other applications | Useful when integrating with existing systems |

### Example: dynamic typing

```python
value = 10
print(value, type(value))

value = "ten"
print(value, type(value))
```

Output:

```text
10 <class 'int'>
ten <class 'str'>
```

The name `value` is rebound to a string. Python does not permanently assign a single type to the variable name.

### Trade-offs to remember

- Python can be slower than compiled languages for some CPU-intensive workloads.
- Dynamic typing means some type errors appear only when code runs.
- Python is not automatically the best choice for every mobile, embedded, or real-time application.
- Performance can often be improved through algorithmic changes, profiling, caching, native extensions, or suitable libraries.

---

## 3. Applications of Python

### Common areas

1. **Web development:** APIs and web applications using Django, Flask, or FastAPI.
2. **Automation and scripting:** File operations, report generation, repetitive tasks, and system utilities.
3. **Data analysis:** Cleaning, transforming, and analyzing data with libraries such as pandas and NumPy.
4. **Artificial intelligence and machine learning:** Model development and experimentation using frameworks such as PyTorch and scikit-learn.
5. **Testing and quality assurance:** Unit tests, integration tests, and browser automation.
6. **DevOps and cloud tooling:** Deployment scripts, infrastructure utilities, and cloud SDKs.
7. **Cybersecurity:** Log analysis, defensive automation, and security testing in authorized environments.
8. **Scientific computing:** Numerical methods, simulations, and research workflows.
9. **Desktop utilities:** GUI applications using suitable libraries.
10. **Education:** Teaching programming concepts and problem-solving.

### Example: automate a simple report

```python
sales = [1200, 850, 1500, 950]
total_sales = sum(sales)
average_sales = total_sales / len(sales)

print("Total sales:", total_sales)
print("Average sale:", average_sales)
```

Output:

```text
Total sales: 4500
Average sale: 1125.0
```

**Developer tip:** Select a language and framework based on requirements, team skills, deployment environment, performance needs, and long-term maintenance—not popularity alone.

---

## 4. Python Versions

### Python 2 vs Python 3

Python 2 is end-of-life and should not be selected for new projects. Use a supported Python 3 release and check the official Python website for the current release and support status.

| Topic | Python 2 (legacy) | Python 3 |
|---|---|---|
| Status | End-of-life | Current language family |
| Print syntax | `print "Hello"` | `print("Hello")` |
| Division example | `5 / 2` gives `2` for integers | `5 / 2` gives `2.5` |
| Text handling | Different default string behavior | `str` represents Unicode text |
| New projects | Avoid | Recommended |

### Check the version from code

```python
import sys

print(sys.version)
print(sys.version_info)
```

To check whether the interpreter is Python 3:

```python
import sys

if sys.version_info.major == 3:
    print("Running Python 3")
```

### Choosing a Python version for a project

- Prefer a **currently supported Python 3 release**.
- Check the framework and dependency compatibility matrix before upgrading.
- Use a virtual environment for each project.
- Pin or constrain dependencies where appropriate.
- Run automated tests after upgrading Python or packages.

Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

Install a package into the active environment:

```bash
python -m pip install requests
```

Using `python -m pip` helps ensure that `pip` belongs to the interpreter you are using.

---

## 5. Python Data Types

Python is dynamically typed. Every object has a type, and `type(value)` can help inspect it.

```python
x = 42
print(type(x))  # <class 'int'>
```

### 5.1 Numeric types

| Type | Example | Notes |
|---|---|---|
| `int` | `age = 22` | Whole numbers; integers can grow beyond fixed 32-bit limits |
| `float` | `price = 99.5` | Floating-point numbers; many decimal fractions are approximate |
| `complex` | `z = 2 + 3j` | Complex numbers |

```python
count = 10
temperature = 36.6
signal = 2 + 3j

print(type(count))
print(type(temperature))
print(type(signal))
```

### 5.2 Boolean

`bool` has two values: `True` and `False`.

```python
is_active = True
has_error = False

print(is_active and not has_error)  # True
```

In Python, `bool` is a subtype of `int`, but treat booleans as logical values in application code.

### 5.3 String (`str`)

A string is an immutable sequence of Unicode characters.

```python
name = "Rahul"
message = 'Welcome to Python'

print(name[0])       # R
print(name.lower())  # rahul
print(len(name))     # 5
```

Strings are immutable, so methods generally return a new string rather than changing the original.

```python
text = "python"
text = text.upper()
print(text)  # PYTHON
```

### 5.4 Sequence types

| Type | Example | Mutable? | Typical use |
|---|---|---:|---|
| `list` | `[10, 20, 30]` | Yes | Ordered collection that can change |
| `tuple` | `(10, 20, 30)` | No | Fixed ordered collection |
| `range` | `range(5)` | No | Integer sequences, often used in loops |

```python
skills = ["Python", "SQL"]
skills.append("Git")
print(skills)  # ['Python', 'SQL', 'Git']

coordinates = (18.5, 73.8)
print(coordinates[0])  # 18.5

print(list(range(1, 5)))  # [1, 2, 3, 4]
```

### 5.5 Mapping type: `dict`

A dictionary stores key-value pairs. Keys must be hashable; values can be of many types.

```python
student = {
    "name": "Rahul",
    "marks": 85,
    "passed": True
}

print(student["name"])       # Rahul
print(student.get("course")) # None
```

Use `dict.get()` when a key may be missing and you want to avoid a `KeyError`.

### 5.6 Set types

- `set`: mutable collection of unique hashable elements.
- `frozenset`: immutable set.

```python
numbers = {1, 2, 2, 3}
print(numbers)  # {1, 2, 3} (display order is not a contract)

numbers.add(4)
print(3 in numbers)  # True

fixed = frozenset({1, 2, 3})
```

Sets are useful for membership checks and removing duplicates when order is not the primary requirement.

### 5.7 Binary types

- `bytes`: immutable sequence of byte values.
- `bytearray`: mutable sequence of byte values.
- `memoryview`: view of binary data without necessarily copying it.

```python
data = b"ABC"
print(data[0])  # 65

mutable_data = bytearray(b"ABC")
mutable_data[0] = 90
print(mutable_data)  # bytearray(b'ZBC')
```

### 5.8 `NoneType`

`None` represents the absence of a value.

```python
result = None

if result is None:
    print("No result available")
```

Use `is None` rather than `== None` by convention.

### 5.9 Mutable vs immutable

**Mutable objects** can be changed after creation: `list`, `dict`, `set`, and `bytearray`.

**Immutable objects** cannot be changed in place: `int`, `float`, `bool`, `str`, `tuple`, `bytes`, and `frozenset`.

Important nuance: a tuple is immutable, but it can contain a mutable object.

```python
items = ([1, 2], "hello")
items[0].append(3)

print(items)  # ([1, 2, 3], 'hello')
```

The tuple's references cannot be reassigned, but the list it references can still be mutated.

### 5.10 Check a type safely

```python
value = 100

if isinstance(value, int):
    print("Integer value")
```

`isinstance()` is often preferable to comparing `type(value)` directly because it also recognizes subclasses.

---

## 6. Python Variable Declaration

Python does not require a separate declaration statement or a type annotation before assigning a variable. Assignment binds a name to an object.

```python
name = "Rahul"
age = 22
height = 1.72
is_learning = True
```

### Naming rules

- Names may contain letters, digits, and underscores.
- A name cannot begin with a digit.
- Names are case-sensitive: `age`, `Age`, and `AGE` are different.
- Python keywords such as `if`, `class`, and `for` cannot be used as variable names.
- Prefer descriptive `snake_case` names for variables and functions.

Valid:

```python
student_name = "Asha"
marks_1 = 90
_total = 100
```

Invalid:

```python
# 1marks = 90       # Starts with a digit
# student-name = "" # Hyphen is not allowed in a name
# class = "A"       # Reserved keyword
```

### Multiple assignment

```python
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

x = y = 0
print(x, y)  # 0 0
```

Be careful with chained assignment and mutable objects:

```python
a = b = []
a.append(1)

print(a)  # [1]
print(b)  # [1] — both names refer to the same list
```

To create separate lists:

```python
a = []
b = []
```

### Reassignment and dynamic typing

```python
value = 25
value = "twenty-five"
```

This is valid Python. Type annotations can document expected types and help static-analysis tools, but they are not automatically enforced at runtime.

```python
age: int = 22
name: str = "Rahul"
```

### Constants by convention

Python does not enforce constants with a special declaration keyword. Uppercase names communicate that a value should not be reassigned.

```python
MAX_RETRIES = 3
API_TIMEOUT_SECONDS = 10
```

### Scope basics

- **Local:** Defined inside a function.
- **Enclosing:** In an outer function that contains another function.
- **Global:** Defined at module level.
- **Built-in:** Names provided by Python, such as `len`.

Python resolves names using the LEGB rule: Local, Enclosing, Global, Built-in.

```python
message = "global"

def show_message():
    message = "local"
    print(message)

show_message()  # local
print(message)  # global
```

Avoid unnecessary global state; passing values through function parameters often makes code easier to test.

---

## 7. Python Type Casting

Type casting means converting a value from one type to another. Python provides constructors such as `int()`, `float()`, `str()`, `bool()`, `list()`, `tuple()`, and `set()`.

### 7.1 Explicit conversions

```python
number_text = "42"
number = int(number_text)

price = float("19.95")
message = str(100)

print(number, type(number))  # 42 <class 'int'>
print(price, type(price))   # 19.95 <class 'float'>
print(message, type(message))  # 100 <class 'str'>
```

### 7.2 Numeric conversions

```python
print(int(9.8))    # 9 — truncates toward zero
print(float(7))    # 7.0
print(complex(2))  # (2+0j)
```

`int(9.8)` does **not** round to the nearest integer. For rounding, use `round()` where appropriate.

```python
print(round(9.8))  # 10
```

### 7.3 String conversions

```python
print(int("123"))       # 123
print(float("12.5"))    # 12.5
print(str(123))         # '123'
```

Invalid numeric text raises an exception:

```python
# int("hello")  # ValueError
```

Handle expected bad input explicitly:

```python
text = "12x"

try:
    number = int(text)
except ValueError:
    print("Please provide a valid whole number")
```

### 7.4 Collection conversions

```python
print(list("cat"))             # ['c', 'a', 't']
print(tuple([1, 2, 3]))        # (1, 2, 3)
print(set([1, 2, 2, 3]))        # {1, 2, 3}
print(list(range(3)))          # [0, 1, 2]
```

A `set` removes duplicates but does not guarantee the original order.

### 7.5 Boolean conversion

`bool()` uses truth-value rules:

```python
print(bool(0))       # False
print(bool(1))       # True
print(bool(""))      # False
print(bool("False")) # True
print(bool([]))      # False
print(bool([0]))     # True
```

**Common pitfall:** `bool("False")` is `True` because every non-empty string is truthy. Parse user-entered boolean text by comparing it to expected values instead of calling `bool()` directly.

### 7.6 Implicit conversion

Some operations convert compatible numeric values automatically:

```python
result = 5 + 2.5
print(result)        # 7.5
print(type(result))  # <class 'float'>
```

Python does not generally convert a numeric string to a number during arithmetic:

```python
# "5" + 2  # TypeError
print(int("5") + 2)  # 7
```

---

## 8. Python User Input

The built-in `input()` function reads a line from standard input and **always returns a string**.

### 8.1 Read text

```python
name = input("Enter your name: ")
print("Hello,", name)
```

Example interaction:

```text
Enter your name: Rahul
Hello, Rahul
```

### 8.2 Read an integer

```python
age_text = input("Enter your age: ")
age = int(age_text)

print("Next year you will be", age + 1)
```

If the user enters non-numeric text, `int()` raises `ValueError`. Validate input in production code.

### 8.3 Read a decimal

```python
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity
print(f"Total: {total:.2f}")
```

### 8.4 Validate input

```python
while True:
    text = input("Enter a whole number: ")

    try:
        number = int(text)
        break
    except ValueError:
        print("Invalid input. Try again.")

print("You entered:", number)
```

### 8.5 Read multiple values

```python
a, b = map(int, input("Enter two integers separated by a space: ").split())
print("Sum:", a + b)
```

Example input:

```text
10 20
```

Output:

```text
Sum: 30
```

This compact pattern is useful in coding challenges. It raises an error if the user provides the wrong number of values or non-integer text. For robust applications, validate the number and format of tokens.

### 8.6 Use f-strings for output

```python
name = "Rahul"
score = 87.456

print(f"{name} scored {score:.2f} marks.")
```

Output:

```text
Rahul scored 87.46 marks.
```

### Input-handling checklist

- Remember that `input()` returns `str`.
- Convert only after deciding what format is valid.
- Catch `ValueError` for expected conversion failures.
- Check ranges where appropriate (for example, quantity must be positive).
- Avoid assuming user input is trustworthy.
- For money, consider `decimal.Decimal` rather than binary floating-point arithmetic when exact decimal behavior is required.

---

## 9. Python Operators and Operations

Operators perform calculations, comparisons, assignments, and logical decisions.

### 9.1 Arithmetic operators

Assume `a = 10` and `b = 3`.

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | True division | `a / b` | `3.333...` |
| `//` | Floor division | `a // b` | `3` |
| `%` | Remainder | `a % b` | `1` |
| `**` | Exponentiation | `a ** b` | `1000` |

Important: floor division rounds down toward negative infinity.

```python
print(7 // 2)    # 3
print(-7 // 2)   # -4
print(7 % 2)     # 1
print(-7 % 2)    # 1
```

The remainder follows the divisor's sign. For ordinary positive integer divisibility checks, `number % 2 == 0` identifies even numbers.

### 9.2 Comparison operators

Comparison expressions return a boolean.

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

```python
age = 22

print(age >= 18)  # True
print(age == 18)  # False
print(age != 18)  # True
```

Do not confuse assignment (`=`) with equality comparison (`==`).

### 9.3 Assignment operators

```python
count = 10
count += 2   # count = count + 2
count -= 1   # count = count - 1
count *= 3   # count = count * 3
count //= 2  # count = count // 2
count %= 4   # count = count % 4

print(count)
```

Other augmented assignment operators include `/=`, `**=`, `&=`, `|=`, `^=`, `<<=`, and `>>=`.

### 9.4 Logical operators

Python uses `and`, `or`, and `not`.

```python
age = 22
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False
```

`and` and `or` short-circuit: they may return one of their operands rather than a literal boolean.

```python
name = ""
display_name = name or "Guest"
print(display_name)  # Guest
```

### 9.5 Membership operators

`in` and `not in` test membership.

```python
skills = ["Python", "Java", "SQL"]

print("Python" in skills)      # True
print("C++" not in skills)     # True
print("py" in "python")        # False — case-sensitive
```

For dictionaries, membership tests keys by default:

```python
student = {"name": "Rahul", "marks": 85}

print("name" in student)  # True
print("Rahul" in student)  # False
```

### 9.6 Identity operators

`is` and `is not` test whether two references point to the same object. They do **not** mean value equality.

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True — equal values
print(a is b)  # False — distinct list objects
print(a is c)  # True — same object
```

Use `is None` for `None` checks. For most other value comparisons, use `==`.

### 9.7 Bitwise operators

Bitwise operators work on integer bits.

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise NOT |
| `<<` | Left shift |
| `>>` | Right shift |

```python
a = 6  # binary 110
b = 3  # binary 011

print(a & b)   # 2  (010)
print(a | b)   # 7  (111)
print(a ^ b)   # 5  (101)
print(a << 1)  # 12
print(a >> 1)  # 3
```

Bitwise operations are useful in flags, low-level protocols, and certain algorithms. They are different from logical `and` and `or`.

### 9.8 Operator precedence

Precedence determines how an expression is grouped. Use parentheses when they make intent clearer.

```python
result = 2 + 3 * 4
print(result)  # 14

result = (2 + 3) * 4
print(result)  # 20
```

A few useful reminders:

- Parentheses group expressions.
- Exponentiation (`**`) binds more tightly than multiplication and division.
- Multiplication, division, floor division, and remainder bind more tightly than addition and subtraction.
- Comparisons bind less tightly than arithmetic.
- `not` binds more tightly than `and`, and `and` more tightly than `or`.

Avoid relying on obscure precedence rules in complex expressions; add parentheses.

### 9.9 Common operator use cases

**Even or odd**

```python
number = 17
print("Even" if number % 2 == 0 else "Odd")
```

**Maximum of two values**

```python
a, b = 10, 25
print(a if a > b else b)
```

**Range validation**

```python
score = 78
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Invalid score")
```

**Swap two variables**

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

---

## 10. Common Errors and Debugging Tips

| Error | Typical cause | What to check |
|---|---|---|
| `SyntaxError` | Invalid Python syntax | Colons, quotes, parentheses, indentation |
| `NameError` | Name used before it is defined or misspelled | Spelling and scope |
| `TypeError` | Operation or function used with an incompatible type | Types of operands and arguments |
| `ValueError` | Correct type requested but invalid value supplied | Input format and conversion |
| `ZeroDivisionError` | Division by zero | Denominator and input validation |
| `IndexError` | Sequence index outside valid bounds | Length and index calculations |
| `KeyError` | Missing dictionary key accessed with `dict[key]` | Key existence or use `get()` |
| `IndentationError` | Inconsistent or missing indentation | Consistent spaces; usually four spaces per level |

### Debugging workflow

1. Read the complete traceback, especially the last line and the line where the error occurred.
2. Reproduce the problem with the smallest input possible.
3. Inspect types and values with `print()` or a debugger.
4. Check boundary cases: empty input, zero, negative numbers, and unexpected text.
5. Fix the root cause rather than hiding the exception.
6. Add a test that would catch the same bug in the future.

Example:

```python
text = "abc"

try:
    value = int(text)
except ValueError as error:
    print(f"Could not convert input: {error}")
```

Catch specific exceptions where possible. Avoid a bare `except:` unless there is a compelling reason, because it can hide unexpected failures.

---

## 11. Practice Exercises

Try solving these without checking the solutions first.

### Beginner

1. Print your name, city, and favorite programming language.
2. Store two integers in variables and print their sum, difference, product, and quotient.
3. Ask for a user's name and greet them.
4. Read a number and print its type before and after converting it to `float`.
5. Read an integer and determine whether it is even or odd.
6. Convert `"123"` to an integer. What happens when you convert `"12a"`?
7. Create a list of five skills, append one skill, and print the list.
8. Given `a = [1, 2]` and `b = a`, change `a` and observe `b`. Explain why.

### Intermediate

9. Read two space-separated integers and print the larger number.
10. Read a score and validate that it lies between 0 and 100.
11. Given a list with duplicate values, create a set and explain what information may be lost.
12. Demonstrate the difference between `==` and `is` using two separate lists with equal contents.
13. Write a loop that keeps asking for an integer until conversion succeeds.
14. Predict the result of `-7 // 2` and `-7 % 2`, then verify in Python.
15. Write a program that calculates the total cost from a price and quantity, validating that quantity is non-negative.

### Challenge

16. Build a small command-line calculator for `+`, `-`, `*`, and `/`. Handle invalid operators and division by zero.
17. Read a comma-separated list of integers, validate each item, and calculate the minimum, maximum, and average.
18. Explain when a list is preferable to a tuple, and when a set is preferable to a list.
19. Describe how you would debug a `TypeError` in a function receiving user input.
20. Write a function with type hints and a docstring that converts a numeric string to an integer, reporting invalid input clearly.

---

## 12. Quick Revision

- Python is a high-level, general-purpose language with a broad ecosystem.
- Use a supported Python 3 release for new projects.
- `input()` returns a string; convert and validate it when needed.
- `int(9.8)` truncates toward zero; it does not round.
- `bool("False")` is `True` because the string is non-empty.
- Lists, dictionaries, and sets are mutable; strings and tuples are immutable (although a tuple may contain mutable objects).
- `==` compares values; `is` compares object identity.
- `in` checks membership; for dictionaries it checks keys by default.
- `/` performs true division; `//` performs floor division.
- Use `try`/`except` for expected conversion failures, and catch specific exceptions.
- Use descriptive names, small functions, tests, and a virtual environment to improve maintainability.

### Official references

- Python documentation: https://docs.python.org/3/
- Python tutorial: https://docs.python.org/3/tutorial/
- Built-in functions: https://docs.python.org/3/library/functions.html
- Built-in types: https://docs.python.org/3/library/stdtypes.html
- Python downloads and release information: https://www.python.org/downloads/

---

**End of notes.** Use the examples as runnable snippets, then complete the exercises to reinforce each concept.
