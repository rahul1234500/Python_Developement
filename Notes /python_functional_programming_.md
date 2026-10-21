# Python Functional Programming: Real-World Problems and Solutions
### Project-oriented practice from a production Python developer's perspective

Functional programming is a way to organize computations as small functions and transformations, ideally limiting hidden state changes. Production Python often combines functional and imperative styles. Use whichever is clearest, testable, and correct.

## Core tools
- `map(fn, items)`: transform each item (returns an iterator in Python 3).
- `filter(fn, items)`: keep items where the predicate is truthy (returns an iterator).
- `sum`, `any`, `all`, `sorted`, comprehensions: often clearer than a custom reducer.
- `functools.reduce`: combine values into one result when it improves clarity.
- Pure functions: same inputs produce the same outputs without changing external state.
- `lambda`: keep it short; use named functions for meaningful business rules.

---

## 1. Normalize user records
**Use case:** Clean incoming user data before matching records.

```python
users = [
    {"id": 1, "name": "  RAHUL Kale ", "email": " RAHUL@EXAMPLE.COM "},
    {"id": 2, "name": "Mira Shah", "email": "mira@example.com "},
]

def normalize_user(user):
    return {
        **user,
        "name": user["name"].strip().title(),
        "email": user["email"].strip().lower(),
    }

print(list(map(normalize_user, users)))
```

Output:
```text
[{'id': 1, 'name': 'Rahul Kale', 'email': 'rahul@example.com'}, {'id': 2, 'name': 'Mira Shah', 'email': 'mira@example.com'}]
```

`**user` copies existing fields into a new dictionary; this function does not mutate the input record. Note that `.title()` is not correct for every person's name, so production normalization rules need care.

## 2. Filter active users
**Use case:** Select records for an active-user dashboard.

```python
users = [
    {"id": 1, "name": "Asha", "active": True},
    {"id": 2, "name": "Dev", "active": False},
    {"id": 3, "name": "Mira", "active": True},
]

active_users = list(filter(lambda user: user["active"], users))
print([user["name"] for user in active_users])
```

Output: `['Asha', 'Mira']`

A readable alternative is `[user for user in users if user["active"]]`. Do not rely on a client-provided `active` field for authorization; access control must be enforced by trusted backend logic.

## 3. Transform database rows into safe API responses
**Use case:** Return only public fields, never internal secrets.

```python
rows = [
    {"id": 101, "name": "Asha", "password_hash": "internal-1", "role": "admin"},
    {"id": 102, "name": "Dev", "password_hash": "internal-2", "role": "user"},
]

def public_user(row):
    return {"id": row["id"], "name": row["name"], "role": row["role"]}

print(list(map(public_user, rows)))
```

Output:
```text
[{'id': 101, 'name': 'Asha', 'role': 'admin'}, {'id': 102, 'name': 'Dev', 'role': 'user'}]
```

Explicit response schemas help prevent accidental exposure of internal fields.

## 4. Calculate shopping cart subtotal
**Use case:** Calculate the cost of all cart line items.

```python
cart = [
    {"product": "Keyboard", "quantity": 2, "price": 1500},
    {"product": "Mouse", "quantity": 1, "price": 700},
    {"product": "USB cable", "quantity": 3, "price": 200},
]

subtotal = sum(map(lambda item: item["quantity"] * item["price"], cart))
print(subtotal)
```

Output: `4300`

For production financial calculations, prefer `decimal.Decimal` or integer minor units, validate values, and define tax, shipping, discount, currency, and rounding rules.

## 5. Apply a discount
**Use case:** Give 10% off products priced at ₹1,000 or more.

```python
products = [
    {"name": "Bag", "price": 1200},
    {"name": "Bottle", "price": 400},
    {"name": "Shoes", "price": 2500},
]

def discounted(product):
    rate = 0.10 if product["price"] >= 1000 else 0
    return {
        **product,
        "discount": round(product["price"] * rate, 2),
        "final_price": round(product["price"] * (1 - rate), 2),
    }

print(list(map(discounted, products)))
```

Output:
```text
[{'name': 'Bag', 'price': 1200, 'discount': 120.0, 'final_price': 1080.0}, {'name': 'Bottle', 'price': 400, 'discount': 0, 'final_price': 400}, {'name': 'Shoes', 'price': 2500, 'discount': 250.0, 'final_price': 2250.0}]
```

Real discount policies may depend on coupons, customer segments, date windows, category restrictions, and whether discounts can be combined.

## 6. Validate signup input
**Use case:** Return field errors without changing the request payload.

```python
def validate_signup(payload):
    errors = {}
    email = payload.get("email", "").strip()
    password = payload.get("password", "")

    if not email or "@" not in email:
        errors["email"] = "Enter a valid email address"
    if len(password) < 8:
        errors["password"] = "Password must contain at least 8 characters"
    return errors

print(validate_signup({"email": "bad-email", "password": "123"}))
```

