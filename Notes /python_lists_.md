# Python Lists and Core Operations — Developer Notes

> **Audience:** Beginner to intermediate Python learners, interview candidates, and application developers  
> **Perspective:** Practical guidance from a Python application-development and debugging perspective  
> **Python baseline:** Modern Python 3 (examples generally work with Python 3.10+).

---

## Table of Contents

1. [Introduction to Python](#1-introduction-to-python)
2. [Python Lists](#2-python-lists)
3. [Python List Methods with Examples](#3-python-list-methods-with-examples)
4. [Real-World Python List Applications](#4-real-world-python-list-applications)
5. [Python Operators and Operations](#5-python-operators-and-operations)
6. [Common List Bugs and Debugging](#6-common-list-bugs-and-debugging)
7. [Performance and Best Practices](#7-performance-and-best-practices)
8. [Practice Exercises](#8-practice-exercises)
9. [Quick Revision](#9-quick-revision)

---

## 1. Introduction to Python

Python is a high-level, general-purpose programming language with readable syntax and a large standard library. It supports procedural, object-oriented, and functional programming styles.

### First program

```python
print("Hello, Python!")
```

Output:

```text
Hello, Python!
```

### How Python runs code

With CPython, source code is parsed and compiled into Python bytecode, which the Python virtual machine executes. Other Python implementations may work differently.

Check your installed version:

```bash
python --version
```

On some systems, use `python3 --version`.

### Why Python is useful in application development

- Readable syntax helps teams maintain code.
- The standard library supports common tasks such as JSON handling, dates, files, and testing.
- Packages support web development, data processing, automation, and machine learning.
- Frameworks such as Django, Flask, and FastAPI are commonly used to build web applications and APIs.

### Example: simple backend-style data processing

```python
orders = [
    {"id": 101, "total": 250.0},
    {"id": 102, "total": 499.0},
    {"id": 103, "total": 150.0},
]

total_revenue = sum(order["total"] for order in orders)
print(f"Revenue: ₹{total_revenue:.2f}")
```

Output:

```text
Revenue: ₹899.00
```

**Developer note:** Python is productive, but production systems still need input validation, tests, logging, secure configuration, observability, and careful performance measurement.

---

## 2. Python Lists

A **list** is an ordered, mutable collection. It can contain duplicate values and elements of different types.

```python
numbers = [10, 20, 30]
mixed = ["Rahul", 22, True, 7.5]
empty = []

print(numbers)
print(type(numbers))  # <class 'list'>
```

### 2.1 Create lists

```python
skills = ["Python", "SQL", "Git"]
scores = [85, 92, 78]
from_range = list(range(1, 6))

print(skills)
print(scores)
print(from_range)  # [1, 2, 3, 4, 5]
```

A list can be created with square brackets or with `list(iterable)`.

### 2.2 Indexing

Python list indexes start at `0`.

```python
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[-1])  # mango
print(fruits[-2])  # banana
```

Invalid indexes raise `IndexError`.

```python
# print(fruits[5])  # IndexError
```

### 2.3 Slicing

Syntax: `list[start:stop:step]`. The `stop` index is excluded.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[3:])    # [40, 50, 60]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10]
```

Slicing beyond the list's boundaries usually does not raise `IndexError`; it returns the available portion.

### 2.4 Lists are mutable

```python
prices = [100, 200, 300]
prices[1] = 250
print(prices)  # [100, 250, 300]
```

Unlike strings and tuples, list elements can be changed after the list is created.

### 2.5 Lists allow duplicates

```python
ids = [101, 102, 101, 103, 102]
print(ids)
```

Duplicates are valid. Whether to remove them depends on the business requirement.

### 2.6 Lists can contain nested lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

print(matrix[0][1])  # 2
```

Nested lists can represent grids, tables, or matrix data.

### 2.7 Iterate through a list

```python
tasks = ["Design", "Build", "Test"]

for task in tasks:
    print(task)
```

When the index is needed, use `enumerate()`:

```python
for index, task in enumerate(tasks, start=1):
    print(index, task)
```

Output:

```text
1 Design
2 Build
3 Test
```

### 2.8 List comprehension

A list comprehension builds a new list from an iterable.

```python
numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in numbers]
evens = [number for number in numbers if number % 2 == 0]

print(squares)  # [1, 4, 9, 16, 25, 36]
print(evens)    # [2, 4, 6]
```

Use comprehensions for simple transformations and filters. Prefer a regular loop if the expression becomes difficult to read.

### 2.9 Copying a list

Assignment does not copy the list; it creates another reference to the same object.

```python
original = [1, 2, 3]
alias = original
alias.append(4)

print(original)  # [1, 2, 3, 4]
```

Make a shallow copy using `copy()` or slicing:

```python
original = [1, 2, 3]
copied = original.copy()
copied.append(4)

print(original)  # [1, 2, 3]
print(copied)    # [1, 2, 3, 4]
```

A **shallow copy** does not recursively copy nested objects. For nested mutable data, changes to shared inner objects may still be visible through both lists.

### 2.10 Check membership and length

```python
languages = ["Python", "Java", "TypeScript"]

print("Python" in languages)  # True
print("C++" not in languages)  # True
print(len(languages))  # 3
```

List membership (`value in my_list`) normally scans items from left to right, so its time complexity is O(n). A set is often better for repeated membership checks when uniqueness and ordering are not the primary concern.

---

## 3. Python List Methods with Examples

List methods usually modify the list in place unless otherwise noted. A common mistake is expecting a mutating method to return the updated list.

### 3.1 `append(value)`

Adds one item to the end.

```python
items = ["pen", "book"]
result = items.append("pencil")

print(items)   # ['pen', 'book', 'pencil']
print(result)  # None
```

**Complexity:** Amortized O(1).

### 3.2 `extend(iterable)`

Adds each item from an iterable.

```python
items = [1, 2]
items.extend([3, 4])

print(items)  # [1, 2, 3, 4]
```

Compare with `append()`:

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]
```

### 3.3 `insert(index, value)`

Inserts an item at a specified position.

```python
numbers = [10, 30, 40]
numbers.insert(1, 20)

print(numbers)  # [10, 20, 30, 40]
```

**Complexity:** O(n) in general because later elements may need to shift.

### 3.4 `remove(value)`

Removes the first matching value. Raises `ValueError` if no matching value exists.

```python
numbers = [10, 20, 20, 30]
numbers.remove(20)

print(numbers)  # [10, 20, 30]
```

Safe handling when the value may be missing:

```python
target = 50
if target in numbers:
    numbers.remove(target)
```

This performs two scans in the worst case. If performance matters, consider whether the lookup and removal can be redesigned.

### 3.5 `pop([index])`

Removes and returns the item at the specified index. Without an index, it removes the last item. An empty list or invalid index raises `IndexError`.

```python
tasks = ["build", "test", "deploy"]

last_task = tasks.pop()
first_task = tasks.pop(0)

print(last_task)   # deploy
print(first_task)  # build
print(tasks)       # ['test']
```

**Complexity:** Popping from the end is O(1); popping from the front is O(n) due to shifting.

### 3.6 `clear()`

Removes all items from the list.

```python
cache_keys = ["a", "b", "c"]
cache_keys.clear()

print(cache_keys)  # []
```

### 3.7 `index(value[, start[, end]])`

Returns the index of the first matching value. Raises `ValueError` if not found.

```python
names = ["Asha", "Rahul", "Asha"]

print(names.index("Rahul"))  # 1
print(names.index("Asha"))   # 0
```

To check for existence without an exception:

```python
target = "Meera"

if target in names:
    print(names.index(target))
else:
    print("Not found")
```

### 3.8 `count(value)`

Counts occurrences of a value.

```python
votes = ["yes", "no", "yes", "yes"]

print(votes.count("yes"))  # 3
print(votes.count("no"))   # 1
```

**Complexity:** O(n).

### 3.9 `sort(key=None, reverse=False)`

Sorts the existing list in place and returns `None`.

```python
numbers = [40, 10, 30, 20]
result = numbers.sort()

print(numbers)  # [10, 20, 30, 40]
print(result)   # None
```

Descending order:

```python
numbers.sort(reverse=True)
print(numbers)  # [40, 30, 20, 10]
```

Sort strings by length:

```python
words = ["python", "API", "backend", "SQL"]
words.sort(key=len)

print(words)  # ['API', 'SQL', 'python', 'backend']
```

Sort records by a field:

```python
users = [
    {"name": "Asha", "age": 27},
    {"name": "Rahul", "age": 22},
    {"name": "Meera", "age": 25},
]

users.sort(key=lambda user: user["age"])
print(users)
```

For sorting without modifying the original iterable, use `sorted()`:

```python
original = [3, 1, 2]
ordered = sorted(original)

print(original)  # [3, 1, 2]
print(ordered)   # [1, 2, 3]
```

### 3.10 `reverse()`

Reverses the list in place; returns `None`.

```python
letters = ["a", "b", "c"]
letters.reverse()

print(letters)  # ['c', 'b', 'a']
```

For a reversed copy, use `letters[::-1]` or `list(reversed(letters))`.

### 3.11 `copy()`

Creates a shallow copy.

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]
```

### 3.12 Quick method reference

| Method | Purpose | Mutates list? | Typical complexity |
|---|---|---:|---:|
| `append(x)` | Add one item at end | Yes | Amortized O(1) |
| `extend(iterable)` | Add multiple items | Yes | O(k), where k is added items |
| `insert(i, x)` | Insert at index | Yes | O(n) |
| `remove(x)` | Remove first matching value | Yes | O(n) |
| `pop()` | Remove and return item | Yes | O(1) from end |
| `pop(0)` | Remove and return first item | Yes | O(n) |
| `clear()` | Remove all items | Yes | O(n) |
| `index(x)` | Find first matching index | No | O(n) |
| `count(x)` | Count matching items | No | O(n) |
| `sort()` | Sort in place | Yes | O(n log n) typical |
| `reverse()` | Reverse in place | Yes | O(n) |
| `copy()` | Shallow copy | No change to original | O(n) |

Complexity is a useful guide, not a guarantee about exact runtime. It can depend on the operation, implementation, and input.

---

## 4. Real-World Python List Applications

Lists are useful when an application needs an ordered collection of items. In backend applications, lists commonly appear in request payloads, query results, batch processing, validation errors, and API responses.

### 4.1 Backend API response

A web endpoint may return a JSON array of records. In Python, that data is often represented as a list of dictionaries.

```python
products = [
    {"id": 1, "name": "Keyboard", "price": 1499},
    {"id": 2, "name": "Mouse", "price": 799},
]

response = {
    "count": len(products),
    "results": products,
}

print(response)
```

Frameworks such as FastAPI and Django REST Framework can serialize suitable Python data structures to JSON. In production, use response schemas/serializers and validate values rather than returning arbitrary objects.

### 4.2 Filtering records

Example: filter available products under a budget.

```python
products = [
    {"name": "Keyboard", "price": 1499, "in_stock": True},
    {"name": "Mouse", "price": 799, "in_stock": True},
    {"name": "Monitor", "price": 9999, "in_stock": False},
]

budget = 2000

available = [
    product for product in products
    if product["in_stock"] and product["price"] <= budget
]

print([product["name"] for product in available])
# ['Keyboard', 'Mouse']
```

**Backend use case:** Filtering a small, already-loaded collection. For large datasets, apply filters in the database when possible to avoid loading unnecessary rows into application memory.

### 4.3 Batch processing jobs

```python
pending_jobs = ["email-101", "email-102", "email-103"]

for job_id in pending_jobs:
    print(f"Processing {job_id}")
```

**Backend use case:** Processing a batch of IDs, files, or tasks.

For production job queues, do not treat a plain in-memory list as a durable queue. If a process restarts, in-memory items may be lost. Use a durable queue or broker when persistence, retries, concurrency, or delivery guarantees matter.

### 4.4 Collect validation errors

```python
errors = []

email = "not-an-email"
age = -2

if "@" not in email:
    errors.append("Email format is invalid")

if age < 0:
    errors.append("Age cannot be negative")

if errors:
    print({"valid": False, "errors": errors})
```

Possible output:

```text
{'valid': False, 'errors': ['Email format is invalid', 'Age cannot be negative']}
```

**Backend use case:** Return multiple validation errors in one response instead of failing at the first invalid field. Use a proper email validation strategy for real systems; checking for `@` is only a teaching example.

### 4.5 Pagination

For a small in-memory list:

```python
users = [f"user-{i}" for i in range(1, 26)]

page = 2
page_size = 5
start = (page - 1) * page_size
end = start + page_size

page_users = users[start:end]
print(page_users)
# ['user-6', 'user-7', 'user-8', 'user-9', 'user-10']
```

**Backend use case:** Demonstrates offset-based slicing. For large database tables, paginate in the database. Cursor/keyset pagination can perform better and behave more predictably as data changes.

### 4.6 Remove duplicates while preserving order

```python
tags = ["python", "api", "python", "backend", "api"]

unique_tags = list(dict.fromkeys(tags))
print(unique_tags)
# ['python', 'api', 'backend']
```

This works because dictionaries preserve insertion order in modern Python. If order does not matter, a set may be sufficient.

### 4.7 Aggregate metrics

```python
response_times_ms = [120, 98, 150, 110, 105]

average = sum(response_times_ms) / len(response_times_ms)
minimum = min(response_times_ms)
maximum = max(response_times_ms)

print(f"Average: {average:.1f} ms")
print(f"Min: {minimum} ms")
print(f"Max: {maximum} ms")
```

Check for an empty list before dividing or calling `min()`/`max()`:

```python
if response_times_ms:
    average = sum(response_times_ms) / len(response_times_ms)
else:
    average = 0
```

For real monitoring systems, use a metrics or telemetry system rather than keeping unbounded histories in application memory.

### 4.8 Simple in-memory cache

```python
recent_items = []

def remember(item, limit=3):
    recent_items.append(item)

    if len(recent_items) > limit:
        recent_items.pop(0)

remember("page-A")
remember("page-B")
remember("page-C")
remember("page-D")

print(recent_items)  # ['page-B', 'page-C', 'page-D']
```

This is a teaching example, not a scalable cache. Removing from the front of a list is O(n). For queue-like behavior, use `collections.deque`; for a real shared production cache, consider a dedicated cache such as Redis when appropriate.

### 4.9 Database query results

A database library may return rows that are iterated over or converted to a list:

```python
# Illustrative pseudocode: exact API depends on the database driver.
rows = [
    {"id": 1, "status": "paid"},
    {"id": 2, "status": "pending"},
]

paid_orders = [row for row in rows if row["status"] == "paid"]
```

**Production consideration:** Avoid materializing millions of rows into a list. Prefer database filtering, pagination, iterators, or streaming results where supported.

### 4.10 API request payload validation

An API may accept a list of item IDs:

```python
requested_ids = [101, 102, 103]

if not requested_ids:
    print("At least one ID is required")
elif any(not isinstance(item_id, int) for item_id in requested_ids):
    print("All IDs must be integers")
else:
    print("IDs accepted")
```

This illustrates basic validation only. Real APIs should also consider booleans (`bool` is a subclass of `int` in Python), duplicate IDs, allowed ranges, authorization, request-size limits, and schema validation.

### Lists are not always the right data structure

| Requirement | Consider |
|---|---|
| Ordered collection with duplicates | `list` |
| Fast membership checks and uniqueness | `set` |
| Key-to-value lookup | `dict` |
| FIFO queue with efficient operations at both ends | `collections.deque` |
| Immutable ordered collection | `tuple` |
| Large data filtering/aggregation | Database query or specialized data tools |
| Durable asynchronous jobs | A proper message broker or job queue |

---

## 5. Python Operators and Operations

Operators perform arithmetic, comparisons, logical tests, assignments, membership checks, identity checks, and bitwise operations.

### 5.1 Arithmetic operators

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

Floor division rounds down toward negative infinity:

```python
print(7 // 2)   # 3
print(-7 // 2)  # -4
print(7 % 2)    # 1
print(-7 % 2)   # 1
```

### 5.2 Comparison operators

`==`, `!=`, `>`, `<`, `>=`, and `<=` return booleans.

```python
price = 500

print(price < 1000)   # True
print(price == 500)   # True
print(price != 500)   # False
```

Lists can be compared by value:

```python
print([1, 2] == [1, 2])  # True
print([1, 2] == [2, 1])  # False — order matters
```

### 5.3 Assignment operators

```python
count = 10
count += 2
count -= 1
count *= 2
count //= 3

print(count)
```

Augmented assignment updates the target according to the operator. With mutable objects, operations such as `+=` may modify an object in place.

```python
items = [1, 2]
items += [3, 4]
print(items)  # [1, 2, 3, 4]
```

### 5.4 Logical operators

```python
age = 22
has_account = True

print(age >= 18 and has_account)  # True
print(age < 18 or has_account)    # True
print(not has_account)            # False
```

`and` and `or` short-circuit and can return one of their operands, not necessarily `True` or `False`.

### 5.5 Membership operators

`in` and `not in` test whether an item belongs to a collection.

```python
skills = ["Python", "SQL", "Git"]

print("Python" in skills)  # True
print("Java" not in skills)  # True
```

List membership is generally O(n). For many repeated lookups, a set may be more appropriate:

```python
skill_set = set(skills)
print("Python" in skill_set)  # True
```

### 5.6 Identity operators

`is` and `is not` compare object identity.

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)  # True: equal contents
print(a is b)  # False: separate objects
print(a is c)  # True: same object
```

Use `is None` for checking `None`; use `==` for value equality.

### 5.7 Bitwise operators

Bitwise operators operate on integer bits: `&`, `|`, `^`, `~`, `<<`, and `>>`.

```python
a = 6  # binary 110
b = 3  # binary 011

print(a & b)   # 2
print(a | b)   # 7
print(a ^ b)   # 5
print(a << 1)  # 12
print(a >> 1)  # 3
```

These operators are common in bit flags, low-level data processing, and algorithm problems. They differ from logical `and` and `or`.

### 5.8 Operators commonly used with lists

**Concatenation (`+`)** creates a new list:

```python
a = [1, 2]
b = [3, 4]
print(a + b)  # [1, 2, 3, 4]
```

**Repetition (`*`)** repeats list contents:

```python
print([0] * 4)  # [0, 0, 0, 0]
```

Be careful when repeating a list containing a mutable object:

```python
rows = [[]] * 3
rows[0].append("x")

print(rows)  # [['x'], ['x'], ['x']]
```

All three entries refer to the same inner list. Use a comprehension to create independent lists:

```python
rows = [[] for _ in range(3)]
rows[0].append("x")

print(rows)  # [['x'], [], []]
```

**Indexing and slicing:**

```python
numbers = [10, 20, 30, 40]

print(numbers[1])    # 20
print(numbers[1:3])  # [20, 30]
```

**Length:**

```python
print(len(numbers))  # 4
```

### 5.9 Operator precedence

Multiplication binds more tightly than addition:

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

Use parentheses to make complex expressions readable and avoid precedence mistakes.

---

## 6. Common List Bugs and Debugging

### Bug 1: Assigning the result of a mutating method

Incorrect:

```python
numbers = [3, 1, 2]
numbers = numbers.sort()
print(numbers)  # None
```

Correct:

```python
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3]
```

Use `sorted(numbers)` if a new sorted list is needed.

### Bug 2: Modifying a list while iterating over it

Risky:

```python
numbers = [1, 2, 2, 3]
for number in numbers:
    if number == 2:
        numbers.remove(number)
```

Removing elements shifts indexes and can cause items to be skipped. Prefer a new filtered list:

```python
numbers = [1, 2, 2, 3]
numbers = [number for number in numbers if number != 2]
print(numbers)  # [1, 3]
```

### Bug 3: Shared nested lists

Incorrect for independent rows:

```python
grid = [[0] * 3] * 2
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [1, 0, 0]]
```

Correct:

```python
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print(grid)  # [[1, 0, 0], [0, 0, 0]]
```

### Bug 4: Index out of range

```python
items = ["a", "b"]

if items:
    print(items[-1])  # b
```

Check list length and use exception handling only when an out-of-range index is an expected condition.

### Bug 5: Empty-list calculations

`min([])`, `max([])`, and `statistics.mean([])` raise errors. `sum([])` returns `0`.

```python
values = []

if values:
    print(min(values))
else:
    print("No values to process")
```

### Debugging checklist

1. Print or inspect `len(my_list)` and representative values.
2. Check whether a method mutates the list or returns a new object.
3. Inspect aliasing: do two names point to the same list?
4. Reproduce the issue with the smallest input possible.
5. Test empty, singleton, duplicate, and boundary cases.
6. Add a regression test once the bug is fixed.

---

## 7. Performance and Best Practices

### Time complexity overview

| Operation | Typical time complexity |
|---|---:|
| Read by index, e.g. `items[i]` | O(1) |
| Append at end | Amortized O(1) |
| Search by value (`x in items`) | O(n) |
| `count(x)` / `index(x)` | O(n) |
| Insert/remove near front | O(n) |
| Slice a list of k items | O(k) |
| Sort | O(n log n) typical |

### Production-oriented recommendations

- Use meaningful names and keep transformations small and readable.
- Prefer comprehensions for simple mapping/filtering, not complex side effects.
- Avoid repeated list concatenation in a loop when `append()` or `extend()` is clearer and more efficient.
- Do not keep unbounded data in memory.
- Use `deque` for efficient operations at both ends of a queue.
- Use a database for filtering large persistent datasets.
- Validate external data before using it.
- Avoid shared mutable default arguments in functions.

A common default-argument bug:

```python
# Avoid this pattern:
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same default list is reused across calls. Safer:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 8. Practice Exercises

### Beginner

1. Create a list of five favorite technologies and print each on a new line.
2. Print the first, third, and last elements of a list.
3. Use slicing to reverse a list without calling `reverse()`.
4. Add an item with `append()` and several items with `extend()`. Explain the difference.
5. Use `count()` to count how often `2` appears in `[2, 4, 2, 5, 2, 6]`.
6. Sort a list of integers in ascending and descending order.
7. Explain why `numbers = numbers.sort()` results in `None`.

### Intermediate

8. Remove all occurrences of a target value without modifying the list while iterating over it.
9. Remove duplicates while preserving the original order.
10. Find the second-largest distinct number in a list.
11. Filter a list of product dictionaries by stock status and maximum price.
12. Implement simple in-memory pagination using `page` and `page_size`.
13. Create a 3-by-3 grid with independent rows and update one cell.
14. Build a validation error list for a user object containing `name`, `email`, and `age`.
15. Calculate count, minimum, maximum, and average for a non-empty list of response times.

### Backend / challenge

16. Write a function that accepts a list of order dictionaries and returns the total value of paid orders.
17. Design a function that validates a list of IDs, handles an empty list, and reports invalid entries.
18. Explain why an in-memory list is not a reliable production job queue.
19. Given millions of database records, explain why filtering them all in Python may be inefficient.
20. Write tests for a list-filtering function covering empty input, duplicate values, and boundary prices.

---

## 9. Quick Revision

- A list is ordered, mutable, and allows duplicates.
- Indexing begins at `0`; negative indexes count from the end.
- Slice syntax is `items[start:stop:step]`; `stop` is excluded.
- `append(x)` adds one item; `extend(iterable)` adds each item from an iterable.
- `remove(x)` removes the first matching value; `pop()` removes and returns an item.
- `sort()` changes the list and returns `None`; `sorted()` returns a new sorted list.
- `copy()` creates a shallow copy, not a recursive deep copy.
- List membership is O(n) in the typical case; sets are often better for repeated membership checks.
- Do not mutate a list while iterating over it when that can skip elements.
- Avoid `[[...]] * n` when each nested list must be independent.
- In backend code, use lists for manageable ordered collections, but prefer database queries, streaming, durable queues, or dedicated caches when scale and reliability require them.
- `==` compares values; `is` compares object identity.
- `and` / `or` short-circuit; `in` checks membership; `is None` checks for `None`.

### Official references

- Python tutorial: https://docs.python.org/3/tutorial/
- Built-in types (including lists): https://docs.python.org/3/library/stdtypes.html
- Data structures tutorial: https://docs.python.org/3/tutorial/datastructures.html
- `collections` module: https://docs.python.org/3/library/collections.html
- Python performance and profiling tools: https://docs.python.org/3/library/profile.html

---

**End of notes.** Run the examples, predict their output before execution, and complete the exercises to build confidence with Python lists and core operations.
