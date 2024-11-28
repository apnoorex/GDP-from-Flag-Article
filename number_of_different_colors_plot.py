import pandas as pd
import matplotlib.pyplot as plt


countries = pd.read_csv('in_data/world_flags_2024.csv')

color_columns = ['White', 'Red', 'Blue', 'Black', 'Yellow', 'Green', 'Orange', 'OtherColor']
countries['TotalColors'] = countries[color_columns].sum(axis=1)
# print(countries[['Country', 'TotalColors']].head(20))

color_counts = countries.groupby(['TotalColors'], as_index=False).size().rename(columns={'size': 'Size'}).sort_values('Size', ascending=False)
print(color_counts)

plt.figure(figsize=(10, 4))
plt.bar(color_counts['TotalColors'], color_counts['Size'], color='#3a8a8d')

plt.ylabel('Number of countries')
plt.savefig('out_data/NColorCounts.png')
plt.show()
