import pandas as pd
import matplotlib.pyplot as plt


countries = pd.read_csv('in_data/world_flags_2024.csv')

aspect_counts = countries.groupby(['AspectRatio'], as_index=False).size().rename(columns={'size': 'Size'}).sort_values('Size', ascending=False)
# print(aspect_counts)

plt.figure(figsize=(10, 4))
plt.bar(aspect_counts['AspectRatio'], aspect_counts['Size'], color='#3a8a8d')

plt.xlabel('Aspect Ratio')
plt.xticks(rotation=90)
plt.ylabel('Number of countries')
plt.savefig('out_data/AspectRatioCounts.png')
plt.show()

# % of countries with a unique flag aspect ratio
number_of_unique = sum(aspect_counts['Size'] == 1)
portion_of_unique = number_of_unique / len(countries) * 100

print(number_of_unique)
print(portion_of_unique)
