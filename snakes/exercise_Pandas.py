import pandas as pd
import numpy as np

# 1. Creating DataFrame
print("1. Creating DataFrame")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 75000, 80000],
    'Department': ['HR', 'IT', 'IT', 'Finance']
}
df = pd.DataFrame(data)
print(df)
print("\n")

# 2. Basic DataFrame Information
print("2. DataFrame Information")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Basic Statistics:\n", df.describe())
print("\n")

# 3. Data Selection
print("3. Data Selection")
print("Select 'Name' column:\n", df['Name'])
print("Select multiple columns:\n", df[['Name', 'Salary']])
print("Select first 2 rows:\n", df.head(2))
print("Select rows where Age > 30:\n", df[df['Age'] > 30])
print("\n")

# 4. Data Manipulation
print("4. Data Manipulation")
# Adding new column
df['Bonus'] = df['Salary'] * 0.1
print("Added Bonus column:\n", df)

# Updating values
df.loc[df['Department'] == 'IT', 'Salary'] = df['Salary'] + 5000
print("Updated IT department salaries:\n", df)

# Handling missing values
df.loc[1, 'Age'] = np.nan
print("Introduced NaN:\n", df)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("Filled NaN with mean:\n", df)
print("\n")

# 5. Grouping and Aggregation
print("5. Grouping and Aggregation")
grouped = df.groupby('Department').agg({
    'Salary': ['mean', 'sum'],
    'Age': 'mean'
})
print("Department-wise statistics:\n", grouped)
print("\n")

# 6. Sorting
print("6. Sorting")
sorted_df = df.sort_values('Salary', ascending=False)
print("Sorted by Salary (descending):\n", sorted_df)
print("\n")

# 7. Merging DataFrames
print("7. Merging DataFrames")
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Eve'],
    'Performance': ['Excellent', 'Good', 'Average']
})
merged_df = pd.merge(df, df2, on='Name', how='left')
print("Merged DataFrame:\n", merged_df)
print("\n")

# 8. Pivot Table
print("8. Pivot Table")
pivot = df.pivot_table(values='Salary', index='Department', columns='Age', aggfunc='mean')
print("Pivot table (Salary by Department and Age):\n", pivot)
print("\n")

# 9. Time Series Data
print("9. Time Series Data")
dates = pd.date_range('2023-01-01', periods=31, freq='D')
sales = np.random.randint(100, 200, size=31)
df_time = pd.DataFrame({'Sales': sales}, index=dates)
print("Daily Sales:\n", df_time.head())
weekly_sales = df_time.resample('W').sum()
print("Weekly Sales:\n", weekly_sales)
rolling_mean = df_time.rolling(window=7).mean()
print("7-day Rolling Mean:\n", rolling_mean.head(10))
print("\n")

# 10. Multi-Indexing
print("10. Multi-Indexing")
arrays = [
    ['A', 'A', 'B', 'B'],
    ['X', 'Y', 'X', 'Y']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Subcategory'))
df_multi = pd.DataFrame({'Value': [10, 20, 30, 40]}, index=index)
print("Multi-Index DataFrame:\n", df_multi)
print("Select Category 'A':\n", df_multi.loc['A'])
print("Select Subcategory 'X':\n", df_multi.xs('X', level='Subcategory'))
print("\n")

# 11. Apply Function
print("11. Apply Function")
def range_func(x):
    return x.max() - x.min()
numerical_df = df.select_dtypes(include=[np.number])
column_ranges = numerical_df.apply(range_func)
print("Range of each numerical column:\n", column_ranges)
print("\n")

# 12. Transform Function
print("12. Transform Function")
df['Standardized_Salary'] = df.groupby('Department')['Salary'].transform(lambda x: (x - x.mean()) / x.std())
print("DataFrame with Standardized Salary:\n", df)
print("\n")