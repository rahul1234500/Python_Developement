# NumPy Notes: Practical Numerical Computing
## A senior-developer-style guide for Python application development

> **Goal:** Learn how to create and manipulate arrays, perform fast numerical computations, analyze distributions, handle missing numerical values, and apply NumPy in a realistic Kaggle project.

---

## 1. What is NumPy?

NumPy (Numerical Python) is a core Python library for numerical computing. Its central structure is the **`ndarray`**, a multidimensional array that supports vectorized operations, broadcasting, mathematical functions, statistics, and linear algebra.

```python
import numpy as np

marks = np.array([70, 80, 90])
print(marks * 2)
```

Output:

```text
[140 160 180]
```

Unlike a Python list, multiplication of a NumPy numerical array by a scalar performs element-wise multiplication.

**Developer perspective:** NumPy is especially useful when data is numeric and has a regular shape. Pandas is generally more convenient for labeled tables with mixed data types; NumPy is ideal for numerical kernels and array-oriented calculations.

## 2. Setup

```bash
python -m pip install numpy pandas matplotlib
```

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print(np.__version__)
```

NumPy is usually imported as `np`.

## 3. Create arrays

```python
a = np.array([10, 20, 30, 40])
zeros = np.zeros(5)
ones = np.ones(4)
steps = np.arange(0, 10, 2)
even_points = np.linspace(0, 1, 5)
filled = np.full((2, 3), 7)
identity = np.eye(3)
```

| Function | Use case |
|---|---|
| `np.array()` | Convert a sequence to an array |
| `np.zeros()` | Initialize zero-filled storage |
| `np.ones()` | Initialize one-filled storage |
| `np.arange()` | Generate values using a step size |
| `np.linspace()` | Generate a fixed number of evenly spaced values |
| `np.full()` | Fill a shape with a constant |
| `np.eye()` | Create an identity matrix |

Use `linspace()` when the number of points matters. Use `arange()` when a step size matters. Floating-point steps in `arange()` can produce surprising endpoints due to floating-point precision.

## 4. Dimensions, shape, size, and dtype

```python
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
])

print(scores.ndim)   # Number of dimensions
print(scores.shape)  # (2, 3)
print(scores.size)   # 6
print(scores.dtype)  # Integer dtype
```

- **`ndim`**: number of axes.
- **`shape`**: size along each axis.
- **`size`**: total element count.
- **`dtype`**: element data type.

Shape reasoning is essential. If a function expects `(n_samples, n_features)` but receives `(n_features, n_samples)`, calculations can be wrong or fail.

## 5. Indexing and slicing

```python
print(scores[0, 1])   # First row, second column
print(scores[1, 2])   # Second row, third column
print(scores[:, 0])   # First column
print(scores[0, :])   # First row
```

The colon `:` selects all entries along an axis.

Basic slicing usually creates a **view** rather than an independent copy. Mutating the slice may mutate the original array.

```python
a = np.array([10, 20, 30, 40])
view = a[1:3]
view[0] = 999
print(a)  # Original array is changed
```

Use `.copy()` when you need independent storage:

```python
copy = a[1:3].copy()
```

## 6. Vectorization

Vectorization expresses operations over whole arrays instead of explicit Python loops.

```python
marks = np.array([70, 80, 90])
updated_marks = marks + 5
```

This is concise and often faster for large numerical workloads because NumPy performs operations in optimized compiled code. Benchmark critical code rather than assuming every vectorized expression is always faster.

Common vectorized operations:

```python
a + b
a - b
a * b
a / b
a ** 2
a > 50
```

With numerical arrays, `*` means element-wise multiplication. Use `@` or `np.matmul()` for matrix multiplication.

## 7. Broadcasting

Broadcasting lets NumPy operate on arrays of compatible shapes without explicitly copying a small array across a larger one.

```python
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
])

subject_bonus = np.array([5, 0, 3])

print(scores + subject_bonus)
```

Output:

```text
[[75 80 93]
 [65 75 88]]
```

The shapes are `(2, 3)` and `(3,)`. Starting from the right, dimensions are compatible because the final dimension matches and the smaller shape can be extended across the leading dimension.

**Rule:** Compare shapes from the right. Each dimension must be equal or one of them must be `1`; missing leading dimensions are treated as `1`.

When you get a broadcasting error, print both `.shape` values before changing the data.

## 8. Aggregation and axis

```python
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 100],
])

print(np.sum(scores))
print(np.mean(scores, axis=0))  # Average for each column
print(np.mean(scores, axis=1))  # Average for each row
print(np.min(scores))
print(np.max(scores))
```

For a 2D array:

- `axis=0` reduces rows, leaving one result per column.
- `axis=1` reduces columns, leaving one result per row.
- `axis=None` (the default for many aggregations) reduces across all elements.

Before using `axis`, identify what each dimension represents. For example, if rows are students and columns are subjects, `axis=0` calculates per-subject results.

## 9. Universal functions and mathematical operations

NumPy provides vectorized mathematical functions, often called **ufuncs**.

```python
values = np.array([1.0, 4.0, 9.0, 16.0])

