import pandas as pd


countries = pd.read_csv('in_data/world_flags_2024.csv')

countries['IsEurope'] = countries['Continent'].apply(lambda x: 1 if x == 'Europe' else 0)

has_cross = sum(countries['Cross'])
print('Total flags with a cross:', has_cross)
europe_and_cross = sum(countries['IsEurope'] & countries['Cross'])
print('In Europe:', europe_and_cross)

df = countries[countries['Cross'] == 1]
print(df[['Country', 'Cross']].head(15))
