import numpy as np
import pandas as pd

X, Y = 5000, 4
np.random.seed(0)
df = pd.DataFrame(np.random.randint(10, size = (X, Y)))

print(df.head())
print()

#(1) Find the row with the highest sum of numbers in the row.
df[4] = df.sum(axis=1)
#print(df.head())

# Question - it returns only first max?

print('The row with the highest sum of numbers in the row: ', df[4].idxmax())

#(2) Find the number of unique rows in df.

def get_str(row):
    temp_list = []
    for i in row[0:4]:
        temp_list.append(str(i))
    return(''.join(temp_list))

df[5] = df.apply(get_str, axis=1)
#print(df.head())

print('The number of unique rows: ', df[5].nunique())

# (3) Which row occurs in df most often?
print('The row which occurs in dataframe most often: ', df[5].value_counts().idxmax())

#Question: there is another row with the same frequency -  what to do then?