print(np.sqrt(values))
print(np.log(values))
print(np.exp(values))
print(np.round(values / 3, 2))
```

Other useful functions include `np.abs()`, `np.maximum()`, `np.minimum()`, `np.clip()`, and `np.where()`.

```python
bounded = np.clip(values, 2, 10)
```

`clip()` restricts values to a specified range. Apply it only when the range has a defensible analytical or business meaning; it is not a generic fix for outliers.

## 10. Statistics and distributions

```python
marks = np.array([55, 60, 65, 70, 75, 80, 95])

print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))
print(np.var(marks))
print(np.percentile(marks, [25, 50, 75, 90]))
```

- Mean: arithmetic average.
- Median: middle value after sorting.
- Standard deviation: spread around the mean.
- Variance: squared spread measure.
- Percentiles: thresholds below which a specified proportion of observations falls.

By default, `np.std()` uses `ddof=0` (population standard deviation). Use `ddof=1` for a sample standard deviation when that statistical interpretation is appropriate.

Extreme observations can strongly affect mean and standard deviation. Use medians, percentiles, visualizations, and domain context when investigating skewed data.

## 11. Boolean masks and conditional selection

```python
marks = np.array([45, 60, 72, 88, 95])

passed_mask = marks >= 60
passed_marks = marks[passed_mask]

selected = marks[(marks >= 60) & (marks <= 85)]
```

Use `&` and `|` for element-wise logical operations and wrap each condition in parentheses. Python's `and` and `or` are not suitable for array masks.

Conditional assignment:

```python
status = np.where(marks >= 60, "Pass", "Fail")
```

Multiple conditions:

```python
conditions = [marks >= 85, marks >= 60]
choices = ["Excellent", "Pass"]

status = np.select(
    conditions,
    choices,
    default="Needs Improvement",
)
```

Conditions in `np.select()` are evaluated in order, so put the most specific or highest-priority condition first.

## 12. Sorting, uniqueness, and counts

```python
values = np.array([4, 2, 4, 1, 2, 9])

print(np.sort(values))
print(np.unique(values))
print(np.unique(values, return_counts=True))
```

Use `np.unique(..., return_counts=True)` to count occurrences of each distinct value. For grouped counts on mixed categorical tabular data, pandas `value_counts()` may be easier to read.

`np.argsort()` returns the indices that would sort an array:

```python
indices = np.argsort(values)
sorted_values = values[indices]
```

## 13. Missing numerical values

Floating-point arrays can represent missing or undefined values with `np.nan`.

```python
values = np.array([10.0, 20.0, np.nan, 40.0])

print(np.isnan(values))
print(np.mean(values))     # NaN
print(np.nanmean(values))  # Ignores NaN
```

Other useful functions include `np.nanmedian()`, `np.nanstd()`, and `np.nanpercentile()`.

Use `np.isfinite()` to filter both NaN and positive/negative infinity:

```python
valid_values = values[np.isfinite(values)]
```

Do not replace missing values with zero without a justified reason. Zero is a real numerical value and can change the result.

For integer arrays, strings, or structured data, missing-value representation needs more care. Pandas nullable dtypes or masked arrays may be more suitable.

## 14. Random numbers and reproducibility

Prefer the modern random generator API:

```python
rng = np.random.default_rng(42)

sample = rng.choice(
    np.array([55, 60, 65, 70, 75, 80, 95]),
    size=4,
    replace=False,
)

random_values = rng.normal(loc=0, scale=1, size=100)
```

A fixed seed helps make experiments reproducible. Reproducibility also requires controlling input data, library versions, and other sources of randomness.

Use sampling for exploratory analysis, simulations, and experimental workflows. Ensure the sampling design is appropriate before drawing population-level conclusions.

## 15. Reshape and transpose

```python
a = np.arange(12)

matrix = a.reshape(3, 4)
transposed = matrix.T

print(matrix.shape)      # (3, 4)
print(transposed.shape)  # (4, 3)
```

`reshape()` changes the array's shape without changing its element count. A reshape may return a view or a copy depending on memory layout.

Use `ravel()` when a flattened view is possible and `flatten()` when you explicitly need a copy.

## 16. Linear algebra

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(A @ B)             # Matrix multiplication
print(A.T)               # Transpose
print(np.linalg.det(A))  # Determinant
```

For solving a linear system `Ax = b`, prefer:

```python
x = np.linalg.solve(A, b)
```

