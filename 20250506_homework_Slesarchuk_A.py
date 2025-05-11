import pandas as pd

who = pd.read_csv('who.csv', sep = '\t')
#print(who.head())
#print(who.info())

# 1 - find redundant columns

def find_redundant_columns(who):
    redundant_pairs = []

    # iterate through all column pairs
    cols = who.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            col1, col2 = cols[i], cols[j]

            # if group1.max() == 1, it means every value in col1 maps to exactly one value in col2,
            # same for group2
            group1 = who[[col1, col2]].dropna().groupby(col1)[col2].nunique()
            group2 = who[[col1, col2]].dropna().groupby(col2)[col1].nunique()
            if group1.max() == 1 and group2.max() == 1:
                redundant_pairs.append((col1, col2))
    return redundant_pairs

# find redundant columns
print("Redundant columns:", find_redundant_columns(who))

#2 - plot all new cases as a function of time

import matplotlib.pyplot as plt

# Step 1: Identify columns related to new cases
case_cols = [col for col in who.columns if col.startswith('new_')]

# Step 2: Create a new column for total new cases
who['total_new_cases'] = who[case_cols].sum(axis=1, skipna=True)

# Step 3: Group by year and sum
cases_by_year = who.groupby('year')['total_new_cases'].sum()

# Step 4: Plot
plt.figure(figsize=(10, 6))
cases_by_year.plot(kind='line', marker='o')
plt.title('Total New Cases by Year')
plt.xlabel('Year')
plt.ylabel('Total New Cases')
plt.grid(True)
plt.tight_layout()
plt.show()