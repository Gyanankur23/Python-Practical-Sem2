---
# Python Practicals - Semester 2

This repository contains all 9 Python practicals for Semester 2, alongside this structured `README.md` file. Below you'll find details, examples, and highlights of important practicals.

---

## 📋 Contents

- **Practical 1** - Tuples: Concatenation, sorting, unpacking, and cloning.
- **Practical 2** - Tuples: Size, length, duplicate removal, and flattening.
- **Practical 3** - Tuples and HTML: Immutability, retrieval from HTML file, replace/search operators, current date/time.
- **Practical 4** - Dates and Time: Time class, timedelta, strptime, strftime, and remaining days.
- **Practical 5** - Dates and Numpy: Timestamp to datestamp, compare two dates, calendar module, numpy arrays.
- **Practical 6** - Numpy Basics: Min, mean, reverse array, add rows/columns.
- **Practical 7** - Numpy Operations: Arithmetic operations, slicing, sorting, filtering.
- **Practical 8** - Pandas Basics: DataFrame, Series, arithmetic operations, concatenation.
- **Practical 9** - Pandas Operations: Filtering >90%, joining DataFrames, selecting rows, removing duplicates.

---

## ✅ Practicals and Code Snippets

### **Practical 1: Tuples**
```python
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4)

# Sorting
tup = (4, 1, 3)
sorted_tup = tuple(sorted(tup))
print(sorted_tup)  # (1, 3, 4)

# Unpacking
a, b, c = (10, 20, 30)
print(a, b, c)  # 10 20 30

# Cloning
original = (1, 2, 3)
clone = tuple(original)
print(clone)  # (1, 2, 3)

Practical 2: Tuples

# Finding Size
tup = (10, 20, 30)
print(len(tup))  # 3

# Removing Duplicates
tup = (1, 2, 2, 3)
unique = tuple(set(tup))
print(unique)  # (1, 2, 3)

# Flattening Tuples
nested = ((1, 2), (3, 4))
flat = tuple(i for sub in nested for i in sub)
print(flat)  # (1, 2, 3, 4)

# Getting Length
tup = (10, 20, 30)
print(len(tup))  # 3

Practical 3: Tuples and HTML

# Immutability
tup = (10, 20, 30)
# tup[0] = 40  # This would raise TypeError

# Retrieve from HTML
import re
content = "<p>Sample</p>"
text = re.sub(r'<.*?>', '', content)
print(text)  # Sample

# Replace/Search
s = "Hello world"
print(s.replace("world", "Python"))  # Hello Python

# Current Date and Time
from datetime import datetime
now = datetime.now()
print(now)

Practical 4: Dates and Time

# Time Class
from datetime import time
t = time(14, 30, 0)
print(t)  # 14:30:00

# Timedelta
from datetime import timedelta
delta = timedelta(days=5, hours=3)
print(delta)  # 5 days, 3:00:00

# Strptime
from datetime import datetime
dt = datetime.strptime("2025-04-18", "%Y-%m-%d")
print(dt)

# Strftime
now = datetime.now()
print(now.strftime("%d/%m/%Y %H:%M:%S"))

Practical 5: Dates and Numpy

# Timestamp to Datestamp
from datetime import datetime
timestamp = 1681903620
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)

# Compare Two Dates
from datetime import date
d1 = date(2025, 4, 18)
d2 = date(2025, 5, 1)
print(d2 > d1)  # True

# Calendar Module
import calendar
print(calendar.month(2025, 4))

# Numpy Array
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr)

Practical 6: Numpy Basics

# Minimum Value
arr = np.array([5, 2, 9, 1])
print(np.min(arr))  # 1

# Mean Value
arr = np.array([1, 2, 3, 4])
print(np.mean(arr))  # 2.5

# Reverse Array
arr = np.array([1, 2, 3, 4])
print(arr[::-1])  # [4, 3, 2, 1]

# Add Rows/Columns
arr = np.array([[1, 2], [3, 4]])
new_row = np.array([5, 6])
arr = np.vstack([arr, new_row])
print(arr)

Practical 7: Numpy Operations

# Arithmetic Operations
arr = np.array([10, 20, 30])
print(arr + 10)  # [20, 30, 40]

# Slicing
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # [2, 3, 4]

# Sorting
arr = np.array([5, 1, 4, 2])
print(np.sort(arr))  # [1, 2, 4, 5]

# Filtering
arr = np.array([1, 2, 3, 4, 5])
filtered = arr[arr > 3]
print(filtered)  # [4, 5]

Practical 8: Pandas Basics

# Create a DataFrame
import pandas as pd
data = {'Name': ['John', 'Alice'], 'Score': [85, 90]}
df = pd.DataFrame(data)
print(df)

# Create a Series
series = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(series)

# Arithmetic Operations on Series
s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
print(s1 + s2)  # [4, 6]

# Concatenation
df1 = pd.DataFrame({'A': [1], 'B': [2]})
df2 = pd.DataFrame({'A': [3], 'B': [4]})
df = pd.concat([df1, df2])
print(df)

Practical 9: Pandas Operations

# Filter Rows >90%
df = pd.DataFrame({'Name': ['John', 'Alice'], 'Score': [95, 88]})
filtered = df[df['Score'] > 90]
print(filtered)

# Join Two DataFrames
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['John', 'Alice']})
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 95]})
merged = pd.merge(df1, df2, on='ID')
print(merged)

# Select Rows Based on Column Values
df = pd.DataFrame({'Name': ['John', 'Alice'], 'Score': [95, 88]})
selected = df[df['Name'] == 'John']
print(selected)

# Filter Duplicate Values
df = pd.DataFrame({'Name': ['John', 'Alice', 'John']})
df = df.drop_duplicates()
print(df)


---

🚀 Important Questions

Practical 3: Tuples and HTML

# What is the immutability of tuples?
tup = (1, 2, 3)
# tup[0] = 0  # Raises TypeError
print(tup)

# How to retrieve plain text from an HTML string?
import re
html = "<p>This is a paragraph</p>"
text = re.sub(r'<.*?>', '', html)
print(text)

# How to replace all occurrences of a word in a string?
text = "Hello world, world is beautiful."
updated_text = text.replace("world", "Python")
print(updated_text)

# Current date and time
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

Practical 5: Dates and Numpy

# Convert UNIX timestamp
from datetime import datetime
timestamp = 1681903620
dt = datetime.fromtimestamp(timestamp)
print(dt)

# Compare two dates
from datetime import date
d1 = date(2025, 4, 18)
d2 = date(2025, 5, 1)
print(d1 < d2)

# Print calendar
import calendar
print(calendar.month(2025, 4))

# NumPy min and mean
import numpy as np
arr = np.array([10, 20, 30])
print(np.min(arr), np.mean(arr))

Practical 6: Numpy Basics

# Reverse NumPy array
arr = np.array([1, 2, 3, 4])
print(arr[::-1])

# Add a row to 2D array
arr = np.array([[1, 2], [3, 4]])
new_row = np.array([5, 6])
arr = np.vstack([arr, new_row])
print(arr)

# Element-wise addition
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
print(arr1 + arr2)

# Sort NumPy array
arr = np.array([5, 2, 8, 1])
print(np.sort(arr))

Practical 8: Pandas Basics

# Create DataFrame
import pandas as pd
data = {'Name': ['John', 'Alice'], 'Score': [85, 90]}
df = pd.DataFrame(data)
print(df)

# Create Series
series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series)

# Arithmetic on Series
s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
print(s1 + s2)

# Concatenate DataFrames
df1 = pd.DataFrame({'A': [1], 'B': [2]})
df2 = pd.DataFrame({'A': [3], 'B': [4]})
df = pd.concat([df1, df2])
print(df)

Practical 9: Pandas Operations

# Filter rows >90%
df = pd.DataFrame({'Name': ['John', 'Alice'], 'Score': [95, 88]})
filtered = df[df['Score'] > 90]
print(filtered)

# Join DataFrames
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['John', 'Alice']})
df2 = pd.DataFrame({'ID': [1, 2], 'Score': [90, 95]})
merged = pd.merge(df1, df2, on='ID')
print(merged)

# Select rows with condition
df = pd.DataFrame({'Name': ['John', 'Alice'], 'Score': [95, 88]})
selected = df[df['Name'] == 'John']
print(selected)

# Remove duplicates
df = pd.DataFrame({'Name': ['John', 'Alice', 'John']})
df = df.drop_duplicates()
print(df)


---

📜 Closing Note

This repository is developed by Gyanankur, and all solutions are tailored for academic and learning purposes.

> Copyright All rights reserved. Unauthorized use, distribution, or reproduction is strictly prohibited.



To explore the codes further, clone the repository:

git clone https://github.com/Gyanankur23/Python-Practical-Sem2.git

Happy coding!