rather than explicitly computing `np.linalg.inv(A) @ b`. Solving directly is generally more numerically appropriate and efficient.

Use linear algebra operations for scientific computing, regression-related calculations, transformations, and machine-learning foundations. Check shapes and numerical conditioning when results seem unstable.

## 17. NumPy with pandas: realistic Kaggle workflow

Suggested dataset: **Student Performance Factors**. Find it on Kaggle, add it to a notebook, and inspect the actual filename and schema. Use pandas for mixed tabular data and NumPy for numerical calculations.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance.csv")

print(df.shape)
print(df.dtypes)
display(df.head())
print(df.isna().sum())
```

The exact filename and columns depend on the dataset version you download.

### Extract numerical data

```python
numeric_df = df.select_dtypes(include="number")
X = numeric_df.to_numpy(dtype=np.float64)

print(X.shape)
print(X.ndim)
print(X.dtype)
```

Converting to `float64` can increase memory usage. Use a dtype appropriate to the precision and range you need.

### Analyze exam scores

```python
scores = df["Exam_Score"].to_numpy(dtype=np.float64)
valid_scores = scores[np.isfinite(scores)]

print("Mean:", np.mean(valid_scores))
print("Median:", np.median(valid_scores))
print("Standard deviation:", np.std(valid_scores))
print("Percentiles:", np.percentile(valid_scores, [25, 50, 90]))
```

Verify the column's meaning, units, and valid range before interpreting these statistics.

### Compare study time and scores

```python
study_hours = df["Hours_Studied"].to_numpy(dtype=np.float64)
exam_scores = df["Exam_Score"].to_numpy(dtype=np.float64)

valid = np.isfinite(study_hours) & np.isfinite(exam_scores)

study_hours = study_hours[valid]
exam_scores = exam_scores[valid]

correlation = np.corrcoef(study_hours, exam_scores)[0, 1]
print("Correlation:", correlation)
```

Correlation measures linear association, not causation. It may also be undefined if either variable has zero variance.

### Visualize

```python
plt.scatter(study_hours, exam_scores, alpha=0.5)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()
```

Write down what the chart suggests, how strong the relationship appears, and what it cannot prove.

## 18. NumPy debugging guide

### Shape mismatch or broadcasting error

```python
print(a.shape)
print(b.shape)
```

Check the dimensions from right to left. Use `reshape()` only when the intended meaning of each dimension is clear.

### Unexpected result from `axis`

Print the input shape and write down what each axis represents. Test the operation on a tiny array where you can calculate the expected result manually.

### NaN propagates through calculations

```python
print(np.isnan(values))
print(np.isfinite(values))
```

Decide whether to investigate, filter, or use a NaN-aware aggregation. Do not treat all non-finite values as ordinary missing data without checking their source.

### Integer truncation or overflow

```python
a = np.array([1, 2, 3], dtype=np.int64)
```

Inspect `dtype` when results look wrong. Integer division, conversion to integer types, and arithmetic on fixed-width integers can produce unexpected results or overflow for sufficiently large values.

### Original array changes unexpectedly

Basic slices often create views:

```python
subset = a[1:4].copy()
```

Use `.copy()` when independent data is required.

### Floating-point equality

Binary floating-point cannot represent every decimal exactly. For numerical comparisons, consider:

```python
np.isclose(0.1 + 0.2, 0.3)
```

Choose tolerances appropriate to the scale and meaning of your problem.

### Slow computation

- Prefer array operations over Python loops where appropriate.
- Avoid unnecessary copies of large arrays.
- Choose suitable dtypes.
- Profile before optimizing.
- For datasets too large for memory, process chunks or use an appropriate out-of-core/distributed tool.

## 19. Capstone project checklist

For the student performance dataset:

- [ ] Load and inspect the dataset.
- [ ] Check types, missing values, and invalid numerical values.
- [ ] Calculate exam-score statistics and percentiles.
- [ ] Filter students using boolean masks.
- [ ] Compare study time, attendance, sleep, and scores where fields exist.
- [ ] Calculate correlations and discuss their limitations.
- [ ] Investigate possible outliers using a documented rule.
- [ ] Produce a histogram and scatter plot.
- [ ] Write three evidence-based findings.
- [ ] Document assumptions and make the notebook reproducible.

## 20. Learning progression

| Stage | Demonstrate |
|---|---|
| Beginner | Array creation, indexing, slicing, shapes, and dtypes |
| Intermediate | Vectorization, broadcasting, aggregation, masks, and statistics |
| Advanced | Views/copies, random generators, linear algebra, and numerical stability |
| Portfolio | A reproducible Kaggle analysis with charts and written conclusions |

**Core habit:** Before performing an array operation, predict the output shape, identify the meaning of each axis, and consider how missing values and dtype affect the result. This habit prevents many subtle numerical bugs.
