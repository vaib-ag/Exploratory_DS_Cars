
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats


#https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
#https://towardsdatascience.com/exploratory-data-analysis-in-python-c9a77dfa39ce
#https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
#https://www.dataoptimal.com/data-science-projects-2018/



# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

print("---Start----")
df = pd.read_csv("data.csv")
print(df.head(5))
#print(df.dtypes)
print("------------------------")
print(df.count())

# Dropping irrelevant columns
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
print(df.head(5))

df=df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "MSRP": "Price"})
print(df.head(5))

print(df.shape)
# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)

print(df.count())

df=df.drop_duplicates()
print(df.shape)
print(df.count())


print("------------Start isNUll ------------")
print(df.isnull().sum())


print("------------Start count ------------")
df=df.dropna()
print(df.count())
print(df.isnull().sum())

#sns.boxplot(x=df['Price'])


print("------------Start zScore ------------")
z = np.abs(stats.zscore(df['Price']))
print(z)
threshold = 3
array_outliners_zIndex=np.where(z > threshold)
print(array_outliners_zIndex)

print(z[444])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df = df[~((df < (Q1-1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print(df.shape)

sns.boxplot(x=df['Year'])