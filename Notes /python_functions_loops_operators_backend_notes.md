# Python Functions, Loops, Operators & Operations
## Practical Developer Notes — Backend, Debugging, and Interview Focus

**Perspective:** Senior Python developer (4–5 years of application development experience)  
**Audience:** Beginner to intermediate Python learners preparing for practical development and interviews.

---

## Table of Contents

1. [Learning Outcomes](#1-learning-outcomes)
2. [Python Functions: Fundamentals](#2-python-functions-fundamentals)
3. [Types and Patterns of Functions](#3-types-and-patterns-of-functions)
4. [Function Arguments and Return Values](#4-function-arguments-and-return-values)
5. [Scope, Closures, and Lambda Functions](#5-scope-closures-and-lambda-functions)
6. [Practical Function Examples](#6-practical-function-examples)
7. [Real-World Loop Applications](#7-real-world-loop-applications)
8. [Backend Use Cases for Loops](#8-backend-use-cases-for-loops)
9. [Python Operators and Operations](#9-python-operators-and-operations)
10. [Debugging and Common Mistakes](#10-debugging-and-common-mistakes)
11. [Performance and Production Practices](#11-performance-and-production-practices)
12. [Practice Exercises](#12-practice-exercises)
13. [Interview Questions](#13-interview-questions)
14. [Quick Revision](#14-quick-revision)
15. [Official Documentation](#15-official-documentation)

---

## 1. Learning Outcomes

After completing these notes, you should be able to:

- Define reusable functions with clear inputs, outputs, and responsibilities.
- Understand built-in, user-defined, anonymous, recursive, generator, and asynchronous functions.
- Use positional, keyword, default, and variable-length arguments correctly.
- Explain local/global/nonlocal scope and avoid mutable-default-argument bugs.
- Use loops to validate API data, process records, aggregate metrics, paginate results, and handle batches.
- Select the right Python operator and understand operator precedence.
- Debug common function and loop errors and write code that is easier to test and maintain.

---

## 2. Python Functions: Fundamentals

A **function** is a named, reusable block of code that performs a focused task. Functions reduce duplication and make code easier to test, debug, and maintain.

### 2.1 Basic syntax

```python
def function_name(parameters):
    """Optional docstring describing the function."""
    # Function body
    return result
```

Example:

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(199.50, 3)
print(total)
```

Output:

```text
598.5
```

**How it works**
1. `def` defines the function.
2. `price` and `quantity` are parameters.
3. `calculate_total(199.50, 3)` calls the function with arguments.
4. `return` sends the result back to the caller.

### 2.2 Parameters vs. arguments

- **Parameter:** variable named in the function definition.
- **Argument:** actual value passed during the call.

```python
def greet(name):       # name is a parameter
    return f"Hello, {name}!"

message = greet("Asha")  # "Asha" is an argument
print(message)
```

Output:

```text
Hello, Asha!
```

### 2.3 `return` vs. `print`

`print()` displays information. `return` gives a value back to the caller.

```python
def add_and_print(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

result_1 = add_and_print(2, 3)
result_2 = add_and_return(2, 3)

print("result_1:", result_1)
print("result_2:", result_2)
```

Output:

```text
5
result_1: None
result_2: 5
```

A function with no explicit `return` returns `None`. In application code, return data from business-logic functions and let the calling layer decide whether to log, display, or serialize it.

### 2.4 Docstrings and type hints

```python
def calculate_discount(price: float, discount_rate: float) -> float:
    """Return a price after applying a discount rate from 0 to 1."""
    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_rate <= 1:
        raise ValueError("discount_rate must be between 0 and 1")
    return price * (1 - discount_rate)

print(calculate_discount(100.0, 0.15))
```

Output:

```text
85.0
```

Type hints document intended types and improve editor/static-analysis support. Python does **not** automatically enforce most annotations at runtime. Validate untrusted input explicitly.

---

## 3. Types and Patterns of Functions

The phrase “types of functions” can mean several different classifications. The following are common Python function forms and patterns.

### 3.1 Built-in functions

Python provides functions such as `len()`, `sum()`, `min()`, `max()`, `sorted()`, `enumerate()`, and `zip()`.

```python
scores = [78, 91, 84]
print(len(scores))
print(sum(scores))
print(max(scores))
print(sorted(scores))
```

Output:

```text
3
253
91
[78, 84, 91]
```

Use built-ins when they clearly express intent; they are usually more readable than manually implementing the same operation.

### 3.2 User-defined functions

Functions you create with `def`.

```python
def is_adult(age: int) -> bool:
    return age >= 18

print(is_adult(20))
print(is_adult(16))
```

Output:

```text
True
False
```

### 3.3 Anonymous functions (`lambda`)

A `lambda` creates a small anonymous function containing one expression. It is useful when a short callable is needed temporarily.

```python
products = [
    {"name": "Keyboard", "price": 1200},
    {"name": "Mouse", "price": 600},
    {"name": "Monitor", "price": 8500},
]

by_price = sorted(products, key=lambda product: product["price"])
print([product["name"] for product in by_price])
```

Output:

```text
['Mouse', 'Keyboard', 'Monitor']
```

Prefer a normal `def` when the logic needs multiple steps, meaningful documentation, validation, or reuse.

### 3.4 Recursive functions

A recursive function calls itself. It needs a **base case** to stop recursion.

```python
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):       # Base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

Recursion can be elegant for tree traversal and divide-and-conquer algorithms. Python has a recursion limit, so an iterative solution may be safer for deeply nested or very large input.

### 3.5 Generator functions (`yield`)

A generator function yields values one at a time instead of building and returning the entire collection at once.

```python
def even_numbers(limit: int):
    for number in range(limit + 1):
        if number % 2 == 0:
            yield number

print(list(even_numbers(8)))
```

Output:

```text
[0, 2, 4, 6, 8]
```

Generators are useful for streaming large files, processing database records in batches, and handling large datasets without holding everything in memory.

### 3.6 Asynchronous functions (`async def`)

An asynchronous function can pause at `await` while an asynchronous operation is waiting, allowing other tasks to progress under an event loop.

```python
import asyncio

async def fetch_label():
    await asyncio.sleep(0.1)  # Demonstration of non-blocking waiting
    return "record-loaded"

async def main():
    label = await fetch_label()
    print(label)

asyncio.run(main())
```

Output:

```text
record-loaded
```

Use `async` for suitable I/O-bound workloads with async-compatible libraries. It does not automatically make CPU-heavy code faster. Do not call `asyncio.run()` inside an already-running event loop, such as many notebook environments; there, use `await main()`.

### 3.7 Methods vs. functions

A method is a function associated with an object or class.

```python
text = "  python  "
print(text.strip())  # strip is a string method
```

Output:

```text
python
```

### 3.8 Pure functions vs. side-effecting functions

A **pure function** returns a result based only on its inputs and does not mutate external state. A side-effecting function may write to a file, update a database, send a message, or change shared state.

```python
def normalized_email(email: str) -> str:
    return email.strip().lower()  # Pure transformation

def print_welcome(name: str) -> None:
    print(f"Welcome, {name}!")    # Side effect: console output
```

Pure functions are easier to test and reuse. Keep I/O at application boundaries where practical.

---

## 4. Function Arguments and Return Values

### 4.1 Positional arguments

Arguments are matched by their position.

```python
def subtract(a, b):
    return a - b

print(subtract(10, 3))
```

Output: `7`

### 4.2 Keyword arguments

Arguments are matched by parameter name.

```python
def create_user(name, role):
    return {"name": name, "role": role}

print(create_user(role="developer", name="Asha"))
```

Output:

```text
{'name': 'Asha', 'role': 'developer'}
```

Keyword arguments make calls more readable when several parameters have similar types.

### 4.3 Default arguments

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Asha"))
print(greet("Asha", greeting="Welcome"))
```

Output:

```text
Hello, Asha!
Welcome, Asha!
```

**Important: avoid mutable default values.**

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same list is reused between calls. Correct approach:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("pen"))
print(add_item("book"))
```

Output:

```text
['pen']
['book']
```

### 4.4 Variable-length positional arguments: `*args`

`*args` collects extra positional arguments into a tuple.

```python
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))
```

Output: `100`

### 4.5 Variable-length keyword arguments: `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def build_profile(**details):
    return details

print(build_profile(name="Asha", role="Backend Developer", active=True))
```

Output:

```text
{'name': 'Asha', 'role': 'Backend Developer', 'active': True}
```

Use these features when variable input is a real requirement. Avoid accepting arbitrary arguments if a clear, explicit signature would be safer.

### 4.6 Positional-only and keyword-only parameters

```python
def transfer(source, destination, /, *, amount):
    return f"Transfer {amount} from {source} to {destination}"

print(transfer("A", "B", amount=500))
```

Output:

```text
Transfer 500 from A to B
```

- Parameters before `/` are positional-only.
- Parameters after `*` are keyword-only.
- These markers can make public APIs clearer and reduce accidental argument swaps.

### 4.7 Multiple return values

Python commonly returns multiple values as a tuple.

```python
def min_max(values):
    if not values:
        raise ValueError("values must not be empty")
    return min(values), max(values)

lowest, highest = min_max([8, 3, 11, 5])
print(lowest, highest)
```

Output: `3 11`

### 4.8 Early return and guard clauses

```python
def get_discounted_price(price, rate):
    if price < 0:
        raise ValueError("price cannot be negative")
    if rate < 0 or rate > 1:
        raise ValueError("rate must be between 0 and 1")
    if price == 0 or rate == 0:
        return price
    return price * (1 - rate)

print(get_discounted_price(200, 0.10))
```

Output: `180.0`

Guard clauses handle invalid or special cases early and reduce deeply nested conditionals.

---

## 5. Scope, Closures, and Lambda Functions

### 5.1 Local and global scope

```python
app_name = "Inventory API"  # Global/module-level variable

def describe_app():
    message = "Running"
    return f"{app_name}: {message}"

print(describe_app())
```

Output:

```text
Inventory API: Running
```

Variables created inside a function are generally local to that function. Minimize global mutable state because it makes tests and concurrent execution harder to reason about.

### 5.2 The `global` keyword

`global` allows assignment to a module-level variable. It exists, but passing values explicitly or using a class/object is often easier to test.

```python
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)
```

Output: `1`

### 5.3 The `nonlocal` keyword and closures

`nonlocal` refers to a variable in the nearest enclosing function scope.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())
print(counter())
```

Output:

```text
1
2
```

A closure remembers variables from its enclosing scope even after the outer function has returned.

### 5.4 Type hints for structured data

For modern Python, use built-in generic types such as `list[str]` and `dict[str, int]`.

```python
def count_words(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in words:
        normalized = word.casefold()
        counts[normalized] = counts.get(normalized, 0) + 1
    return counts

print(count_words(["API", "python", "API"]))
```

Output:

```text
{'api': 2, 'python': 1}
```

Type hints improve clarity, but they are not a replacement for runtime validation of external data.

---

## 6. Practical Function Examples

### Example 1: Validate a user payload

```python
def validate_user_payload(payload: dict) -> list[str]:
    errors = []

    if not isinstance(payload, dict):
        return ["Payload must be a dictionary"]

    name = payload.get("name")
    email = payload.get("email")

    if not isinstance(name, str) or not name.strip():
        errors.append("name is required")
    if not isinstance(email, str) or "@" not in email:
        errors.append("email must be a valid-looking string")

    return errors

payload = {"name": " Asha ", "email": "asha@example.com"}
print(validate_user_payload(payload))
```

Output:

```text
[]
```

This is a lightweight example, not complete email validation. In a real API, validate schema, field lengths, allowed values, and security constraints at the boundary.

### Example 2: Normalize user data

```python
def normalize_user(user: dict) -> dict:
    return {
        **user,
        "name": user.get("name", "").strip(),
        "email": user.get("email", "").strip().lower(),
    }

print(normalize_user({"name": " Asha ", "email": " ASHA@EXAMPLE.COM "}))
```

Output:

```text
{'name': 'Asha', 'email': 'asha@example.com'}
```

The dictionary unpacking copies existing fields and overwrites the normalized fields. This is a shallow copy; nested objects are still shared.

### Example 3: Calculate an order total safely

```python
from decimal import Decimal

def order_total(unit_price: Decimal, quantity: int) -> Decimal:
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    return unit_price * quantity

print(order_total(Decimal("19.99"), 3))
```

Output:

```text
59.97
```

For monetary calculations, prefer `Decimal` with values created from strings or validated decimal input rather than binary floating-point arithmetic.

### Example 4: Separate business logic from I/O

```python
def is_eligible_for_free_shipping(order_total: float, minimum: float = 499.0) -> bool:
    return order_total >= minimum

for amount in [250.0, 499.0, 750.0]:
    print(amount, is_eligible_for_free_shipping(amount))
```

Output:

```text
250.0 False
499.0 True
750.0 True
```

The function is easy to unit test because it does not call a database, network, or console.

### Example 5: Retry decision helper

```python
def should_retry(status_code: int, attempt: int, max_attempts: int) -> bool:
    if attempt >= max_attempts:
        return False
    return status_code in {408, 429, 500, 502, 503, 504}

print(should_retry(503, 1, 3))
print(should_retry(400, 1, 3))
print(should_retry(503, 3, 3))
```

Output:

```text
True
False
False
```

This function only decides whether to retry. Production retry logic should also use timeouts, bounded exponential backoff, jitter, idempotency where appropriate, and clear error handling.

### Example 6: A function that returns a generator

```python
def read_non_empty_lines(lines):
    for line in lines:
        cleaned = line.strip()
        if cleaned:
            yield cleaned

sample = [" first line \n", "\n", "second line\n"]
print(list(read_non_empty_lines(sample)))
```

Output:

```text
['first line', 'second line']
```

This pattern processes items lazily and can be used with file objects or streaming sources.

---

## 7. Real-World Loop Applications

Loops repeat operations over an iterable or while a condition is true. They are essential for validation, data transformation, aggregation, file processing, and batch jobs.

### 7.1 `for` loop

Use a `for` loop when iterating over a sequence or iterable.

```python
languages = ["Python", "Java", "TypeScript"]

for language in languages:
    print(language)
```

Output:

```text
Python
Java
TypeScript
```

### 7.2 `while` loop

Use a `while` loop when repetition depends on a condition. Make sure the condition can eventually become false.

```python
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}")
    attempt += 1
```

Output:

```text
Attempt 1
Attempt 2
Attempt 3
```

### 7.3 `range()`

`range(start, stop, step)` generates a sequence of integers. The `stop` value is excluded.

```python
for number in range(2, 11, 2):
    print(number)
```

Output:

```text
2
4
6
8
10
```

### 7.4 Iterate with `enumerate()`

Use `enumerate()` when both index and value are needed.

```python
tasks = ["validate", "save", "notify"]

for index, task in enumerate(tasks, start=1):
    print(index, task)
```

Output:

```text
1 validate
2 save
3 notify
```

### 7.5 Iterate over dictionaries

```python
status_counts = {"pending": 4, "completed": 12, "failed": 2}

for status, count in status_counts.items():
    print(f"{status}: {count}")
```

Output:

```text
pending: 4
completed: 12
failed: 2
```

### 7.6 Use `zip()` to process related lists

```python
names = ["Asha", "Ravi", "Meera"]
scores = [91, 78, 88]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

Output:

```text
Asha: 91
Ravi: 78
Meera: 88
```

By default, `zip()` stops at the shortest iterable. If lengths must match, validate them or use `zip(..., strict=True)` in Python 3.10+.

### 7.7 `break`, `continue`, and `pass`

- `break`: exits the nearest loop.
- `continue`: skips to the next iteration.
- `pass`: does nothing; it is a placeholder statement.

```python
for number in range(1, 6):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)
```

Output:

```text
1
3
4
```

### 7.8 Loop `else`

A loop's `else` runs if the loop finishes normally, without being terminated by `break`.

```python
numbers = [3, 7, 11]
target = 8

for number in numbers:
    if number == target:
        print("Found")
        break
else:
    print("Not found")
```

Output:

```text
Not found
```

### 7.9 Nested loops and complexity

```python
for row in range(1, 4):
    for column in range(1, 3):
        print(row, column)
```

The inner loop runs for every outer-loop iteration. If both loops process `n` items, the total work is often `O(n²)`. Avoid nested scans when a dictionary or set can reduce repeated searching.

### 7.10 List comprehensions and generator expressions

List comprehension:

```python
squares = [number * number for number in range(1, 6)]
print(squares)
```

Output: `[1, 4, 9, 16, 25]`

Generator expression:

```python
squares = (number * number for number in range(1, 6))
print(sum(squares))
```

Output: `55`

Use comprehensions for simple transformations. For complex branching, logging, error handling, or multiple side effects, a regular loop is usually easier to read.

---

## 8. Backend Use Cases for Loops

### 8.1 Validate a batch of API records

```python
records = [
    {"id": 1, "email": "asha@example.com"},
    {"id": 2, "email": ""},
    {"id": 3, "email": "ravi@example.com"},
]

valid_records = []
invalid_ids = []

for record in records:
    if record.get("id") and record.get("email", "").strip():
        valid_records.append(record)
    else:
        invalid_ids.append(record.get("id"))

print("Valid:", len(valid_records))
print("Invalid IDs:", invalid_ids)
```

Output:

```text
Valid: 2
Invalid IDs: [2]
```

For production APIs, validate types before calling string methods, and use a schema-validation library where appropriate.

### 8.2 Aggregate API status codes

```python
responses = [
    {"status": 200},
    {"status": 200},
    {"status": 404},
    {"status": 500},
    {"status": 200},
]

counts = {}
for response in responses:
    status = response.get("status", "unknown")
    counts[status] = counts.get(status, 0) + 1

print(counts)
```

Output:

```text
{200: 3, 404: 1, 500: 1}
```

This pattern can summarize request logs or batch responses. In production, metrics libraries are usually better for long-running telemetry.

### 8.3 Process records in batches

```python
def batches(items, batch_size):
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")

    for start in range(0, len(items), batch_size):
        yield items[start:start + batch_size]

records = list(range(1, 8))
for batch in batches(records, 3):
    print(batch)
```

Output:

```text
[1, 2, 3]
[4, 5, 6]
[7]
```

Batching is useful for bulk inserts, API calls, and scheduled jobs. For huge or streaming inputs, use an iterator-based batching approach rather than requiring a full list.

### 8.4 Paginate through an API conceptually

```python
def pages(items, page_size):
    if page_size <= 0:
        raise ValueError("page_size must be positive")

    for offset in range(0, len(items), page_size):
        yield items[offset:offset + page_size]

users = [f"user-{n}" for n in range(1, 8)]
for page_number, page in enumerate(pages(users, 3), start=1):
    print(page_number, page)
```

Output:

```text
1 ['user-1', 'user-2', 'user-3']
2 ['user-4', 'user-5', 'user-6']
3 ['user-7']
```

For a real remote API, use its pagination token or next-page link, configure request timeouts, handle rate limits, and stop when no next page exists.

### 8.5 Filter log events

```python
events = [
    {"level": "INFO", "message": "Server started"},
    {"level": "ERROR", "message": "Database unavailable"},
    {"level": "WARNING", "message": "Slow response"},
    {"level": "ERROR", "message": "Payment failed"},
]

errors = []
for event in events:
    if event.get("level") == "ERROR":
        errors.append(event["message"])

print(errors)
```

Output:

```text
['Database unavailable', 'Payment failed']
```

Avoid logging passwords, access tokens, personal data, or payment details. Use structured logging and appropriate retention policies in production.

### 8.6 Safely build a response payload

```python
internal_user = {
    "id": 17,
    "name": "Asha",
    "email": "asha@example.com",
    "password_hash": "DO_NOT_EXPOSE",
    "is_admin": False,
}

public_fields = ("id", "name", "email")
response = {}

for field in public_fields:
    response[field] = internal_user[field]

print(response)
```

Output:

```text
{'id': 17, 'name': 'Asha', 'email': 'asha@example.com'}
```

Explicit allowlists reduce the risk of accidentally exposing internal fields. Real applications should also enforce authorization and use response schemas/serializers.

### 8.7 Inventory aggregation

```python
items = [
    {"sku": "A1", "quantity": 4},
    {"sku": "B2", "quantity": 3},
    {"sku": "A1", "quantity": 6},
]

inventory = {}
for item in items:
    sku = item["sku"]
    inventory[sku] = inventory.get(sku, 0) + item["quantity"]

print(inventory)
```

Output:

```text
{'A1': 10, 'B2': 3}
```

### 8.8 File processing line by line

```python
from io import StringIO

file_like = StringIO("INFO started\n\nERROR failed\nINFO stopped\n")
error_lines = []

for line_number, line in enumerate(file_like, start=1):
    if "ERROR" in line:
        error_lines.append((line_number, line.strip()))

print(error_lines)
```

Output:

```text
[(3, 'ERROR failed')]
```

Iterating over a file object processes one line at a time, which is generally more memory-efficient than reading the entire file into a list.

### 8.9 Looping with bounded retries

```python
def simulated_request():
    # Demo only: real code would make an HTTP request with a timeout.
    return 503

max_attempts = 3
for attempt in range(1, max_attempts + 1):
    status = simulated_request()
    print(f"Attempt {attempt}: {status}")

    if 200 <= status < 300:
        print("Success")
        break
else:
    print("Request failed after retries")
```

Output:

```text
Attempt 1: 503
Attempt 2: 503
Attempt 3: 503
Request failed after retries
```

A real retry loop should not retry every failure indiscriminately. Distinguish transient failures from permanent ones and use bounded backoff, jitter, request timeouts, and idempotency safeguards.

### 8.10 Avoid inefficient repeated membership checks

Less efficient for repeated membership tests:

```python
allowed_ids = [101, 105, 110, 115]
requested_ids = [105, 110, 999]

matches = []
for requested_id in requested_ids:
    if requested_id in allowed_ids:
        matches.append(requested_id)

print(matches)
```

Output: `[105, 110]`

If `allowed_ids` is large and many checks are needed, convert it to a set:

```python
allowed_ids = {101, 105, 110, 115}
matches = [item_id for item_id in requested_ids if item_id in allowed_ids]
print(matches)
```

Expected average membership lookup in a set is `O(1)`, compared with `O(n)` for a list. Sets use additional memory and do not preserve duplicate entries.

---

## 9. Python Operators and Operations

An operator performs an operation on one or more operands. The value or object receiving the operation is an operand.

### 9.1 Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `8 + 3` | `11` |
| `-` | Subtraction | `8 - 3` | `5` |
| `*` | Multiplication | `8 * 3` | `24` |
| `/` | True division | `8 / 3` | `2.666...` |
| `//` | Floor division | `8 // 3` | `2` |
| `%` | Modulo/remainder | `8 % 3` | `2` |
| `**` | Exponentiation | `2 ** 3` | `8` |

```python
print(8 / 3)
print(8 // 3)
print(8 % 3)
print(2 ** 3)
```

Output:

```text
2.6666666666666665
2
2
8
```

`//` rounds down toward negative infinity, not toward zero. For example, `-7 // 3 == -3`.

### 9.2 Comparison operators

Comparison operators return Boolean values.

```python
x = 10
print(x == 10)
print(x != 5)
print(x > 7)
print(x <= 10)
```

Output:

```text
True
True
True
True
```

Common operators: `==`, `!=`, `<`, `<=`, `>`, `>=`.

Use `==` to compare values. Use `is` for object identity, especially when checking singletons such as `None`.

### 9.3 Assignment operators

```python
count = 10
count += 2
count *= 3
count -= 6
print(count)
```

Output:

```text
30
```

Common augmented assignments include `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, and `**=`. They update a variable using an operation. For mutable objects, in-place operations may mutate the object rather than create a new one.

### 9.4 Logical operators: `and`, `or`, `not`

```python
age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

Output:

```text
True
True
False
```

`and` and `or` short-circuit and return one of their operands, not necessarily a Boolean.

```python
name = ""
display_name = name or "Guest"
print(display_name)
```

Output: `Guest`

This fallback pattern works for falsy values such as empty strings, `0`, `False`, and `None`. If only `None` should trigger a fallback, use an explicit `is None` check.

### 9.5 Membership operators: `in`, `not in`

```python
roles = {"admin", "editor", "viewer"}
print("admin" in roles)
print("guest" not in roles)
```

Output:

```text
True
True
```

Membership tests work with strings, lists, tuples, sets, dictionaries, and other containers. For a dictionary, `in` checks keys by default.

### 9.6 Identity operators: `is`, `is not`

```python
value = None
print(value is None)
print(value is not None)
```

Output:

```text
True
False
```

Do not use `is` to compare ordinary strings or numbers by value. Object interning can make identity behavior appear inconsistent. Prefer `==` for value comparison.

### 9.7 Bitwise operators

Bitwise operators operate on integer bits.

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise inversion |
| `<<` | Left shift |
| `>>` | Right shift |

```python
a = 6   # Binary 110
b = 3   # Binary 011

print(a & b)
print(a | b)
print(a ^ b)
print(a << 1)
print(a >> 1)
```

Output:

```text
2
7
5
12
3
```

Bitwise operations are useful for bit masks, flags, and low-level protocols. They are not substitutes for logical `and`/`or` when working with Boolean conditions.

### 9.8 Conditional expression (ternary expression)

```python
score = 72
result = "PASS" if score >= 40 else "FAIL"
print(result)
```

Output: `PASS`

Keep conditional expressions short. For complex logic, use a regular `if`/`else` statement.

### 9.9 Operator precedence

Precedence determines which operation is evaluated first.

```python
result = 2 + 3 * 4
print(result)

result_with_parentheses = (2 + 3) * 4
print(result_with_parentheses)
```

Output:

```text
14
20
```

When an expression is not immediately clear, add parentheses rather than relying on memorized precedence rules.

### 9.10 Chained comparisons

```python
temperature = 25
print(18 <= temperature <= 30)
```

Output: `True`

This is equivalent to checking both boundaries, with the middle expression evaluated only once.

### 9.11 Common numeric and data pitfalls

**Floating-point precision**

```python
print(0.1 + 0.2)
```

Typical output:

```text
0.30000000000000004
```

Binary floating-point cannot represent every decimal exactly. Use `Decimal` for financial arithmetic or suitable tolerance-based comparisons for scientific calculations.

**Integer division**

```python
print(7 / 2)
print(7 // 2)
```

Output:

```text
3.5
3
```

**Division by zero**

```python
# 10 / 0  # Raises ZeroDivisionError
```

Validate denominators when zero is a possible input.

**Truthiness**

Falsy values include `False`, `None`, numeric zero, and empty containers/strings. Non-empty containers and most other objects are truthy.

```python
items = []
if not items:
    print("No items")
```

Output: `No items`

---

## 10. Debugging and Common Mistakes

### 10.1 Function returns `None`

**Cause:** the function prints a result but does not return it, or has no return path.

**Fix:** return the value when the caller needs to use it.

### 10.2 Mutable default argument

**Cause:** a list or dictionary default is created once when the function is defined.

**Fix:** use `None` and create a new mutable object inside the function.

### 10.3 `TypeError` while iterating or calling a function

Examples:
- Calling a non-callable value, such as `items()`, when `items` is a list.
- Adding a string and an integer without conversion or validation.
- Passing the wrong number of arguments.

**Debugging approach:** inspect the traceback, identify the exact line, check types with `type(value)`, and verify the function signature.

### 10.4 Infinite `while` loop

**Cause:** the loop condition never becomes false because the state is not updated or the exit condition is wrong.

**Fix:** make the progress variable explicit, test boundary cases, and add a bounded attempt count for retry logic.

### 10.5 Modifying a collection while iterating

Avoid removing items from a list while iterating over that same list; indexes can shift and items may be skipped.

Safer pattern:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
```

Output: `[2, 4]`

### 10.6 Catching overly broad exceptions

Avoid using `except Exception:` to hide errors without a reason. Catch expected exception types, log useful context, and re-raise or return a clearly defined error when appropriate.

### 10.7 Debugging checklist

1. Read the full traceback from the bottom upward to identify the exception and failing line.
2. Confirm the actual types and values of inputs.
3. Reproduce the bug with the smallest possible input.
4. Check empty input, boundary values, and unexpected `None`.
5. Add focused unit tests for the failing behavior.
6. Avoid logging secrets or sensitive user data.
7. Remove temporary prints or replace them with structured logging.

---

## 11. Performance and Production Practices

### 11.1 Choose the right data structure

- Use a `set` for repeated membership tests.
- Use a `dict` to aggregate counts or map IDs to records.
- Use a `deque` for efficient queue operations at both ends.
- Use a generator when processing a large stream one item at a time.

### 11.2 Think about complexity

| Pattern | Typical complexity |
|---|---|
| One pass through `n` records | `O(n)` |
| Nested loops over two `n`-item lists | `O(n²)` |
| Repeated list membership checks | `O(n)` per check |
| Average set membership | `O(1)` |
| Sorting `n` items | `O(n log n)` |

Complexity depends on the operation and data structure; these are common average-case estimates, not universal guarantees.

### 11.3 Keep functions focused

A maintainable function generally:
- Has one clear responsibility.
- Uses meaningful names and type hints.
- Validates assumptions at the correct boundary.
- Returns data rather than mixing business logic with console output.
- Raises specific exceptions for invalid states.
- Is small enough to test independently.

### 11.4 Backend architecture guideline

A useful separation of responsibilities:

- **Route/controller layer:** parses the request and returns an HTTP response.
- **Validation layer:** checks shape, types, required fields, and constraints.
- **Service/business layer:** contains functions for business rules.
- **Repository/data layer:** reads and writes persistent data.
- **Logging/metrics layer:** records operational information without leaking secrets.

Do not put all business rules, database operations, retries, and response formatting into one enormous function.

### 11.5 Testing a function

Example using plain assertions:

```python
def apply_tax(amount: float, rate: float) -> float:
    if amount < 0 or rate < 0:
        raise ValueError("amount and rate must be non-negative")
    return amount * (1 + rate)

assert apply_tax(100.0, 0.10) == 110.00000000000001
```

Floating-point exact equality can be brittle. Prefer `math.isclose()` when appropriate:

```python
import math

assert math.isclose(apply_tax(100.0, 0.10), 110.0)
print("Tests passed")
```

Output:

```text
Tests passed
```

For larger applications, use `pytest` or `unittest`, and test normal cases, invalid inputs, edge cases, and expected exceptions.

---

## 12. Practice Exercises

Try these without looking at solutions first.

### Beginner

1. Write `square(number)` and return the square.
2. Write `is_even(number)` and return a Boolean.
3. Write a function that accepts a name and optional greeting.
4. Use a loop to print every item in a list with its 1-based position.
5. Find the sum of all even numbers from 1 through 100.
6. Count how many times each character appears in a string.
7. Use `%` to determine whether a number is divisible by 3 and 5.

### Intermediate

8. Write `safe_divide(a, b)` that raises a clear error when `b == 0`.
9. Write a function that returns both the minimum and maximum of a non-empty list.
10. Normalize a list of email addresses by trimming spaces and lowercasing.
11. Aggregate order totals by customer ID using a dictionary.
12. Filter invalid records from a list of API payloads.
13. Implement a generator that yields lines containing `ERROR`.
14. Split a list into batches of a given positive size.
15. Replace repeated list membership checks with a set.
16. Use `zip()` to combine product names and prices, and validate equal lengths.

### Backend / advanced

17. Create a function that validates a user-registration payload and returns all validation errors.
18. Build a batch processor that records successes and failures without stopping the entire batch.
19. Implement a bounded retry loop that retries only transient status codes.
20. Calculate revenue by month from transaction records; handle invalid records explicitly.
21. Build a response allowlist that never includes password hashes or internal fields.
22. Compare a list-based lookup with a set-based lookup and explain the complexity.
23. Write unit tests for a discount function, including negative values and boundary rates.
24. Refactor one long function into validation, business logic, and I/O functions.

---

## 13. Interview Questions

1. What is the difference between a parameter and an argument?
2. What is the difference between `return` and `print()`?
3. What does a Python function return if there is no explicit `return`?
4. Explain positional, keyword, default, `*args`, and `**kwargs` arguments.
5. Why are mutable default arguments dangerous?
6. What is a lambda function, and when would you avoid using one?
7. What is recursion? Why is a base case required?
8. What is the difference between a generator function and a normal function?
9. When would you use `async def` in a backend service?
10. What do `global` and `nonlocal` do?
11. What is the difference between a pure function and a side-effecting function?
12. Explain `break`, `continue`, and `pass`.
13. When does a loop's `else` block execute?
14. What is the difference between a list and a set for membership checks?
15. What is the difference between `==` and `is`?
16. Explain `/`, `//`, and `%`.
17. Why can `0.1 + 0.2` produce an unexpected decimal representation?
18. What is short-circuit evaluation in `and` and `or`?
19. What is the complexity of nested loops over the same list?
20. How would you process a large file without loading it entirely into memory?
21. How would you design a retry loop for an HTTP request?
22. How do you keep sensitive fields out of API responses?
23. How do you debug an unexpected `TypeError`?
24. How would you unit-test a function that validates API input?

---

## 14. Quick Revision

### Functions

- `def`: defines a named function.
- `return`: passes a result to the caller.
- `lambda`: small anonymous expression function.
- `yield`: produces generator values lazily.
- `async def`: defines an asynchronous coroutine function.
- `*args`: extra positional arguments as a tuple.
- `**kwargs`: extra keyword arguments as a dictionary.
- Use `None` as a default when a fresh mutable value is required.
- Keep business logic focused and testable.

### Loops

- `for`: iterate over an iterable.
- `while`: repeat while a condition is true.
- `range(stop)`: integers from `0` through `stop - 1`.
- `enumerate()`: index plus item.
- `zip()`: iterate over corresponding items.
- `break`: exit the loop.
- `continue`: skip to the next iteration.
- `pass`: placeholder with no action.
- Loop `else`: runs if the loop did not end through `break`.

### Operators

- Arithmetic: `+ - * / // % **`
- Comparison: `== != < <= > >=`
- Assignment: `= += -= *= ...`
- Logical: `and or not`
- Membership: `in`, `not in`
- Identity: `is`, `is not`
- Bitwise: `& | ^ ~ << >>`
- Use `==` for value comparison and `is None` for checking `None`.
- Use parentheses when precedence is unclear.

---

## 15. Official Documentation

- Python Tutorial — Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Python Tutorial — More on Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
- Python Tutorial — Data Structures: https://docs.python.org/3/tutorial/datastructures.html
- Python Tutorial — Control Flow Tools: https://docs.python.org/3/tutorial/controlflow.html
- Python Built-in Functions: https://docs.python.org/3/library/functions.html
- Python Expressions and Operator Precedence: https://docs.python.org/3/reference/expressions.html
- Python Typing Documentation: https://docs.python.org/3/library/typing.html
- Python `asyncio` Documentation: https://docs.python.org/3/library/asyncio.html
- Python `decimal` Documentation: https://docs.python.org/3/library/decimal.html
- `unittest` Documentation: https://docs.python.org/3/library/unittest.html

---

## Final Developer Advice

When learning these topics, don't memorize syntax in isolation. For each concept:

1. Run the example.
2. Predict the output before executing it.
3. Change one input and observe the behavior.
4. Test empty, invalid, and boundary inputs.
5. Refactor the code into a small reusable function.
6. Ask whether the data structure and algorithm are appropriate for realistic input sizes.

The goal is not merely code that runs once. Aim for code that is understandable, testable, safe with real input, and straightforward to debug.