Output:
```text
{'email': 'Enter a valid email address', 'password': 'Password must contain at least 8 characters'}
```

A real application needs an agreed validation policy. Passwords must be hashed with an appropriate password-hashing library before storage.

## 7. Remove duplicate records by ID
**Use case:** Keep the first occurrence of each record while preserving input order.

```python
records = [
    {"id": 1, "name": "Asha"},
    {"id": 2, "name": "Dev"},
    {"id": 1, "name": "Duplicate"},
    {"id": 3, "name": "Mira"},
]

def unique_by_id(records):
    seen = set()
    result = []
    for record in records:
        if record["id"] not in seen:
            seen.add(record["id"])
            result.append(record)
    return result

print(unique_by_id(records))
```

Output:
```text
[{'id': 1, 'name': 'Asha'}, {'id': 2, 'name': 'Dev'}, {'id': 3, 'name': 'Mira'}]
```

This uses a loop deliberately: a `seen` set makes the algorithm easy to read and typically O(n) time. Functional programming does not ban loops.

## 8. Group orders by status
**Use case:** Prepare counts or lists for an operations dashboard.

```python
from collections import defaultdict

orders = [
    {"id": 1, "status": "paid"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "paid"},
]

def group_orders(orders):
    groups = defaultdict(list)
    for order in orders:
        groups[order["status"]].append(order["id"])
    return dict(groups)

print(group_orders(orders))
```

Output: `{'paid': [1, 3], 'pending': [2]}`

A clear loop is often better than forcing grouping into a complex `reduce()` expression.

## 9. Count API response statuses
**Use case:** Summarize response codes from a log batch.

```python
from collections import Counter

codes = [200, 200, 404, 500, 200, 404, 201]
print(dict(Counter(codes)))
```

Output: `{200: 3, 404: 2, 500: 1, 201: 1}`

For ongoing production monitoring, use a metrics system rather than relying on an in-memory counter.

## 10. Rank products by popularity
**Use case:** Sort products by units sold, highest first.

```python
products = [
    {"name": "Keyboard", "sold": 90},
    {"name": "Mouse", "sold": 150},
    {"name": "Monitor", "sold": 60},
]

ranked = sorted(products, key=lambda product: product["sold"], reverse=True)
print([product["name"] for product in ranked])
```

Output: `['Mouse', 'Keyboard', 'Monitor']`

`sorted()` returns a new list. For very large datasets, sorting at the database or analytics layer may be more appropriate.

## 11. Build a paginated API response
**Use case:** Return a page of products plus metadata.

```python
products = [{"id": i, "name": f"Product {i}"} for i in range(1, 6)]

def paginate(items, page=1, page_size=2):
    if page < 1 or page_size < 1:
        raise ValueError("page and page_size must be positive")
    start = (page - 1) * page_size
    return {
        "items": items[start:start + page_size],
        "page": page,
        "page_size": page_size,
        "total": len(items),
        "total_pages": (len(items) + page_size - 1) // page_size,
    }

print(paginate(products, page=2, page_size=2))
```

Output:
```text
{'items': [{'id': 3, 'name': 'Product 3'}, {'id': 4, 'name': 'Product 4'}], 'page': 2, 'page_size': 2, 'total': 5, 'total_pages': 3}
```

In a production API, cap `page_size` and usually paginate in the database rather than loading every row.

## 12. Sum successful payment transactions
**Use case:** Calculate a report total. This does not authorize or execute payments.

```python
from decimal import Decimal

transactions = [
    {"id": "tx-1", "status": "success", "amount": Decimal("120.50")},
    {"id": "tx-2", "status": "failed", "amount": Decimal("75.00")},
    {"id": "tx-3", "status": "success", "amount": Decimal("20.00")},
]

successful = filter(lambda tx: tx["status"] == "success", transactions)
total = sum((tx["amount"] for tx in successful), Decimal("0.00"))
print(total)
```

Output: `140.50`

Production payment workflows need idempotency, trusted provider/ledger status, audit trails, and reconciliation. Keep this calculation separate from side-effectful payment operations.

## 13. Calculate monthly revenue
**Use case:** Aggregate paid sales by month.

```python
from collections import defaultdict
from decimal import Decimal

sales = [
    {"date": "2026-01-05", "status": "paid", "amount": Decimal("100.00")},
    {"date": "2026-01-20", "status": "paid", "amount": Decimal("50.00")},
    {"date": "2026-02-02", "status": "paid", "amount": Decimal("80.00")},
    {"date": "2026-02-12", "status": "refunded", "amount": Decimal("20.00")},
]

def monthly_revenue(sales):
    totals = defaultdict(lambda: Decimal("0.00"))
    for sale in sales:
        if sale["status"] == "paid":
            totals[sale["date"][:7]] += sale["amount"]
    return dict(totals)

print(monthly_revenue(sales))
```

