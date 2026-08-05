# Data Cleaning Projects

Three real-world data cleaning projects across different domains — sales, sports, and education — showcasing recovery-based cleaning rather than simple deletion of missing data.

Each project follows the same core process:
1. Inspect the raw data to find hidden issues (fake missing values, wrong types)
2. Convert columns to their correct data types
3. Recover missing values mathematically where possible, instead of deleting them
4. Fill unrecoverable categorical gaps with an honest placeholder
5. Drop only what truly cannot be fixed
6. Verify the final dataset is fully clean

---

## 1. Cafe Sales Data Cleaning
**Folder:** `cafe-sales/`

The raw dataset had disguised missing values (`"ERROR"`, `"UNKNOWN"` used as literal text instead of real missing values), causing every column — including numeric ones — to load as text instead of numbers.

**What I did:**
- Converted all disguised junk values into real missing values
- Fixed data types (numbers and dates were stored as text)
- Recovered missing `Quantity`, `Price Per Unit`, and `Total Spent` values using their mathematical relationship (e.g. `Total = Quantity × Price`) instead of deleting incomplete rows
- Filled unrecoverable categorical gaps (`Item`, `Payment Method`, `Location`) with `"Unknown"`
- Dropped only the rows where no data existed to recover from

**Result:** Preserved hundreds of rows that a basic cleanup would have discarded.

---

## 2. 2026 World Cup Player Stats Cleaning
**Folder:** `world-cup-stats/`

The raw dataset had missing values only in categorical/text columns (`Club`, `SecondPos`), with no numeric relationships to recover from.

**What I did:**
- Inspected the dataset to confirm missing data was limited to non-numeric columns
- Filled missing categorical values with `"Unknown"` — the appropriate fix here since no formula could reconstruct these fields

**Result:** A clean, sorted dataset ready for further sports analytics.

---

## 3. Student Performance Data Cleaning
**Folder:** `students-performances/`

The raw dataset had missing values only in categorical/text column `parental_education`, with no numeric relationships to recover from.

**What I did:**
- Inspected the dataset to confirm missing data was limited to non-numeric columns
- Filled missing categorical values with `"Unknown"` — the appropriate fix here since no formula could reconstruct these fields

**Result:** A clean, sorted dataset ready for further academic performance analytics.

---

## Skills Demonstrated
- Data inspection and diagnosis (pandas `.info()`, `.isnull()`, `.unique()`)
- Type conversion (`pd.to_numeric`, `pd.to_datetime`)
- Conditional data recovery using boolean masks and `.loc`
- Judgment-based cleaning decisions (recover vs. fill vs. drop)
- Clean, documented, reproducible Python scripts
