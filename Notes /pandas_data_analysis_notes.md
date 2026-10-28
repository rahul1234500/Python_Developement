# Pandas Notes: Practical Data Analysis
## A senior-developer-style guide for Python application development

> **Goal:** Learn to inspect, clean, transform, analyze, validate, and communicate findings from tabular data using pandas. These notes combine core concepts, practical examples, common use cases, and debugging habits.

---

## 1. What is pandas?

Pandas is a Python library for working with labeled, tabular data. Its two core data structures are:

- **`Series`**: a one-dimensional labeled collection.
- **`DataFrame`**: a two-dimensional table with labeled rows and columns.

Use pandas when data has columns such as customer, date, product, region, quantity, or revenue. Typical sources include CSV files, Excel workbooks, SQL queries, and API responses.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Quantity": [2, 5, 3],
    "Price": [50000, 500, 1500],
})

df["Revenue"] = df["Quantity"] * df["Price"]
print(df)
```

**Developer perspective:** Start by defining what each row represents. A row might be an order, an order item, a customer, or a daily summary. Many analysis bugs come from misunderstanding the row-level grain.

## 2. Setup

```bash
python -m pip install pandas numpy matplotlib seaborn jupyterlab
jupyter lab
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)
```

For a project, consider recording dependencies in `requirements.txt` or a managed environment file so another developer can reproduce your results.

## 3. Load data and inspect it before changing anything

```python
df = pd.read_csv("sales.csv")

print(df.shape)          # (row_count, column_count)
print(df.columns.tolist())
print(df.dtypes)
df.info()
display(df.head())
display(df.sample(min(5, len(df)), random_state=42))
display(df.describe(include="all").T)
```

Useful inspection methods:

| Method | Why use it |
|---|---|
| `head()` / `tail()` | Check example records and file boundaries |
| `shape` | Confirm row and column counts |
| `columns` | Inspect the schema |
| `dtypes` / `info()` | Detect incorrect types and missing values |
| `describe()` | Understand numerical ranges and category frequencies |
| `isna().sum()` | Count missing values |
| `nunique()` | Count distinct values |
| `value_counts()` | Inspect category frequencies |
| `duplicated().sum()` | Count exact duplicate rows |

```python
print(df.isna().sum().sort_values(ascending=False))
print("Exact duplicate rows:", df.duplicated().sum())
```

**Debugging habit:** Never assume that a file was loaded correctly just because `read_csv()` did not raise an exception. Check the dimensions, column names, types, and sample values.

## 4. Select, filter, and sort

### Select columns

```python
df["Product"]                       # Series
df[["Product", "Revenue"]]          # DataFrame
```

### Select rows: `` and `iloc`

- `loc` selects using index labels.
- `iloc` selects using integer positions.

```python
df.loc[0, "Product"]
df.iloc[0, 0]
df.iloc[:3]
```

After filtering or sorting, index labels may not be consecutive. Do not confuse a label with a row's current position.

### Boolean filtering

```python
expensive = df.loc[df["Price"] >= 1500]

filtered = df.loc[
    (df["Price"] >= 1000) &
    (df["Quantity"] >= 2)
]

selected_products = df[df["Product"].isin(["Laptop", "Mouse"])]
price_range = df[df["Price"].between(500, 2000)]
```

Use parentheses around each condition when combining masks with `&` or `|`. Python's `and` and `or` are not the correct operators for element-wise pandas conditions.

For text searches where values may be missing:

```python
matches = df[
    df["Product"].str.contains("key", case=False, na=False)
]
```

### Sort and rank

```python
df.sort_values("Revenue", ascending=False)
df.nlargest(2, "Revenue")

df["Revenue_Rank"] = df["Revenue"].rank(
    ascending=False,
    method="dense",
)
```

Most pandas operations return a new object unless the method explicitly modifies data. Assign the result when you want to keep it.

## 5. Create and transform columns

```python
df["Revenue"] = df["Quantity"] * df["Price"]
df["Discounted_Revenue"] = df["Revenue"] * 0.90
```

Useful approaches:

- Arithmetic operations: simple numeric transformations.
- `np.where()`: two-way conditional assignment.
- `np.select()`: multiple ordered conditions.
- `map()`: map values through a dictionary or Series.
- `apply()`: custom function application when a vectorized approach is not practical.

```python
df["Price_Band"] = np.where(
    df["Price"] >= 1000,
    "High",
    "Low",
)

