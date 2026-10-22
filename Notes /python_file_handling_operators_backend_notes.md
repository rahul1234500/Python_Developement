# Python File Handling, Operators & Operations
## Practical Developer Notes — Backend, Debugging, and Interview Focus

**Perspective:** Senior Python developer with 4–5 years of application development and debugging experience  
**Audience:** Beginner to intermediate Python learners building practical Python and backend skills.

---

## Table of Contents

1. [Learning Outcomes](#1-learning-outcomes)
2. [File Handling Fundamentals](#2-file-handling-fundamentals)
3. [Opening Files and File Modes](#3-opening-files-and-file-modes)
4. [Reading Files](#4-reading-files)
5. [Writing, Appending, and Creating Files](#5-writing-appending-and-creating-files)
6. [Context Managers and Resource Safety](#6-context-managers-and-resource-safety)
7. [Paths, Directories, and File Metadata](#7-paths-directories-and-file-metadata)
8. [Working with CSV, JSON, and Text Files](#8-working-with-csv-json-and-text-files)
9. [Exceptions and Robust File Handling](#9-exceptions-and-robust-file-handling)
10. [Real-World File Handling Applications](#10-real-world-file-handling-applications)
11. [Backend File Handling Use Cases](#11-backend-file-handling-use-cases)
12. [Python Operators and Operations](#12-python-operators-and-operations)
13. [Debugging and Common Mistakes](#13-debugging-and-common-mistakes)
14. [Security, Reliability, and Performance](#14-security-reliability-and-performance)
15. [Practice Exercises](#15-practice-exercises)
16. [Interview Questions](#16-interview-questions)
17. [Quick Revision](#17-quick-revision)
18. [Official Documentation](#18-official-documentation)

---

## 1. Learning Outcomes

By the end of these notes, you should be able to:

- Open, read, write, append, and safely close files.
- Choose appropriate file modes and understand text versus binary I/O.
- Use `with` statements, `pathlib`, and exception handling correctly.
- Read and write CSV and JSON data for application workflows.
- Process large files without loading all data into memory.
- Design practical file-processing utilities for logs, reports, imports, and uploads.
- Understand operators and common numeric/data pitfalls.
- Identify common file bugs involving paths, encodings, permissions, partial writes, and unsafe filenames.

---

## 2. File Handling Fundamentals

**File handling** means reading data from files and writing data to files. Python can work with text files, structured data files, images, archives, PDFs, and other binary formats.

Common use cases:

- Read application configuration.
- Process CSV exports and JSON payloads.
- Write logs, reports, and generated files.
- Import user or product records.
- Process uploaded files.
- Read large files line by line.
- Save application data or temporary artifacts.

### 2.1 Basic workflow

A typical file operation follows this pattern:

1. Identify the correct file path.
2. Open the file in the appropriate mode and encoding.
3. Read or write the required content.
4. Handle expected errors.
5. Ensure the file is closed.

```python
from pathlib import Path

path = Path("hello.txt")
path.write_text("Hello, Python!\n", encoding="utf-8")

text = path.read_text(encoding="utf-8")
print(text, end="")
```

Output:

```text
Hello, Python!
```

`Path.write_text()` and `Path.read_text()` are convenient for small text files. For large files, prefer streaming with `open()`.

### 2.2 Text files vs. binary files

- **Text mode:** reads or writes `str` values and uses an encoding such as UTF-8.
- **Binary mode:** reads or writes raw `bytes`; no text encoding/decoding is applied.

Use text mode for `.txt`, `.csv`, and JSON text. Use binary mode for images, PDFs, compressed archives, audio, and other binary formats.

---

## 3. Opening Files and File Modes

Use Python's built-in `open()` function:

```python
file = open("notes.txt", mode="r", encoding="utf-8")
```

For text files, explicitly specify `encoding="utf-8"` unless a different encoding is required by the file format or source.

### 3.1 Common file modes

| Mode | Meaning | Behavior |
|---|---|---|
| `"r"` | Read | File must already exist |
| `"w"` | Write | Creates file or truncates existing file |
| `"a"` | Append | Writes at the end; creates file if missing |
| `"x"` | Exclusive create | Fails if file already exists |
| `"b"` | Binary modifier | Use with another mode, e.g. `"rb"` |
| `"t"` | Text modifier | Default mode, e.g. `"rt"` |
| `"+"` | Read and write | Combine with another mode, e.g. `"r+"` |

Examples:

```python
open("input.txt", "r", encoding="utf-8")   # Read text
open("output.txt", "w", encoding="utf-8")  # Replace/create text
open("events.log", "a", encoding="utf-8")  # Append text
open("photo.png", "rb")                    # Read bytes
open("archive.zip", "wb")                  # Write bytes
```

**Warning:** `"w"` immediately truncates an existing file. Do not use it when you intend to preserve the old contents.

### 3.2 Exclusive file creation

```python
from pathlib import Path

path = Path("new-report.txt")
try:
    with path.open("x", encoding="utf-8") as file:
        file.write("First report\n")
    print("Created")
except FileExistsError:
    print("File already exists")
```

Expected output depends on whether `new-report.txt` already exists:

```text
Created
```

or:

```text
File already exists
```

Exclusive creation is useful when overwriting an existing file would be a mistake.

### 3.3 File pointers and seek operations

File objects maintain a current position. Reading advances the position.

```python
from io import StringIO

file = StringIO("ABCDE")
print(file.read(2))
print(file.tell())
file.seek(0)
print(file.read(3))
```

Output:

```text
AB
2
ABC
```

`seek()` changes the position and `tell()` reports it. Seeking is most straightforward with regular files and binary streams; not every text stream supports arbitrary byte-position seeking.

---

## 4. Reading Files

### 4.1 Read the entire file with `read()`

```python
from io import StringIO

file = StringIO("Python\nJava\nSQL\n")
content = file.read()
print(content)
```

Output:

```text
Python
Java
SQL
```

`read()` without a size reads the remaining content into memory. Use it for small files, not arbitrarily large files.

### 4.2 Read one line with `readline()`

```python
from io import StringIO

file = StringIO("first\nsecond\nthird\n")
print(file.readline(), end="")
print(file.readline(), end="")
```

Output:

```text
first
second
```

A subsequent call reads the next line. At end-of-file, `readline()` returns an empty string.

### 4.3 Read all lines with `readlines()`

```python
from io import StringIO

file = StringIO("red\nblue\ngreen\n")
lines = file.readlines()
print(lines)
```

Output:

```text
['red\n', 'blue\n', 'green\n']
```

`readlines()` returns a list and retains newline characters unless configured or processed otherwise. It can consume substantial memory for large files.

### 4.4 Recommended: iterate line by line

```python
from io import StringIO

file = StringIO("INFO started\nERROR failed\nINFO stopped\n")

for line_number, line in enumerate(file, start=1):
    print(line_number, line.strip())
```

Output:

```text
1 INFO started
2 ERROR failed
3 INFO stopped
```

This is generally more memory-efficient because it processes one line at a time.

### 4.5 Read only a bounded amount

```python
from io import StringIO

file = StringIO("abcdefghij")
chunk = file.read(4)
print(chunk)
print(file.read(4))
```

Output:

```text
abcd
efgh
```

Chunked reading is useful when processing large text or binary files, streaming data, or copying files.

---

## 5. Writing, Appending, and Creating Files

### 5.1 Write text with `write()`

```python
from io import StringIO

file = StringIO()
characters_written = file.write("Python file handling")
print(characters_written)
print(file.getvalue())
```

Output:

```text
21
Python file handling
```

`write()` returns the number of characters written for a text stream. Do not assume one call to a lower-level binary stream will always write all requested bytes; robust low-level code may need to handle partial writes.

### 5.2 Write multiple lines with `writelines()`

`writelines()` writes each string as provided; it does **not** add newline characters automatically.

```python
from io import StringIO

file = StringIO()
file.writelines(["Python\n", "Java\n", "SQL\n"])
print(file.getvalue(), end="")
```

Output:

```text
Python
Java
SQL
```

### 5.3 Append content

```python
from pathlib import Path

path = Path("activity.log")
with path.open("a", encoding="utf-8") as file:
    file.write("Application started\n")
```

Append mode preserves existing content and adds new content at the end. Concurrent writers can still require coordination depending on the platform, filesystem, and logging requirements.

### 5.4 Create a file only if it does not exist

Use `"x"` mode for exclusive creation or use a suitable file-management strategy based on the application's concurrency needs. Checking `exists()` and then creating a file is vulnerable to a time-of-check/time-of-use race if another process can create it between those steps.

### 5.5 Overwrite vs. append

```python
from pathlib import Path

path = Path("sample.txt")
path.write_text("Version 1\n", encoding="utf-8")
path.write_text("Version 2\n", encoding="utf-8")  # Overwrites
print(path.read_text(encoding="utf-8"), end="")
```

Output:

```text
Version 2
```

To preserve earlier contents, open the file in append mode or use a format designed for incremental records.

---

## 6. Context Managers and Resource Safety

### 6.1 Why use `with open(...)`?

A context manager ensures the file is closed when the block exits, including when an exception occurs.

Recommended:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Avoid relying on the garbage collector to close file handles.

### 6.2 Write and read using a context manager

```python
from pathlib import Path

path = Path("greeting.txt")

with path.open("w", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("World\n")

with path.open("r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Output:

```text
Hello
World
```

### 6.3 `flush()` vs. `close()`

- `flush()` pushes buffered data toward the underlying stream.
- `close()` flushes and releases the file resource.
- `with` handles normal closing automatically.
- Neither `flush()` nor `close()` alone guarantees that data is safely persisted through every hardware or filesystem failure scenario.

For high-value data, understand the storage system's durability guarantees and use appropriate atomic-write or synchronization strategies.

### 6.4 Safe replacement with a temporary file

For configuration or generated reports, writing a temporary file and then replacing the destination can prevent readers from seeing a partially written output in many common local-filesystem scenarios.

```python
from pathlib import Path
import os

destination = Path("settings.txt")
temporary = destination.with_suffix(".tmp")

temporary.write_text("mode=production\n", encoding="utf-8")
os.replace(temporary, destination)
print(destination.read_text(encoding="utf-8"), end="")
```

Output:

```text
mode=production
```

Important caveats:
- Temporary and destination files should normally be on the same filesystem for atomic replacement semantics.
- This example is simplified; robust production code should clean up temporary files on failure and consider permissions, concurrent writers, and durability requirements.
- Do not use this pattern as a substitute for a database transaction when multiple related records must change together.

---

## 7. Paths, Directories, and File Metadata

### 7.1 Prefer `pathlib.Path`

`pathlib` provides a readable, cross-platform API for filesystem paths.

```python
from pathlib import Path

path = Path("data") / "users.txt"
print(path.name)
print(path.suffix)
print(path.parent)
```

Typical output:

```text
users.txt
.txt
data
```

Path output may vary slightly depending on the operating system and path representation.

### 7.2 Current working directory

```python
from pathlib import Path

print(Path.cwd())
```

This prints the process's current working directory. Relative paths are resolved from that directory, which may differ between an IDE, terminal, notebook, test runner, and deployed service.

### 7.3 Create directories

```python
from pathlib import Path

directory = Path("output/reports")
directory.mkdir(parents=True, exist_ok=True)
print(directory.exists())
```

Output:

```text
True
```

`parents=True` creates missing parent directories. `exist_ok=True` avoids an error if the target directory already exists.

### 7.4 Check file type and size

```python
from pathlib import Path

path = Path("example.txt")
path.write_text("Hello", encoding="utf-8")

print(path.exists())
print(path.is_file())
print(path.stat().st_size)
```

Output:

```text
True
True
5
```

`st_size` is measured in bytes, not necessarily characters. A Unicode character may occupy multiple bytes in UTF-8.

### 7.5 List files

```python
from pathlib import Path

directory = Path(".")

for path in directory.iterdir():
    if path.is_file():
        print(path.name)
```

The output depends on the contents of the current directory. Use `glob()` or `rglob()` to match filename patterns. Avoid recursively scanning huge or untrusted directory trees without limits.

### 7.6 Absolute vs. relative paths

- **Relative path:** interpreted from the current working directory or another defined base.
- **Absolute path:** identifies a location from the filesystem root or drive.

In applications, build paths from a known application directory or explicit configuration instead of assuming the process always starts from a particular folder.

---

## 8. Working with CSV, JSON, and Text Files

### 8.1 Read CSV with `csv.DictReader`

Use the standard-library `csv` module rather than splitting CSV lines on commas. CSV values may contain quoted commas, quotes, or embedded newlines.

```python
import csv
from io import StringIO

csv_text = "id,name,active\n1,Asha,true\n2,Ravi,false\n"
file = StringIO(csv_text)

for row in csv.DictReader(file):
    print(row["id"], row["name"], row["active"])
```

Output:

```text
1 Asha true
2 Ravi false
```

CSV fields are strings by default. Convert and validate types explicitly.

### 8.2 Write CSV with `csv.DictWriter`

```python
import csv
from io import StringIO

buffer = StringIO(newline="")
writer = csv.DictWriter(buffer, fieldnames=["id", "name"])
writer.writeheader()
writer.writerow({"id": 1, "name": "Asha"})
writer.writerow({"id": 2, "name": "Ravi"})

print(buffer.getvalue(), end="")
```

Output:

```text
id,name
1,Asha
2,Ravi
```

When opening a real CSV file for writing, use `newline=""` as recommended by the CSV module documentation:

```python
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name"])
    writer.writeheader()
    writer.writerow({"id": 1, "name": "Asha"})
```

### 8.3 Read JSON

```python
import json
from io import StringIO

json_text = '{"id": 7, "name": "Asha", "active": true}'
data = json.load(StringIO(json_text))
print(data["name"])
print(data["active"])
```

Output:

```text
Asha
True
```

- `json.load(file_object)` reads JSON from a file-like object.
- `json.loads(string)` parses a JSON string.
- `json.dump(data, file_object)` writes JSON to a file-like object.
- `json.dumps(data)` returns a JSON string.

### 8.4 Write JSON

```python
import json
from io import StringIO

data = {"id": 7, "name": "Asha", "active": True}
buffer = StringIO()
json.dump(data, buffer, indent=2)
print(buffer.getvalue())
```

Output:

```json
{
  "id": 7,
  "name": "Asha",
  "active": true
}
```

JSON is a data-interchange format, not a secure serialization format for arbitrary Python objects. Do not use `pickle` to load untrusted files because unpickling can execute code.

### 8.5 JSON parse errors

```python
import json

try:
    data = json.loads('{"name": }')
except json.JSONDecodeError as error:
    print("Invalid JSON")
```

Output:

```text
Invalid JSON
```

In a backend service, log safe diagnostic context and return an appropriate validation error rather than exposing internal tracebacks to clients.

### 8.6 Encoding and Unicode

Prefer UTF-8 for text files when appropriate:

```python
from pathlib import Path

path = Path("unicode.txt")
path.write_text("नमस्ते Python 🌱\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"), end="")
```

Output:

```text
नमस्ते Python 🌱
```

An incorrect encoding can cause `UnicodeDecodeError` or corrupted text. If you must process a legacy file, determine its actual encoding instead of guessing.

---

## 9. Exceptions and Robust File Handling

### 9.1 Common file exceptions

| Exception | Typical cause |
|---|---|
| `FileNotFoundError` | Requested file or path does not exist |
| `PermissionError` | Process lacks required permission |
| `IsADirectoryError` | A file operation was attempted on a directory |
| `NotADirectoryError` | A path component expected to be a directory is not one |
| `UnicodeDecodeError` | Bytes cannot be decoded using the selected encoding |
| `UnicodeEncodeError` | Text cannot be encoded using the selected encoding |
| `json.JSONDecodeError` | Input is not valid JSON |
| `csv.Error` | CSV parsing/writing issue |

### 9.2 Handle expected errors specifically

```python
from pathlib import Path

path = Path("missing-input.txt")

try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("Input file was not found")
except PermissionError:
    print("Permission denied")
else:
    print(content)
```

Output for a missing file:

```text
Input file was not found
```

Avoid catching every exception just to suppress it. Handle known failure modes, log appropriately, and let unexpected errors surface to the correct error-handling layer.

### 9.3 Validate file size before reading

```python
from pathlib import Path

path = Path("upload.bin")
max_bytes = 10 * 1024 * 1024  # 10 MiB

if path.exists() and path.is_file():
    if path.stat().st_size > max_bytes:
        print("File too large")
    else:
        print("File size accepted")
else:
    print("File does not exist")
```

This example demonstrates a basic size check. In a production upload path, enforce size limits while receiving/streaming the data too; checking afterward may be too late to prevent resource exhaustion.

### 9.4 Preserve the original error context

```python
from pathlib import Path

def read_config(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise RuntimeError(f"Could not read configuration: {path.name}") from error
```

Exception chaining with `from error` preserves the underlying cause for debugging. Do not include secrets or sensitive full paths in client-facing error messages.

---

## 10. Real-World File Handling Applications

### 10.1 Process an application log line by line

```python
from pathlib import Path

log_path = Path("application.log")
log_path.write_text(
    "INFO service started\nERROR database timeout\nINFO request completed\n",
    encoding="utf-8",
)

error_count = 0
with log_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if "ERROR" in line:
            error_count += 1
            print(line_number, line.strip())

print("Total errors:", error_count)
```

Output:

```text
2 ERROR database timeout
Total errors: 1
```

For real logs, use structured logging or a log-processing tool when log volume is high. Do not scan sensitive log content indiscriminately.

### 10.2 Read a CSV and calculate a total

```python
import csv
from io import StringIO
from decimal import Decimal

csv_text = "product,price,quantity\nKeyboard,25.50,2\nMouse,10.00,3\n"
total = Decimal("0.00")

with StringIO(csv_text, newline="") as file:
    for row in csv.DictReader(file):
        price = Decimal(row["price"])
        quantity = int(row["quantity"])
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity must be non-negative")
        total += price * quantity

print(total)
```

Output:

```text
81.00
```

For money, `Decimal` helps avoid binary floating-point rounding surprises. Validate malformed rows and define how a batch should behave when one row is invalid.

### 10.3 Generate a report file

```python
from pathlib import Path

report = [
    "Daily Report",
    "============",
    "Processed records: 125",
    "Failed records: 3",
]

Path("daily-report.txt").write_text(
    "\n".join(report) + "\n",
    encoding="utf-8",
)
print("Report generated")
```

Output:

```text
Report generated
```

Reports should include timestamps, clear units, and a known output location. For important reports, write to a temporary file and replace the destination after successful generation.

### 10.4 Process a large text file in chunks

```python
from pathlib import Path

path = Path("large-input.txt")
path.write_text(("record line\n" * 5), encoding="utf-8")

line_count = 0
with path.open("r", encoding="utf-8") as file:
    for line in file:
        line_count += 1

print(line_count)
```

Output:

```text
5
```

This pattern scales better than `read_text().splitlines()` for very large files because it avoids holding all lines in memory simultaneously.

### 10.5 Combine multiple text files

```python
from pathlib import Path

input_files = [Path("part1.txt"), Path("part2.txt")]
output_path = Path("combined.txt")

input_files[0].write_text("First section\n", encoding="utf-8")
input_files[1].write_text("Second section\n", encoding="utf-8")

with output_path.open("w", encoding="utf-8") as output:
    for input_path in input_files:
        with input_path.open("r", encoding="utf-8") as source:
            for line in source:
                output.write(line)

print(output_path.read_text(encoding="utf-8"), end="")
```

Output:

```text
First section
Second section
```

For a real merge job, define ordering, duplicate handling, encoding expectations, error recovery, and whether a partially generated output is acceptable.

### 10.6 Check for duplicate lines

```python
from io import StringIO

file = StringIO("alpha\nbeta\nalpha\ngamma\nbeta\n")
seen = set()
duplicates = set()

for line in file:
    value = line.strip()
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)

print(sorted(duplicates))
```

Output:

```text
['alpha', 'beta']
```

The `seen` set gives efficient average membership checks. For very large inputs, the set itself may consume significant memory; consider external sorting or a database when needed.

---

## 11. Backend File Handling Use Cases

### 11.1 Upload validation pipeline

A backend upload workflow often needs to:
1. Enforce request and file-size limits while receiving data.
2. Validate file type using content and an allowlist, not only the user-provided extension.
3. Generate a server-controlled filename.
4. Store files outside executable/public directories when appropriate.
5. Scan files if required by the threat model.
6. Store metadata in a database.
7. Enforce authorization for download.
8. Clean up temporary files and handle failures.

**Do not trust client filenames or MIME types.** Treat uploads as untrusted input.

### 11.2 Safe filename generation

```python
from uuid import uuid4
from pathlib import Path

original_name = "quarterly-report.csv"
extension = Path(original_name).suffix.lower()
allowed_extensions = {".csv", ".json", ".txt"}

if extension not in allowed_extensions:
    raise ValueError("Unsupported extension")

stored_name = f"{uuid4().hex}{extension}"
print(stored_name.endswith(extension))
```

Output:

```text
True
```

This only demonstrates server-generated naming and an extension allowlist. Extension checks alone do not establish that file contents are safe or valid.

### 11.3 Avoid path traversal

A malicious filename such as `../../secrets.txt` must not be allowed to select arbitrary paths.

Prefer generating a server-controlled filename. If you must resolve a user-selected relative path, resolve it against a trusted base directory and verify that the result remains inside that base. Do not rely on string-prefix checks alone.

```python
from pathlib import Path

base_dir = Path("uploads").resolve()
base_dir.mkdir(parents=True, exist_ok=True)

# In production, prefer a server-generated filename instead.
candidate = (base_dir / "report.txt").resolve()

if candidate.is_relative_to(base_dir):
    print("Path is inside upload directory")
else:
    raise ValueError("Path escapes upload directory")
```

Output:

```text
Path is inside upload directory
```

`Path.is_relative_to()` is available in modern Python versions. This check is a demonstration; symlinks, races, and platform-specific filesystem behavior require careful consideration for hostile environments.

### 11.4 Import records from CSV

```python
import csv
from io import StringIO

csv_data = "id,email\n1,asha@example.com\n2,\n3,ravi@example.com\n"
valid = []
rejected = []

with StringIO(csv_data, newline="") as file:
    for row_number, row in enumerate(csv.DictReader(file), start=2):
        record_id = row.get("id", "").strip()
        email = row.get("email", "").strip().lower()

        if record_id and "@" in email:
            valid.append({"id": record_id, "email": email})
        else:
            rejected.append({"row": row_number, "reason": "Missing ID or invalid email"})

print("Valid:", len(valid))
print("Rejected:", rejected)
```

Output:

```text
Valid: 2
Rejected: [{'row': 3, 'reason': 'Missing ID or invalid email'}]
```

A production import should define transaction boundaries, idempotency, duplicate handling, row-level error reporting, and limits on rows and file size.

### 11.5 Write an audit event

```python
import json
from datetime import datetime, timezone
from pathlib import Path

event = {
    "event": "report_generated",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "record_count": 125,
}

with Path("audit.jsonl").open("a", encoding="utf-8") as file:
    file.write(json.dumps(event) + "\n")

print("Audit event appended")
```

Output:

```text
Audit event appended
```

JSON Lines (one JSON object per line) is convenient for append-oriented event files. For multi-process or high-throughput production auditing, use a proper logging or event-storage system with defined durability and concurrency behavior. Never put secrets into audit events.

### 11.6 Stream a file response

Web frameworks often support streaming file responses so large downloads do not need to be loaded fully into memory. The exact API differs by framework. A robust implementation should authorize access, set safe content headers, handle missing files, and avoid exposing arbitrary filesystem paths.

### 11.7 Configuration files

Use JSON, TOML, or another explicit format for configuration rather than trying to parse arbitrary text with ad hoc string operations. Validate required keys and types at application startup, and avoid storing credentials in source-controlled configuration files.

### 11.8 Background file-processing jobs

For long-running imports or report generation:
- Store a job ID and status.
- Process records in bounded batches.
- Record progress and failures.
- Make retries idempotent.
- Use temporary outputs and publish only completed results.
- Clean up abandoned temporary files.
- Limit concurrency to protect CPU, memory, disk, and downstream services.

---

## 12. Python Operators and Operations

An **operator** performs an operation on one or more operands. Operators appear throughout file handling—for example, combining paths, checking file sizes, validating metadata, and choosing retry conditions.

### 12.1 Arithmetic operators

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

`//` rounds down toward negative infinity. For example, `-7 // 3 == -3`.

### 12.2 Comparison operators

```python
size_bytes = 4096
max_bytes = 8192

print(size_bytes == 4096)
print(size_bytes != max_bytes)
print(size_bytes < max_bytes)
print(size_bytes >= 1024)
```

Output:

```text
True
True
True
True
```

Operators: `==`, `!=`, `<`, `<=`, `>`, `>=`. They typically return Boolean results.

### 12.3 Assignment operators

```python
processed = 10
processed += 5
processed -= 2
processed *= 2
print(processed)
```

Output:

```text
26
```

Common augmented assignment operators include `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, and `**=`.

### 12.4 Logical operators

```python
file_exists = True
size_is_valid = True
extension_is_allowed = False

print(file_exists and size_is_valid)
print(file_exists or extension_is_allowed)
print(not file_exists)
```

Output:

```text
True
True
False
```

`and` and `or` short-circuit and can return one of their operands, not necessarily a Boolean. Use parentheses for clarity when combining complex conditions.

### 12.5 Membership operators

```python
allowed_extensions = {".csv", ".json", ".txt"}
extension = ".csv"

print(extension in allowed_extensions)
print(".exe" not in allowed_extensions)
```

Output:

```text
True
True
```

Sets are often suitable for repeated membership checks. For dictionaries, `key in dictionary` checks keys by default.

### 12.6 Identity operators

```python
error = None
print(error is None)
print(error is not None)
```

Output:

```text
True
False
```

Use `is None` to check for `None`. Use `==` for ordinary value comparisons; do not use `is` to compare normal strings or integers by value.

### 12.7 Bitwise operators

| Operator | Meaning |
|---|---|
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `~` | Bitwise inversion |
| `<<` | Left shift |
| `>>` | Right shift |

```python
a = 6  # Binary 110
b = 3  # Binary 011

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

Bitwise operations are used for flags and low-level protocols; they are distinct from logical `and` and `or`.

### 12.8 Conditional expression

```python
file_size = 900
limit = 1000
status = "accepted" if file_size <= limit else "too large"
print(status)
```

Output:

```text
accepted
```

Keep conditional expressions short. Use a regular `if` statement when the logic is complex.

### 12.9 Operator precedence

```python
result = 2 + 3 * 4
print(result)

result = (2 + 3) * 4
print(result)
```

Output:

```text
14
20
```

When precedence is not obvious, use parentheses to make intent explicit.

### 12.10 Operations that commonly appear in file workflows

```python
from pathlib import Path

path = Path("reports") / "summary.csv"
max_size = 5 * 1024 * 1024  # 5 MiB
suffix = path.suffix.lower()

print(path.name)
print(suffix in {".csv", ".json"})
print(max_size)
```

Output:

```text
summary.csv
True
5242880
```

Important details:
- `/` between `Path` objects joins path components; `/` between numbers performs division.
- `+` joins strings but does not automatically convert numbers to strings.
- `in` checks whether an extension is in the allowlist.
- Comparisons can validate size limits, but validate actual input at the correct point in the processing pipeline.

### 12.11 Floating-point precision

```python
print(0.1 + 0.2)
```

Typical output:

```text
0.30000000000000004
```

Binary floating-point cannot represent every decimal exactly. Use `Decimal` for financial values, and use tolerance-based comparisons such as `math.isclose()` when appropriate.

### 12.12 Truthiness and fallback behavior

```python
filename = ""
chosen_name = filename or "upload.bin"
print(chosen_name)
```

Output:

```text
upload.bin
```

`or` chooses the first truthy operand. This fallback also triggers for values such as `0`, `False`, empty lists, and `None`. If only `None` should trigger a fallback, use an explicit `is None` check.

---

## 13. Debugging and Common Mistakes

### 13.1 `FileNotFoundError`

**Possible causes:**
- The working directory is not what you expected.
- The path is misspelled.
- A parent directory does not exist.
- The file was moved or deleted.

**Debugging steps:**

```python
from pathlib import Path

print("Working directory:", Path.cwd())
print("Resolved path:", Path("data/input.csv").resolve())
print("Exists:", Path("data/input.csv").exists())
```

Remember that checking `exists()` before opening is not a guarantee that the file will still exist when the operation occurs.

### 13.2 Data appears missing after writing

Common causes:
- The file was opened in `"w"` mode and truncated.
- Data was written to a different relative path.
- The write was not completed because of an exception.
- The content was not flushed before another process attempted to read it.

Use a known path, `with`, appropriate error handling, and tests that read back the generated file.

### 13.3 `UnicodeDecodeError`

The file bytes do not match the chosen text encoding. Confirm the source encoding; do not blindly switch encodings or ignore errors if doing so could silently corrupt data.

### 13.4 `PermissionError`

The process may not have access to the file or directory, or another program may have a lock on it. Check the path, user permissions, deployment container permissions, and platform-specific locking behavior.

### 13.5 Accidental data loss

Opening a file with `"w"` truncates it. For important outputs:
- Write to a temporary file.
- Validate successful output.
- Replace the destination only when ready.
- Keep backups or use versioned/object storage if required.
- Use a database transaction for transactional records.

### 13.6 Reading a huge file into memory

Avoid this for very large files:

```python
# Potentially memory-heavy:
# content = Path("huge.log").read_text(encoding="utf-8")
# lines = content.splitlines()
```

Prefer streaming:

```python
with open("huge.log", "r", encoding="utf-8") as file:
    for line in file:
        process_line = line.strip()
        # Process one line at a time.
```

Replace the comment with your actual processing logic. If a single line itself can be enormous, line-based iteration may still use substantial memory.

### 13.7 File handle leaks

Opening files repeatedly without closing them can exhaust file descriptors. Use `with open(...)` or `Path.open()` in a context manager.

### 13.8 Debugging checklist

1. Print or inspect `Path.cwd()` and the resolved path.
2. Confirm file mode (`r`, `w`, `a`, `x`, `rb`, `wb`).
3. Confirm encoding and whether the data is text or binary.
4. Check permissions and available disk space.
5. Inspect the full traceback and the original exception.
6. Test empty files, missing files, malformed content, and large inputs.
7. Avoid exposing internal paths, secrets, or raw tracebacks to API clients.
8. Test failure behavior, not only the successful path.

---

## 14. Security, Reliability, and Performance

### 14.1 Treat files as untrusted input

- Enforce upload limits before and during ingestion.
- Validate content and schema, not just filename extensions.
- Use server-generated filenames.
- Prevent path traversal and unauthorized downloads.
- Do not deserialize untrusted data with `pickle`.
- Do not execute uploaded scripts or macros.
- Avoid logging sensitive content.

### 14.2 Avoid unsafe path handling

Do not directly concatenate user input into filesystem paths. Use a trusted storage root and server-generated names. Consider symbolic links, race conditions, filesystem permissions, and container boundaries.

### 14.3 Stream large files

Prefer iteration, chunked reads, or framework-supported streaming instead of loading the entire file into memory. Choose a chunk size based on workload and measure performance.

### 14.4 Use the right storage system

Files are useful for reports, uploads, and interchange. A relational database is generally more appropriate for transactional records that require querying, constraints, concurrent updates, and consistency. Object storage may be a better fit for large user uploads.

### 14.5 Avoid concurrent-write corruption

Multiple processes writing the same file can interleave or overwrite data depending on the operation and platform. Consider:
- A single writer process.
- A logging framework with appropriate concurrency support.
- File locks where suitable.
- Separate per-job output files.
- A database or message queue for concurrent workloads.

### 14.6 Keep operations observable

For a production file job, capture:
- Job or correlation ID.
- Input file identifier, not sensitive content.
- Number of records processed, accepted, and rejected.
- Duration and output location.
- Error category and retry count.
- Final status.

Use structured logs and metrics. Avoid storing credentials or unnecessary personal information in logs.

### 14.7 Testing file-handling code

Test:
- A valid small file.
- A missing file.
- An empty file.
- Invalid encoding or malformed JSON/CSV.
- Permission or write failures where testable.
- Maximum allowed file size.
- Unexpected extra columns or missing required fields.
- Cleanup after an exception.

Use temporary directories in automated tests to prevent test files from polluting the project. Python's `tempfile` module is useful for this purpose.

---

## 15. Practice Exercises

### Beginner

1. Create a text file and write three lines to it.
2. Read the file using `read()`, `readline()`, and a `for` loop.
3. Append a timestamped line to a log file.
4. Count the lines in a text file without loading all lines into memory.
5. Print all `.txt` filenames in a directory using `pathlib`.
6. Explain the difference between `"w"` and `"a"` modes.
7. Read a UTF-8 file containing non-English text.

### Intermediate

8. Read a CSV of products and calculate the total stock value.
9. Write a list of dictionaries to a CSV file.
10. Load a JSON configuration and validate required keys.
11. Catch `FileNotFoundError` and `JSONDecodeError` separately.
12. Merge several text files in a predictable order.
13. Find duplicate lines in a file.
14. Generate a report using a temporary file and `os.replace()`.
15. Count `ERROR`, `WARNING`, and `INFO` entries in a log file.
16. Use `tempfile` to write and test a file without leaving artifacts.

### Backend / advanced

17. Design a CSV import process that records row-level validation failures.
18. Create an upload pipeline with a size limit and server-generated filenames.
19. Explain and mitigate path traversal in an upload endpoint.
20. Process a large file using bounded memory.
21. Implement safe cleanup for a failed file-processing job.
22. Design an idempotent background report-generation workflow.
23. Explain how concurrent writers could corrupt a shared log file.
24. Write unit tests for missing files, invalid JSON, and permission errors.
25. Use `Decimal` to calculate totals from a CSV file containing money values.
26. Design a download endpoint that checks authorization and streams the file.

---

## 16. Interview Questions

1. What is file handling in Python?
2. What is the difference between text mode and binary mode?
3. Explain `r`, `w`, `a`, `x`, `b`, and `+` modes.
4. Why is `with open(...)` recommended?
5. What is the difference between `read()`, `readline()`, and `readlines()`?
6. Why is iterating over a file usually better for large files?
7. What does `writelines()` do, and does it add newlines?
8. What is the difference between `flush()` and `close()`?
9. How does `pathlib` improve path handling?
10. How would you debug `FileNotFoundError`?
11. What causes `UnicodeDecodeError`?
12. How should a backend validate an uploaded file?
13. Why should you not trust a client-supplied filename?
14. What is path traversal and how can it be mitigated?
15. Why is `pickle` unsafe for untrusted data?
16. How do `csv.DictReader` and `csv.DictWriter` work?
17. What is the difference between `json.load()` and `json.loads()`?
18. How can you prevent partial output files from being published?
19. How would you process a multi-gigabyte file?
20. What can happen when multiple processes write to the same file?
21. What is the difference between `/` and `//`?
22. What is the difference between `==` and `is`?
23. Explain short-circuit behavior in `and` and `or`.
24. Why can `0.1 + 0.2` be different from `0.3`?
25. When should data be stored in a database rather than a file?

---

## 17. Quick Revision

### File handling

- `open(path, mode, encoding="utf-8")`: open a text file.
- `with`: automatically closes the file resource.
- `read()`: read the remaining content.
- `readline()`: read one line.
- `readlines()`: return all remaining lines as a list.
- `write()`: write a string.
- `writelines()`: write supplied strings without adding line breaks.
- `"r"`: read; `"w"`: truncate/write; `"a"`: append; `"x"`: exclusive create.
- `"rb"` / `"wb"`: binary read/write.
- `pathlib.Path`: build and inspect paths.
- `csv`: parse and write CSV correctly.
- `json`: parse and write JSON.
- `tempfile`: create temporary files and directories.
- Stream large files; do not read them all into memory unnecessarily.

### Operators

- Arithmetic: `+ - * / // % **`
- Comparison: `== != < <= > >=`
- Assignment: `= += -= *= ...`
- Logical: `and or not`
- Membership: `in`, `not in`
- Identity: `is`, `is not`
- Bitwise: `& | ^ ~ << >>`
- Use `is None` for `None` checks and `==` for value comparison.
- Use parentheses when operator precedence is unclear.

### Production reminders

- Validate file contents, size, and access permissions.
- Never trust user-supplied filenames.
- Avoid loading very large files into memory.
- Use context managers.
- Handle expected exceptions specifically.
- Protect sensitive information in logs.
- Design for retries, cleanup, concurrency, and partial failures.

---

## 18. Official Documentation

- Python Tutorial — Reading and Writing Files: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- Built-in `open()`: https://docs.python.org/3/library/functions.html#open
- `pathlib`: https://docs.python.org/3/library/pathlib.html
- `csv`: https://docs.python.org/3/library/csv.html
- `json`: https://docs.python.org/3/library/json.html
- `tempfile`: https://docs.python.org/3/library/tempfile.html
- `shutil`: https://docs.python.org/3/library/shutil.html
- `os`: https://docs.python.org/3/library/os.html
- Python Expressions and Operator Precedence: https://docs.python.org/3/reference/expressions.html
- `decimal`: https://docs.python.org/3/library/decimal.html
- `unittest`: https://docs.python.org/3/library/unittest.html

---

## Final Developer Advice

File handling is not just about calling `open()`. Production-quality file processing requires correct path resolution, explicit encoding, resource cleanup, input validation, predictable failure behavior, and protection against data loss and hostile inputs.

For every example:
1. Predict the output before running it.
2. Test the empty-file and missing-file cases.
3. Try malformed data and invalid paths.
4. Estimate memory use for large inputs.
5. Make sure files are closed and temporary artifacts are cleaned up.
6. Consider concurrency and whether a file is the right storage system for the job.
