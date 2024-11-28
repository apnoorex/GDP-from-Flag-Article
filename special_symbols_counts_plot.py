import pandas as pd
import matplotlib.pyplot as plt


def has_a_symbol(entry):
    if entry:
        return 'Yes'
    return 'No'

countries = pd.read_csv('in_data/world_flags_2024.csv')

symbols_columns = ['LeftTriangle', 'Canton', 'Cross', 'Crescent', 'Stars', 'Sun', 'Bird', 'Circle', 'BlazonOrOther']
countries['TotalMarks'] = countries[symbols_columns].sum(axis=1)
countries['HasSymbol'] = countries['TotalMarks'].apply(has_a_symbol)
# print(countries[['Country', 'HasSymbol']].head(20))

symbols_counts = countries.groupby(['HasSymbol'], as_index=False).size().rename(columns={'size': 'Size'}).sort_values('Size', ascending=False)
print(symbols_counts)

plt.figure(figsize=(10, 4))
plt.bar(symbols_counts['HasSymbol'], symbols_counts['Size'], color='#3a8a8d')

plt.ylabel('Number of countries')
plt.savefig('out_data/FlagsWithSymbols.png')
plt.show()
