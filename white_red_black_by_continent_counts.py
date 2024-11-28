import pandas as pd


countries = pd.read_csv('in_data/world_flags_2024.csv')

countries['WRB'] = countries['White'] & countries['Red'] & countries['Black']
countries = countries[countries['WRB'] == 1]

rwb_countes = countries.groupby(['Continent'], as_index=False).size().rename(columns={'size': 'Size'}).sort_values('Size', ascending=False)
print(rwb_countes)
