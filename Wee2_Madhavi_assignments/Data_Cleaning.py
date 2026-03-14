import numpy as np
import pandas as pd
import Loading_Sales_data as sales

# checking missing values in each colomn
df= sales.new_data
#missing_values = df.isnull().sum()
#print("Missing Values per Column:")
#print(missing_values)

#let's create a copy and artificially introduce some missing data
df_practice = df.copy()
# Force the first 5 'Sales' values to be NaN (Not a Number)
df_practice.loc[0:4, 'Sales'] = np.nan 

# Check the first few rows to see the missing values
print("\n--- Artificial Missing Values Created ---")
print(df_practice['Sales'].head(7))