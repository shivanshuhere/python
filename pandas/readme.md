
# 🐼 **Pandas**

---

##  1. **Import Pandas**

```python
import pandas as pd
```

---

##  2. **Create Series and DataFrame**

###  Series

```python
# Creating a Series
s = pd.Series([10, 20, 30, 40])
print("Series:")
print(s)
```

###  DataFrame

```python
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
```

---

##  3. **Read Data from Files**

```python
# CSV
# df = pd.read_csv('students.csv')

# Excel
# df = pd.read_excel('students.xlsx')

# JSON
  df = pd.read_json('students.json')
```

---

##  4. **View and Understand Data**

```python
print("\nHead:")
print(df.head())

print("\nTail:")
print(df.tail())

print("\nShape:", df.shape)
print("\nColumns:", df.columns)

print("\nInfo:")
print(df.info())

print("\nDescription:")
print(df.describe())
```

---

##  5. **Select Rows and Columns**

```python
print("\nSingle Column:")
print(df['Name'])

print("\nMultiple Columns:")
print(df[['Name', 'Age']])

print("\nSingle Row (iloc):")
print(df.iloc[0])

print("\nSingle Row (loc):")
print(df.loc[0])

print("\nSingle Cell (loc):", df.loc[0, 'Name'])
print("Single Cell (iloc):", df.iloc[0, 1])
```

---

##  6. **Filter Rows**

```python
print("\nAge > 28:")
print(df[df['Age'] > 28])

print("\nName is Bob:")
print(df[df['Name'] == 'Bob'])
```

---

##  7. **Add, Modify, Rename, Drop Columns**

```python
# Add column
df['Gender'] = ['F', 'M', 'M']
print("\nAfter Adding Gender:")
print(df)

# Modify column
df['Age'] = df['Age'] + 1
print("\nAfter Increasing Age:")
print(df)

# Rename column
df.rename(columns={'Name': 'FullName'}, inplace=True)
print("\nAfter Renaming Name to FullName:")
print(df)

# Drop column
df.drop('Gender', axis=1, inplace=True)
print("\nAfter Dropping Gender:")
print(df)
```

---

##  8. **Missing Values**

```python
# Adding missing value for demo
df.loc[1, 'Age'] = None
print("\nDataFrame with Missing Value:")
print(df)

# Check missing
print("\nMissing Values:")
print(df.isnull())

# Fill missing 
df['Age'].fillna(10, inplace=True)
print("\nAfter Filling Missing Age:")
print(df)

# Drop rows with missing values (if any)
# df.dropna(inplace=True)
```

---

##  9. **Sorting Data**

```python
# Sort by Age ascending
print("\nSorted by Age (Asc):")
print(df.sort_values(by='Age'))

# Sort by Age descending
print("\nSorted by Age (Desc):")
print(df.sort_values(by='Age', ascending=False))
```

---

##  10. **Group By and Aggregation**

```python
# Add Gender back
df['Gender'] = ['F', 'M']

# Group by Gender and average Age
print("\nGroup by Gender (Mean Age):")
print(df.groupby('Gender')['Age'].mean())

# Sum, Mean
print("\nSum of Ages:", df['Age'].sum())
print("Average Age:", df['Age'].mean())
```

---

-

##  11. **Export Data**

```python
# Save to CSV and Excel
# df.to_csv('updated_data.csv', index=False)
df.to_excel('updated_data.xlsx', index=False)
```

---