Output:
```text
{'2026-01': Decimal('150.00'), '2026-02': Decimal('80.00')}
```

Accounting rules must explicitly define refunds, chargebacks, taxes, time zones, and reporting periods.

## 14. Flatten nested API data
**Use case:** Convert an order payload into rows for CSV/reporting.

```python
order = {
    "order_id": "ORD-10",
    "customer": {"id": 7, "name": "Asha"},
    "items": [
        {"sku": "PEN", "quantity": 2},
        {"sku": "BOOK", "quantity": 1},
    ],
}

rows = [
    {
        "order_id": order["order_id"],
        "customer_id": order["customer"]["id"],
        "customer_name": order["customer"]["name"],
        "sku": item["sku"],
        "quantity": item["quantity"],
    }
    for item in order["items"]
]
print(rows)
```

Output:
```text
[{'order_id': 'ORD-10', 'customer_id': 7, 'customer_name': 'Asha', 'sku': 'PEN', 'quantity': 2}, {'order_id': 'ORD-10', 'customer_id': 7, 'customer_name': 'Asha', 'sku': 'BOOK', 'quantity': 1}]
```

Validate nested keys when payloads come from external systems.

## 15. Filter log events by severity
**Use case:** Extract warnings and errors from a log batch.

```python
logs = [
    {"message": "Server started", "level": "INFO"},
    {"message": "Cache miss", "level": "WARNING"},
    {"message": "Database unavailable", "level": "ERROR"},
]

important = list(filter(
    lambda event: event["level"] in {"WARNING", "ERROR"},
    logs,
))
print([event["message"] for event in important])
```

Output: `['Cache miss', 'Database unavailable']`

Use structured logging and centralized alerting in real production systems.

## 16. Compose a normalization and filtering pipeline
**Use case:** Return normalized emails for active customers.

```python
customers = [
    {"email": " ASHA@EXAMPLE.COM ", "active": True},
    {"email": "dev@example.com", "active": False},
    {"email": " MIRA@example.com ", "active": True},
]

def normalize(customer):
    return {**customer, "email": customer["email"].strip().lower()}

pipeline = map(
    lambda customer: customer["email"],
    filter(lambda customer: customer["active"], map(normalize, customers)),
)
print(list(pipeline))
```

Output: `['asha@example.com', 'mira@example.com']`

`map()` and `filter()` return iterators. Materialize with `list()` if you need to keep the result; a consumed iterator generally cannot be reused. A list comprehension may be more readable for simple pipelines.

## 17. Mask an email before logging
**Use case:** Reduce exposure of personal data in diagnostic output.

```python
def mask_email(email):
    local, separator, domain = email.partition("@")
    if not separator or not local:
        return "[invalid-email]"
    return f"{local[0]}***@{domain.lower()}"

print(mask_email("rahul@example.com"))
```

Output: `r***@example.com`

Masking is not anonymization. Avoid logging personal data unless necessary and follow the organization's data-handling policy.

## 18. Find data-quality issues
**Use case:** Separate records missing required fields.

```python
records = [
    {"id": 1, "email": "a@example.com"},
    {"id": 2, "email": ""},
    {"id": 3},
]

def validate(record):
    errors = []
    if not record.get("id"):
        errors.append("missing_id")
    if not record.get("email", "").strip():
        errors.append("missing_email")
    return {"record": record, "errors": errors}

results = list(map(validate, records))
invalid = list(filter(lambda result: result["errors"], results))
print([{"id": item["record"].get("id"), "errors": item["errors"]} for item in invalid])
```

Output:
```text
[{'id': 2, 'errors': ['missing_email']}, {'id': 3, 'errors': ['missing_email']}]
```

Define validation rules explicitly; for example, decide whether ID `0` is valid and how email formats should be checked.

## 19. Compare inventory snapshots
**Use case:** Find stock changes between two snapshots.

```python
before = {"PEN": 100, "BOOK": 40, "BAG": 12}
after = {"PEN": 80, "BOOK": 40, "BAG": 15, "MUG": 7}

skus = before.keys() | after.keys()
changes = {
    sku: after.get(sku, 0) - before.get(sku, 0)
    for sku in skus
    if before.get(sku, 0) != after.get(sku, 0)
}
print(changes)
```

The dictionary contains changes `PEN: -20`, `BAG: 3`, and `MUG: 7` (key order may vary). This identifies differences, but transaction history is needed to explain why stock changed.

## 20. Make a retry decision using a pure function
**Use case:** Decide whether an operation is eligible for retry. This function does not execute the retry.

