# IC-2K23-50-Keshav-Sharma-
# Artificial Intelligence Lab - Lab 3: Data Preprocessing & Exploratory Data Analysis (EDA)

**Student Details:**
- **Roll No:** IC-2K23-50
- **Name:** Keshav Sharma

---

## Overview

This repository contains implementations of foundational Data Preprocessing, Data Cleaning, and Exploratory Data Analysis (EDA) routines using **Python** and **pandas**. These scripts form the data preparation pipeline necessary before training machine learning models or performing statistical analysis.

---

## Table of Contents

1. [Dataset Loading](#1-dataset-loading)
2. [Data Cleaning](#2-data-cleaning)
3. [Exploratory Data Analysis (EDA)](#3-exploratory-data-analysis-eda)
4. [Prerequisites & Execution](#prerequisites--execution)

---

## 1. Dataset Loading

- **File:** [`Dataset_Loading.py`](Dataset_Loading.py)
- **Description:** Implements loading and initial inspection of tabular data from a CSV file.
- **Key Operations:**
  - `pd.read_csv("data.csv")`: Reads the dataset into a pandas DataFrame.
  - `df.head()`: Displays the first 5 rows of the dataset.
  - `df.info()`: Prints a concise summary of the DataFrame including index type, column types, non-null value counts, and memory usage.

### Running the Script:
```bash
python3 Dataset_Loading.py
```

---

## 2. Data Cleaning

- **File:** [`Data_Cleaning.py`](Data_Cleaning.py)
- **Description:** Performs essential data sanitization and preprocessing steps to handle redundancy and inconsistencies in raw data.
- **Key Operations:**
  - **Duplicate Removal:** Drops duplicate rows using `df.drop_duplicates()`.
  - **Empty Row Handling:** Removes rows where all column values are missing with `df.dropna(how="all")`.
  - **Column Whitespace Stripping:** Trims leading and trailing whitespace from column headers (`df.columns.str.strip()`).
  - **String Sanitization:** Iterates through all object/string columns and strips leading/trailing whitespaces (`df[column].str.strip()`).
  - **Verification:** Inspects the cleaned data preview (`df.head()`) and the post-cleaning dimensions (`df.shape`).

### Running the Script:
```bash
python3 Data_Cleaning.py
```

---

## 3. Exploratory Data Analysis (EDA)

- **File:** [`Exploratory_Data_Analysis.py`](Exploratory_Data_Analysis.py)
- **Description:** Conducts preliminary investigation on data to uncover patterns, spot anomalies, test hypotheses, and verify assumptions with summary statistics.
- **Key Operations:**
  - **Head & Tail Inspection:** Inspects first and last 5 rows using `df.head()` and `df.tail()`.
  - **Dimensionality:** Checks number of rows and columns with `df.shape`.
  - **Column Names & Schema:** Lists column names (`df.columns`) and their data types (`df.dtypes`).
  - **Statistical Summary:** Computes central tendency, dispersion, and shape of dataset's distribution using `df.describe()`.
  - **Cardinality:** Identifies the count of distinct elements per column using `df.nunique()`.
  - **Missing Values:** Identifies total null/missing values per feature using `df.isnull().sum()`.

### Running the Script:
```bash
python3 Exploratory_Data_Analysis.py
```

---

## Prerequisites & Execution

### Prerequisites
Make sure Python 3 and `pandas` are installed in your environment:
```bash
pip install pandas
```

> **Note:** Ensure `data.csv` is present in the `Lab-3` directory before executing the scripts.