department_codes = {"IT": "D01", "HR": "D02"}
employees["Department_Code"] = employees["Department"].map(
    department_codes
)
```

`map()` produces missing values for keys not found in the mapping. Check unmatched categories instead of assuming the mapping was complete.

**Performance tip:** Prefer built-in vectorized operations over `DataFrame.apply(axis=1)` or explicit Python loops for ordinary arithmetic. Benchmark when performance matters; not every vectorized expression is automatically faster.

## 6. Missing values: investigate before filling

```python
df.isna().sum()
(df.isna().mean() * 100).round(2)  # percentage missing
```

Possible strategies depend on the meaning of the field:

- Keep missing values when “unknown” is meaningful.
- Use a median for a skewed numerical variable when justified.
- Use a mean for a reasonably symmetric numerical variable when justified.
- Use an explicit category such as `"Unknown"` for a categorical field if that meaning is valid.
- Investigate missing critical identifiers instead of inventing values.
- Drop rows only when the loss is acceptable and the decision is documented.

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
df["City"] = df["City"].fillna("Unknown")
```

Be careful: filling missing data can change distributions and conclusions. For supervised machine learning, calculate imputation values on the training data only, then apply them to validation/test data to avoid data leakage.

Pandas aggregations often skip missing values by default. For example, `sum()` usually skips `NaN`; this can produce a partial total. Report data completeness when that distinction matters.

## 7. Duplicates, types, and text normalization

### Duplicates

```python
df.duplicated().sum()
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["Order_ID"])
```

Only remove duplicates after defining what constitutes a duplicate. Two valid orders can share the same customer and amount. Business keys are often more useful than comparing every column.

### Convert types

```python
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
```

`errors="coerce"` converts invalid values to missing values. Count and investigate those newly missing values so that invalid input is not silently hidden.

Identifiers that are not used in arithmetic are often better represented as strings, especially when leading zeros matter.

### Standardize names and categories

```python
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

df["City"] = (
    df["City"].astype("string")
    .str.strip()
    .str.title()
)
```

Normalization can merge values such as `" pune "` and `"Pune"`. Do not blindly apply title case to product codes, acronyms, or identifiers.

## 8. String and date operations

String methods use `.str`:

```python
df["Product"] = df["Product"].str.strip().str.lower()
df["Product"].str.contains("mouse", na=False)
df["SKU"] = df["Description"].str.extract(r"(SKU-\d+)", expand=False)
```

Date/time methods use `.dt` after parsing:

```python
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Weekday"] = df["Order_Date"].dt.day_name()
```

Monthly aggregation:

```python
monthly = (
    df.set_index("Order_Date")["Revenue"]
    .resample("MS")
    .sum()
)
```

`MS` means month start. Before interpreting gaps, determine whether a missing month means zero activity or missing data.

## 9. Outlier investigation

An outlier is an unusually distant observation, not automatically an error. It might be a data-entry problem, a valid high-value transaction, or a rare event.

The IQR rule uses:

- `IQR = Q3 - Q1`
- Lower threshold: `Q1 - 1.5 * IQR`
- Upper threshold: `Q3 + 1.5 * IQR`

```python
q1 = df["Revenue"].quantile(0.25)
q3 = df["Revenue"].quantile(0.75)
iqr = q3 - q1

outliers = df.loc[
    (df["Revenue"] < q1 - 1.5 * iqr) |
    (df["Revenue"] > q3 + 1.5 * iqr)
]
```

Other approaches include z-scores, percentiles, box plots, and domain-specific rules. Check units, source records, and business constraints before excluding or capping anything.

## 10. GroupBy: split, apply, combine

Use `groupby()` to summarize data by dimensions such as region, product, or month.

