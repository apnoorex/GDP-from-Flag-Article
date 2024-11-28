import pandas as pd


countries = pd.read_csv('in_data/world_flags_2024.csv')

countries['IsAsia'] = countries['Continent'].apply(lambda x: 1 if x == 'Asia' else 0)

has_circle = sum(countries['Circle'])
print('Total flags with a circle:', has_circle)
asia_and_circle = sum(countries['IsAsia'] & countries['Circle'])
print('In Asia:', asia_and_circle)

df = countries[countries['Circle'] == 1]
print(df[['Country', 'Circle']].head(10))