```python
RETRYABLE_ERRORS = {"timeout", "temporary_unavailable"}

def should_retry(attempt, max_attempts, error_type):
    return attempt < max_attempts and error_type in RETRYABLE_ERRORS

print(should_retry(1, 3, "timeout"))
print(should_retry(3, 3, "timeout"))
print(should_retry(1, 3, "invalid_request"))
```

Output:
```text
True
False
False
```

Production retries need timeouts, bounded backoff, jitter where appropriate, and idempotency safeguards for operations with side effects.

## 21. Calculate employee bonuses
**Use case:** Apply a simple performance rating policy.

```python
employees = [
    {"name": "Asha", "rating": 5, "salary": 60000},
    {"name": "Dev", "rating": 3, "salary": 50000},
    {"name": "Mira", "rating": 4, "salary": 70000},
]

def bonus(employee):
    rate = {5: 0.15, 4: 0.10, 3: 0.05}.get(employee["rating"], 0)
    return {"name": employee["name"], "bonus": round(employee["salary"] * rate, 2)}

print(list(map(bonus, employees)))
```

Output:
```text
[{'name': 'Asha', 'bonus': 9000.0}, {'name': 'Dev', 'bonus': 2500.0}, {'name': 'Mira', 'bonus': 7000.0}]
```

Real compensation systems require approved policy, access controls, precise monetary representation, and audit trails.

## 22. Sort available products after normalization
**Use case:** Prepare a clean product list for a UI.

```python
products = [
    {"name": " keyboard ", "stock": 5},
    {"name": "Mouse", "stock": 0},
    {"name": " monitor ", "stock": 3},
]

available_names = sorted(
    product["name"].strip().title()
    for product in products
    if product["stock"] > 0
)
print(available_names)
```

Output: `['Keyboard', 'Monitor']`

This generator expression filters and transforms items, while `sorted()` creates a sorted list.

---

## Production guidelines

1. Keep business-rule functions small, deterministic, and testable.
2. Make side effects explicit: database writes, network requests, emails, payments, and logging should not be hidden inside `map()` or `filter()` callbacks.
3. Validate external input at API boundaries; dictionary keys may be missing and values may have unexpected types.
4. Prefer named functions over complicated lambdas.
5. Use `Decimal` or integer minor units for money.
6. Do not expose internal database fields or secrets in API responses.
7. Remember `map()` and `filter()` are lazy iterators in Python 3.
8. Avoid forcing functional syntax where a simple loop is clearer.
9. Test typical, empty, boundary, malformed, and duplicate inputs.
10. Measure performance before optimizing; concise code is not automatically faster.

## Practice challenges

Try these without looking up a solution first:
1. Filter customers who have verified email and an active account.
2. Calculate order value grouped by customer ID.
3. Return the top three products by revenue.
4. Normalize phone numbers according to a defined rule.
5. Group support tickets by priority and count each group.
6. Compare two user snapshots and list changed fields.
7. Validate CSV rows and separate valid from invalid records.
8. Calculate daily transaction totals using `Decimal`.
9. Build a pipeline that normalizes, filters, and sorts employee records.
10. Explain which parts of a payment workflow should be pure and which parts need side effects.

## Interview questions

**1. What is a pure function?**  
A function whose output depends on explicit inputs and which does not mutate external state or cause observable side effects.

**2. Difference between `map()` and `filter()`?**  
`map()` transforms each item; `filter()` selects items whose predicate is truthy.

**3. Why use a generator expression with `sum()`?**  
It can aggregate values without allocating an intermediate list.

**4. What is a higher-order function?**  
A function that accepts a function as an argument, returns a function, or both.

**5. When should `reduce()` be used?**  
When combining a sequence into one value and it is clearer than a built-in such as `sum()`, `any()`, or `all()`.

**6. Does functional programming always improve performance?**  
No. Performance depends on the algorithm, data size, allocation, and implementation.

**7. Should all backend code be functional?**  
No. I/O and orchestration have side effects. Keep those explicit and isolate pure business rules where practical.

## Recommended learning sequence

1. Functions, parameters, return values, and scope.
2. Pure functions and side effects.
3. `lambda`, `map()`, and `filter()`.
4. Comprehensions and generator expressions.
5. `any()`, `all()`, `sum()`, `sorted()`, `min()`, and `max()`.
6. `functools.reduce()` and function composition.
7. Immutability, shallow copies, and data transformations.
8. Unit testing pure functions.
9. Build a mini order-reporting API with validation, filtering, grouping, and pagination.

## Official documentation

- [Python Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)
- [Built-in functions](https://docs.python.org/3/library/functions.html)
- [`functools.reduce`](https://docs.python.org/3/library/functools.html#functools.reduce)
- [`collections.Counter` and `defaultdict`](https://docs.python.org/3/library/collections.html)
- [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html)

## Final takeaway

Use functional programming to create predictable, testable transformations. Use imperative code when explicit state, complex branching, or orchestration makes the workflow clearer. Strong production Python combines both styles intentionally.