```python
summary = df.groupby("Region").agg(
    Total_Revenue=("Revenue", "sum"),
    Average_Revenue=("Revenue", "mean"),
    Units_Sold=("Quantity", "sum"),
    Row_Count=("Revenue", "size"),
)
```

Group by multiple columns:

```python
df.groupby(["Region", "Product"])["Revenue"].sum()
```

`size()` counts rows, including rows where other columns are missing. `count()` counts non-missing values in the selected column.

### `agg()` versus `transform()`

Use `agg()` when you want one row per group:

```python
region_totals = df.groupby("Region")["Revenue"].sum()
```

Use `transform()` when the group statistic should be aligned with every original row:

```python
df["Region_Total"] = (
    df.groupby("Region")["Revenue"].transform("sum")
)
df["Region_Share"] = df["Revenue"] / df["Region_Total"]
```

## 11. Merge, join, and concatenate

Real analysis often requires several related tables.

```python
order_details = orders.merge(
    customers,
    on="Customer_ID",
    how="left",
    validate="many_to_one",
    indicator=True,
)
```

Join types:

- **Inner:** only matching keys.
- **Left:** every left-side row plus matching right-side data.
- **Right:** every right-side row plus matching left-side data.
- **Outer:** keys from both tables, including unmatched records.

`validate="many_to_one"` asserts that the right table has at most one row per key. This helps prevent unexpected row multiplication.

```python
unmatched = order_details.loc[order_details["_merge"] == "left_only"]
```

Use `merge()` for key-based relationships, `join()` primarily for index-based joins, and `concat()` to stack compatible tables.

```python
all_months = pd.concat([january, february], ignore_index=True)
```

**Debugging habit:** Compare row counts and key uniqueness before and after every merge. A many-to-many merge can inflate revenue and counts.

## 12. Pivot tables and reshaping

```python
pivot = df.pivot_table(
    index="Region",
    columns="Product",
    values="Revenue",
    aggfunc="sum",
    fill_value=0,
)
```

- `pivot()` reshapes data when each index/column combination uniquely identifies a value.
- `pivot_table()` supports aggregation when combinations have multiple records.
- `melt()` converts wide tables into long tables.

```python
long_df = wide_df.melt(
    id_vars=["Customer"],
    value_vars=["January", "February"],
    var_name="Month",
    value_name="Revenue",
)
```

Long format is often convenient for visualization and time-based analysis.

## 13. Statistics and visualization

```python
df["Revenue"].mean()
df["Revenue"].median()
df["Revenue"].std()
df["Revenue"].quantile([0.25, 0.50, 0.75])
```

Correlation:

```python
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
```

Correlation indicates association, not causation.

Choose charts based on the question:

- Bar chart: compare categories.
- Line chart: show a time trend.
- Histogram: inspect a distribution.
- Box plot: compare spread and potential outliers.
- Scatter plot: inspect relationships between two numerical variables.

```python
region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(
    ascending=False
)
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
```

A chart should support a specific question. Include units, labels, and a clear explanation of limitations.

## 14. Build a reusable cleaning function

```python
def clean_sales_data(raw_df: pd.DataFrame) -> pd.DataFrame:
    df = raw_df.copy()

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    for col in ["product", "region"]:
        if col in df.columns:
            df[col] = (
                df[col].astype("string")
                .str.strip()
                .str.title()
            )

    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(
            df["order_date"], errors="coerce"
        )

    if "revenue" in df.columns:
        df["revenue"] = pd.to_numeric(
            df["revenue"], errors="coerce"
        )

    return df.drop_duplicates()
```

Copying the input prevents accidental mutation of the caller's DataFrame. In production, also validate required columns, log rejected values, and document every business rule.

Assertions can encode invariants:

```python
assert df.columns.is_unique
```

Only assert that a column has no missing values if that is truly part of the data contract.

## 15. Realistic Kaggle workflow

Suggested dataset: **Student Performance Factors**. Search for it on Kaggle and inspect its current schema and usage terms before beginning.

Workflow:

1. Define a question, such as “How do study time and attendance relate to exam scores?”
2. Load the data and inspect shape, schema, and sample rows.
3. Audit missing values, duplicates, types, and category consistency.
4. Clean using documented rules.
5. Explore distributions and group summaries.
6. Analyze relationships and create charts.
7. Validate totals, assumptions, and edge cases.
8. Report findings, limitations, and possible next steps.
9. Save a reproducible notebook and README.

Example data loading:

```python
df = pd.read_csv("student_performance.csv")

print(df.shape)
print(df.dtypes)
display(df.head())
display(df.isna().sum())
```

The actual path and column names depend on the dataset version you download.

## 16. Capstone: E-commerce business intelligence

Suggested tables:

| Table | Example fields |
|---|---|
| Orders | Order ID, customer ID, date, status |
| Order items | Order ID, product ID, quantity, unit price |
| Customers | Customer ID, city, segment |
| Products | Product ID, category, product name |
| Payments | Order ID, payment method, amount paid |

Deliverables:

1. Audit data quality and key uniqueness.
2. Standardize types and categories.
3. Join tables and verify row counts.
4. Define revenue correctly, accounting for cancellations, discounts, and refunds when those fields exist.
5. Calculate monthly and category revenue.
6. Analyze customer spending and repeat purchases.
7. Investigate unusual values.
8. Build three meaningful charts.
9. Write findings and limitations.
10. Export clean outputs and document the workflow.

Example item-level calculation:

```python
items["Gross_Item_Amount"] = items["Quantity"] * items["Unit_Price"]

category_summary = items.groupby("Category").agg(
    Gross_Item_Amount=("Gross_Item_Amount", "sum"),
    Units_Sold=("Quantity", "sum"),
    Distinct_Orders=("Order_ID", "nunique"),
)
```

This is a gross item amount, not necessarily recognized revenue. Apply the business's accounting and order-status rules before labeling it revenue.

## 17. Common pandas errors and debugging tips

### `KeyError: 'Revenue'`

Likely cause: the column does not exist or has a different name.

```python
print(df.columns.tolist())
```

Check capitalization, whitespace, spelling, and whether the column was created.

### `AttributeError` involving `.str` or `.dt`

Likely cause: wrong data type or use of an accessor on an incompatible Series.

```python
print(df["Order_Date"].dtype)
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
```

For `.str`, inspect the column values and dtype first.

### Boolean filtering error

Use:

```python
df[(df["Price"] > 100) & (df["Quantity"] > 1)]
```

Do not use `and` between pandas Series conditions.

### `SettingWithCopyWarning` or chained assignment issues

Prefer explicit `.loc` assignment and create a copy when appropriate:

```python
subset = df.loc[df["Price"] > 100].copy()
subset.loc[:, "Price_Band"] = "High"
```

### Unexpected row multiplication after a merge

Check keys:

```python
print(customers["Customer_ID"].duplicated().sum())
```

Then select the correct join cardinality, resolve duplicate keys, or aggregate the right table before merging.

### Unexpected missing values after conversion

```python
before = df["Price"].isna().sum()
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
after = df["Price"].isna().sum()

print("Missing before:", before, "Missing after:", after)
```

Investigate malformed strings or currency symbols instead of silently accepting all conversion failures.

### Performance is slow

- Avoid repeated row-by-row Python loops for simple calculations.
- Select only the required columns.
- Use appropriate dtypes.
- Avoid repeatedly concatenating one row at a time.
- For very large CSVs, consider `read_csv(..., chunksize=...)`.
- Profile before optimizing.

## 18. Portfolio checklist

- [ ] Clear business question and dataset source.
- [ ] Schema and data-quality audit.
- [ ] Reproducible cleaning rules.
- [ ] Correct joins and validated metrics.
- [ ] Useful group summaries and charts.
- [ ] Evidence-based findings and limitations.
- [ ] README, dependencies, and reproducible execution instructions.

**Core habit:** Before every operation, identify the question, expected output, and assumptions. Then validate the result. That is how pandas becomes a reliable analysis tool rather than just a collection of methods.
