import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

health_exp = sns.load_dataset('healthexp')
#print(type(health_exp)) #it's already df, nice
#print(health_exp.head(10))
#print()

#filtering - only years with at least 5 countries
country_counts = health_exp.groupby('Year')['Country'].nunique()
valid_years = country_counts[country_counts >= 5].index
filtered_health_exp = health_exp[health_exp['Year'].isin(valid_years)]

#print(filtered_health_exp.head())

# (1) Which country has the highest average life expectancy?
avg_life_exp = filtered_health_exp.groupby('Country')['Life_Expectancy'].mean()
max_avg_country = avg_life_exp.idxmax()
max_avg_value = avg_life_exp.max()

print(f'Country with the highest average life expectancy: {max_avg_country} ({max_avg_value:.2f} years)')

# Which country had most often the highest life expectancy in a given year?
top_each_year = filtered_health_exp.loc[filtered_health_exp.groupby('Year')['Life_Expectancy'].idxmax()]
top_counts = top_each_year['Country'].value_counts()
most_frequent_top_country = top_counts.idxmax()
most_frequent_top_count = top_counts.max()

print(f"Country that most often had the highest life expectancy: {most_frequent_top_country} ({most_frequent_top_count} times)")

#(3) Which country had most often the highest health expenditures in a given year?
top_health_exp_per_year = filtered_health_exp.loc[filtered_health_exp.groupby('Year')['Spending_USD'].idxmax()]
health_exp_top_counts = top_health_exp_per_year['Country'].value_counts()
most_frequent_spender = health_exp_top_counts.idxmax()
most_frequent_spender_count = health_exp_top_counts.max()

print(f"Country that most often had the highest health expenditures: {most_frequent_spender} ({most_frequent_spender_count} times)")

#(4) Does it sometime happen that the country with the highest expenditures has the lowest life expectancy?
top_spenders = filtered_health_exp.loc[filtered_health_exp.groupby('Year')['Spending_USD'].idxmax()]

lowest_life_exp = filtered_health_exp.loc[filtered_health_exp.groupby('Year')['Life_Expectancy'].idxmin()]

comparison = top_spenders[['Year', 'Country']].merge(
    lowest_life_exp[['Year', 'Country']],
    on='Year',
    suffixes=('_spender', '_lowest_life_exp')
)

mismatch_years = comparison[comparison['Country_spender'] == comparison['Country_lowest_life_exp']]

if not mismatch_years.empty:
    print("Highest spending and lowest life expectancy:")
    print(mismatch_years)
else:
    print("Highest spending and lowest life expectancy is never the case.")


print(
    'There is no way to say if we can buy health,',
    'because the USA healthcare system is one of the most expensive in the world.',
    'The fact that they spend a lot of money does not guarantee that they provide more healthcare services.')