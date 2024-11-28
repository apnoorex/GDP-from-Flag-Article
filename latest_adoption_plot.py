import pandas as pd
import matplotlib.pyplot as plt


def cat_by_year(entry):
    if entry < 1900:
        return 'before 1900'
    elif entry < 1950:
        return '1900-1949'
    elif entry < 2000:
        return '1950-2000'
    else:
        return '2000-2024'

countries = pd.read_csv('in_data/world_flags_2024.csv')
year_category = countries[['LatestAdoption']].copy()

year_category['YearCat'] = countries['LatestAdoption'].apply(cat_by_year)
year_category = year_category.groupby(['YearCat'], as_index=False).size().rename(columns={'size': 'Size'})
year_category = year_category.reindex([3, 0, 1, 2])
# print(year_category.head())

plt.figure(figsize=(10, 4))
plt.bar(year_category['YearCat'], year_category['Size'], color='#3a8a8d')
plt.ylabel('Number of countries')
plt.savefig('out_data/LatestAdoption.png')
plt.show()
