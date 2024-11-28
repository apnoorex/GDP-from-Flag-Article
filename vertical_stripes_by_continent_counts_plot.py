import pandas as pd
import matplotlib.pyplot as plt


countries = pd.read_csv('in_data/world_flags_2024.csv')

countries = countries[countries['StripesVertical'] == 1]
vert_stripes_countes = countries.groupby(['Continent'], as_index=False).size().rename(columns={'size': 'Size'}).sort_values('Size', ascending=False)
# print(vert_stripes_countes)

plt.figure(figsize=(10, 4))
plt.bar(vert_stripes_countes['Continent'], vert_stripes_countes['Size'], color='#3a8a8d')

plt.ylabel('Number of countries')
plt.savefig('out_data/VerticalStripeByContinent.png')
plt.show()
